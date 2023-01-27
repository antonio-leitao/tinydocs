from numpydoc.docscrape import FunctionDoc, ClassDoc
import importlib
import inspect
import types
import sys
import os
from itertools import groupby
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Routine:
    id: str
    name: str
    signature: str
    summary: str
    parameters: list
    returns: list
    references: list
    examples: list


@dataclass
class ClassObj:
    id: str
    name: str
    signature: str
    summary: str
    parameters: list
    returns: list
    references: list
    attributes: list
    methods: list[Routine]
    examples: list


@dataclass
class Module:
    id: str
    name: str
    doc: str
    classes: list[ClassDoc]
    routines: list[FunctionDoc]


@dataclass
class Package:
    modules: list[Module] | None
    data: dict


class ErrorDuringImport(Exception):
    """Errors that occurred while trying to import something to document it."""

    def __init__(self, filename, exc_info):
        self.filename = filename
        self.exc, self.value, self.tb = exc_info

    def __str__(self):
        exc = self.exc.__name__
        return "problem in %s - %s: %s" % (self.filename, exc, self.value)


def _isclass(object):
    return inspect.isclass(object) and not isinstance(object, types.GenericAlias)


def _clean_name(path: str) -> str:
    mod_name = os.path.split(path)[-1].removesuffix(".py")
    mod_name = mod_name.replace("_", " ")
    return mod_name.capitalize()


def _importfile(path):
    """Import a Python source file or compiled file given its path."""
    magic = importlib.util.MAGIC_NUMBER
    with open(path, "rb") as file:
        is_bytecode = magic == file.read(len(magic))
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    if is_bytecode:
        loader = importlib._bootstrap_external.SourcelessFileLoader(name, path)
    else:
        loader = importlib._bootstrap_external.SourceFileLoader(name, path)
    # XXXWe probably don't need to pass in the loader here.
    spec = importlib.util.spec_from_file_location(name, path, loader=loader)
    try:
        return importlib._bootstrap._load(spec)
    except:
        raise ErrorDuringImport(path, sys.exc_info())


def dir_to_breadcrumbs(dirname: str) -> str:
    breadcrumbs = dirname.replace("/", ".")
    if dirname.endswith(".py"):
        return breadcrumbs[:-3]
    return breadcrumbs


def process_dir(
    dirpath: str,
    modules: list[Module],
    data: dict,
    excluded_dirs: list = [],
    excluded_files: list = [],
) -> None:
    for dirname in os.listdir(dirpath):
        path = os.path.join(dirpath, dirname)
        breadcrumbs = dir_to_breadcrumbs(path)
        if os.path.isdir(path):
            if dirname in excluded_dirs:
                continue
            if dirname.startswith("_"):
                continue
            data[breadcrumbs] = _clean_name(dirname)
            process_dir(path, modules, data, excluded_dirs, excluded_files)

        elif os.path.isfile(path):
            if not path.endswith(".py"):
                continue
            if dirname.startswith("_"):
                continue
            if dirname in excluded_files:
                continue
            modules.append(process_module(path, data, breadcrumbs))


def process_module(path: str, data: dict, breadcrumbs: str) -> str:
    module = _importfile(path)
    data[breadcrumbs] = _clean_name(module.__name__)

    # iterate through classes
    classes = []
    for name, node in inspect.getmembers(module, _isclass):
        crumbs = breadcrumbs + "." + name
        classes.append(process_class(name, crumbs, node))
        data[crumbs] = name

    # iterate throough functions
    routines = []
    for name, node in inspect.getmembers(module, inspect.isroutine):
        if name.startswith("_"):
            continue
        crumbs = breadcrumbs + "." + name
        routines.append(process_routine(name, crumbs, node))
        data[crumbs] = name

    mod = Module(
        id=breadcrumbs,
        name=_clean_name(module.__name__),
        doc=module.__doc__,
        routines=routines,
        classes=classes,
    )
    return mod


def process_class(name: str, crumbs: str, node) -> ClassObj:

    # get methods of class and document them
    methods = []
    for method_name, method in inspect.getmembers(node, inspect.isfunction):
        if method_name.startswith("_"):
            continue
        methods.append(process_routine(method_name, "", method))

    doc = ClassDoc(node)
    obj = ClassObj(
        id=crumbs,
        name=name,
        signature=str(inspect.signature(node)),
        summary=doc["Summary"] + doc["Extended Summary"] + doc["Notes"],
        parameters=doc["Parameters"] + doc["Other Parameters"],
        returns=doc["Returns"],
        attributes=doc["Attributes"],
        methods=methods,
        examples=doc["Examples"],
        references=doc["Notes"],
    )

    return obj


def process_routine(name: str, crumbs: str, node) -> Routine:
    doc = FunctionDoc(node)
    routine = Routine(
        id=crumbs,
        name=name,
        signature=str(inspect.signature(node)),
        summary=doc["Summary"] + doc["Extended Summary"] + doc["Notes"],
        parameters=doc["Parameters"] + doc["Other Parameters"],
        returns=doc["Returns"],
        examples=doc["Examples"],
        references=doc["Notes"],
    )
    return routine


def iterate_python_files(
    directory: str, excluded_dirs: list = [], excluded_files: list = []
) -> None:
    data = {}
    modules = []
    process_dir(directory, modules, data, excluded_dirs, excluded_files)
    return data, modules


############################# CREATE MARKDOWN ###################################

REFCOUNT = 0


def parameter_doc(parameter):
    desc = "\n".join(parameter.desc)
    docstring = f"<code>{parameter.name}</code>:{parameter.type}<br>&emsp;{desc}"
    return docstring


def parameter_list(parameter_list: list):
    docstring = "<ul>"
    for parameter in parameter_list:
        docstring += f"<li>{parameter_doc(parameter)}</li>"
    return docstring + "</ul>"


def collapsable_doc(title: str, content: str) -> str:
    docstring = (
        "<details closed><summary>&emsp;<b>"
        + title
        + "</b></summary><p/>"
        + content
        + "</details>"
    )
    return docstring


def summary_doc(summary):
    return "\n".join(summary)


def signature_doc(identifier: str, signature: str) -> str:
    docstring = f"\n```python\n{identifier+signature}\n```\n\n"
    return docstring


def examples_doc(examples: list) -> str:
    docstring = "\n"
    examples = [
        list(group) for k, group in groupby(examples, lambda x: x == "") if not k
    ]
    for example in examples:
        if example[0].startswith(">>>"):
            example = "\n".join(example)
            docstring += f"```python\n{example}\n```\n"
        else:
            example = "\n".join(example)
            docstring += f"\n{example}\n"
    return docstring


def format_methods(methods: list[Routine]) -> str:
    docstring = "<ul>"
    for method in methods:
        method_content = method_docstring(method)
        docstring += f"<li>{collapsable_doc(title=f'<code>{method.name}</code>',content=method_content)}</li>"
    return docstring + "</ul>"


def method_docstring(
    method: Routine,
) -> str:
    docs = signature_doc("." + method.name, method.signature)
    docs += summary_doc(method.summary)

    if method.parameters:
        docs += collapsable_doc("Parameters", parameter_list(method.parameters))
    if method.returns:
        docs += collapsable_doc("Returns", parameter_list(method.returns))
    if method.examples:
        docs += examples_doc(method.examples)
    return docs


def routine_docstring(routine: Routine) -> str:
    docs = f'<h2 id="{routine.id}">{routine.name}</h2>\n'
    docs += signature_doc(routine.id, routine.signature)
    docs += summary_doc(routine.summary)

    if routine.parameters:
        docs += collapsable_doc("Parameters", parameter_list(routine.parameters))
    if routine.returns:
        docs += collapsable_doc("Returns", parameter_list(routine.returns))
    if routine.examples:
        docs += examples_doc(routine.examples)
    return docs


def class_docstring(obj: ClassObj) -> str:
    docs = f'<h2 id="{obj.id}">{obj.name}</h2>\n'
    docs += signature_doc(obj.id, obj.signature)
    docs += summary_doc(obj.summary)
    if obj.parameters:
        docs += collapsable_doc("Parameters", parameter_list(obj.parameters))
    if obj.returns:
        docs += collapsable_doc("Returns", parameter_list(obj.returns))
    if obj.methods:
        docs += collapsable_doc("Methods", format_methods(obj.methods))
    if obj.attributes:
        docs += collapsable_doc("Attributes", parameter_list(obj.attributes))
    if obj.examples:
        docs += examples_doc(obj.examples)
    return docs


def module_docstring(module: Module) -> str:
    docstring = f'<h1 id="{module.id}">{module.name}</h1>\n{module.doc}\n'
    for obj in module.classes:
        docstring += class_docstring(obj)
    for routine in module.routines:
        docstring += routine_docstring(routine)
    return docstring


def write_docme(package: Package, path: str = "DOCME.md") -> None:

    docs = create_toc(package.data)
    for module in package.modules:
        docs += module_docstring(module)
    with open(path, "w") as file:
        file.write(docs)


def create_toc(dictionary):
    toc = "# Table of Contents \n\n"
    for key, value in dictionary.items():
        depth = key.count(".")
        toc += f"{'  ' * (depth-1)}- [{value}](#{key})\n"
    return toc + "\n"


def main(
    directory: str = "example",
    output: str = "DOCME.md",
    excluded_dirs: list = [],
    excluded_files: list = [],
) -> None:
    # args = get_cli_args
    data, modules = iterate_python_files(directory, excluded_dirs, excluded_files)
    package = Package(modules=modules, data=data)
    write_docme(package=package, path=output)


if __name__ == "__main__":
    main()
