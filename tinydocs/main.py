""":: TINYDOCS ::
Lightweight autodoc for github README
"""

# standard
import os
import textwrap
import argparse
import importlib.metadata

# self
from tinydocs.transformer import create_toc, module_docstring
from tinydocs.parser import iterate_python_files
from tinydocs.classes import Package, TDSConfig


__version__ = importlib.metadata.version("tinydocs")


def write_docme(package: Package, path: str = "DOCME.md") -> None:

    docs = create_toc(package.data)
    for module in package.modules:
        docs += module_docstring(module)
    with open(path, "w") as file:
        file.write(docs)


def make_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(__doc__),
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {version}".format(version=__version__),
    )
    parser.add_argument(
        "-d",
        "--dir",
        help="""Path to directory. Defaults to working directory when not supplied.
        """,
        metavar="\b",
        default=os.path.relpath(os.getcwd()),
    )
    parser.add_argument(
        "-o",
        "--out",
        help="""Path of output md file. Defaults to --dir/TINYDOCS.md
        """,
        metavar="\b",
    )
    parser.add_argument(
        "-xd",
        "--exclude-dirs",
        nargs="+",
        help="""List of directories to exclude.
        """,
        metavar="\b",
    )
    parser.add_argument(
        "-xf",
        "--exclude-files",
        nargs="+",
        help="""List of files to exclude.
        """,
        metavar="\b",
    )
    return parser


def handle_args(args) -> TDSConfig:
    if not args.out:
        args.out = os.path.join(args.dir, "TINYDOCS.md")
    config = TDSConfig(
        directory=args.dir,
        output=args.out,
        excluded_dirs=args.exclude_dirs if args.exclude_dirs else [],
        excluded_files=args.exclude_files if args.exclude_files else [],
    )
    return config


def main() -> None:
    parser = make_parser()
    args = parser.parse_args()
    config = handle_args(args)
    data, modules = iterate_python_files(
        config.directory, config.excluded_dirs, config.excluded_files
    )
    package = Package(modules=modules, data=data)
    write_docme(package=package, path=config.output)


if __name__ == "__main__":
    main()
