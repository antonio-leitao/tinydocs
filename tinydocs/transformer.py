# standard
import os
import re
from itertools import groupby

# self
from tinydocs.classes import Module, Routine, ClassObj


NOTECOUNT = 0
REFCOUNT = 0


def parameter_doc(parameter):
    desc = "\n".join(parameter.desc)
    docstring = f"<code>{parameter.name}</code>: {parameter.type}<br>&emsp;{desc}"
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


def summary_doc(summary: list) -> str:
    def match_callback(match):
        global NOTECOUNT
        NOTECOUNT += 1
        return f"[^{NOTECOUNT}]"

    entire_summary = "\n".join(summary)
    summary = re.sub(r"[\[](\d+)[\]]_", match_callback, entire_summary)

    return summary + "\n"


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


def warnings_doc(warnings: list[str]):
    docstring = "\n"
    for warning in warnings:
        docstring += f"\n> **Warning** {warning}\n"
    return docstring + "\n"


def references_doc(references: list[str]):
    def match_callback(match):
        global REFCOUNT
        REFCOUNT += 1
        return f"[^{REFCOUNT}]:"

    docstring = "\n\n"

    refs = []
    temp_list = []
    for i in range(len(references)):
        if references[i].startswith(".. ["):
            if temp_list:
                refs.append(temp_list)
                temp_list = []
        temp_list.append(references[i])
    if temp_list:
        refs.append(temp_list)

    for ref in refs:
        ref[0] = re.sub(r"\.\. ?[\[](\d+)[\]]", match_callback, ref[0])
        docstring += "\n".join(ref) + "\n"

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
    docs = "\n" + signature_doc("." + method.name, method.signature)
    if method.warnings:
        docs += warnings_doc(method.warnings)
    docs += summary_doc(method.summary)
    if method.parameters:
        docs += collapsable_doc("Parameters", parameter_list(method.parameters))
    if method.returns:
        docs += collapsable_doc("Returns", parameter_list(method.returns))
    if method.examples:
        docs += collapsable_doc("Examples", examples_doc(method.examples))
    if method.references:
        docs += references_doc(method.references)
    return docs


def routine_docstring(routine: Routine) -> str:
    docs = f'<h3 id="{routine.id}">{routine.name}</h3>\n'
    docs += signature_doc(routine.id, routine.signature)
    if routine.warnings:
        docs += warnings_doc(routine.warnings)
    docs += summary_doc(routine.summary)
    if routine.parameters:
        docs += collapsable_doc("Parameters", parameter_list(routine.parameters))
    if routine.returns:
        docs += collapsable_doc("Returns", parameter_list(routine.returns))
    if routine.examples:
        docs += collapsable_doc("Examples", examples_doc(routine.examples))
    if routine.references:
        docs += references_doc(routine.references)
    return docs


def class_docstring(obj: ClassObj) -> str:
    docs = f'<h3 id="{obj.id}">{obj.name}</h3>\n'
    docs += signature_doc(obj.id, obj.signature)
    if obj.warnings:
        docs += warnings_doc(obj.warnings)
    docs += summary_doc(obj.summary)
    if obj.parameters:
        docs += collapsable_doc("Parameters", parameter_list(obj.parameters))
    if obj.returns:
        docs += collapsable_doc("Returns", parameter_list(obj.returns))
    if obj.attributes:
        docs += collapsable_doc("Attributes", parameter_list(obj.attributes))
    if obj.methods:
        docs += collapsable_doc("Methods", format_methods(obj.methods))
    if obj.examples:
        docs += collapsable_doc("Examples", examples_doc(obj.examples))
    if obj.references:
        docs += references_doc(obj.references)

    return docs


def module_docstring(module: Module) -> str:
    docstring = f'<h1 id="{module.id}">{module.name}</h1>\n{module.doc}\n'
    for obj in module.classes:
        docstring += class_docstring(obj)
    for routine in module.routines:
        docstring += routine_docstring(routine)
    return docstring


def create_toc(dictionary: dict) -> str:
    common_prefix = os.path.commonprefix([key for key in dictionary.keys()])
    toc = "# Table of Contents \n\n"
    for key, value in dictionary.items():
        # depth = key.lstrip(".").count(".")
        depth = key.replace(common_prefix, "").count(".")
        toc += f"{'  ' * depth}- [{value}](#{key})\n"
    return toc + "\n"
