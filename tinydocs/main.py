from classes import Package
from parser import iterate_python_files
from transformer import create_toc, module_docstring


def write_docme(package: Package, path: str = "DOCME.md") -> None:

    docs = create_toc(package.data)
    for module in package.modules:
        docs += module_docstring(module)
    with open(path, "w") as file:
        file.write(docs)


def main(
    directory: str = "examples",
    output: str = "TINYDOC.md",
    excluded_dirs: list = [],
    excluded_files: list = [],
) -> None:
    # args = get_cli_args
    data, modules = iterate_python_files(directory, excluded_dirs, excluded_files)
    package = Package(modules=modules, data=data)
    write_docme(package=package, path=output)


if __name__ == "__main__":
    main()
