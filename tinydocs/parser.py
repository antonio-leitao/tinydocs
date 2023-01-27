# standard
import importlib
import inspect
import types
import sys
import os

# self
from tinydocs.classes import FunctionDoc, ClassDoc, Routine, ClassObj, Module


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
            if dirname.startswith("."):
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
        warnings=doc["Warnings"],
        summary=doc["Summary"] + doc["Extended Summary"] + doc["Notes"],
        parameters=doc["Parameters"] + doc["Other Parameters"],
        returns=doc["Returns"],
        attributes=doc["Attributes"],
        methods=methods,
        examples=doc["Examples"],
        references=doc["References"],
    )

    return obj


def process_routine(name: str, crumbs: str, node) -> Routine:

    doc = FunctionDoc(node)

    routine = Routine(
        id=crumbs,
        name=name,
        signature=str(inspect.signature(node)),
        summary=doc["Summary"] + doc["Extended Summary"] + doc["Notes"],
        warnings=doc["Warnings"],
        parameters=doc["Parameters"] + doc["Other Parameters"],
        returns=doc["Returns"],
        examples=doc["Examples"],
        references=doc["References"],
    )
    return routine


def iterate_python_files(
    directory: str, excluded_dirs: list = [], excluded_files: list = []
) -> None:
    data = {}
    modules = []
    process_dir(directory, modules, data, excluded_dirs, excluded_files)
    return data, modules
