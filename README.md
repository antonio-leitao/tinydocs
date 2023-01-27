<h1 align="center">Tinydocs</h1>
<p align="center">
Lightweight autodoc for github.
</p>

Are you in need of a simple and efficient solution for documenting your Python code, without the hassle of setting up and maintaining a full-fledged documentation website like `readthedocs`? Do you want something that can quickly and easily be integrated into GitHub, allowing your team to quickly access the documentation for a few classes and helper functions? Look no further!

<h3 align="center">Tinydocs is right for you!</h3>

`readthedocs` automatically generates the documentation of your `.py` files in a small elegant way that fits in a simple `README.md`. Check out the example function below or the [example directory.](#https://github.com/antonio-leitao/tinydocs/tree/master/example)

#### Contents

- [Installation](#installation)
- [Example](#example)
- [Syntax](#syntax)
- [Basic Usage](#basic_usage)
- [Github Workflow](#github-workflow)

# Installation

Best way to install tinydocs is through pip:

```sh
pip install tinydocs
```

# Example

The following is an example of the documentation egenrated for a simple function. YOu can finde how `tinydocs` handles and entire directory by checking the [example directory](#https://github.com/antonio-leitao/tinydocs/tree/master/example).

## Function

```python
module.function(var1, var2, long_var_name=None, *args)
```

> **Warning** Deprecation: `function` will be removed in version 2.0.0, it is replaced by `better_function` because the new one is blazingly fast.

This is an example documentation.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Look at this really big equation that I took from [^1]

$$( \sum_{k=1}^n a_k b_k )^2 \leq ( \sum_{k=1}^n a_k^2 ) ( \sum_{k=1}^n b_k^2 )$$

<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>: array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array.  We can also refer to
variables like `var1`.</li><li><code>var2</code>: int<br>&emsp;The type above can either refer to an actual Python type
(e.g. ``int``), or describe the type of the variable in more
detail, e.g. ``(N,) ndarray`` or ``array_like``.</li><li><code>long_var_name</code>: {'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>*args</code>: iterable<br>&emsp;Other arguments.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code>var3</code>: int<br>&emsp;Returns `var3` which is of type ``int``.</li></ul></details><details closed><summary>&emsp;<b>Examples</b></summary><p/>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> b = deprecated_function(a)
>>> print(b)
[4,5,6]
```

</details>

[^1]: Trager, Scott. "The Earth's atmosphere: seeing, background, absorption & scattering" (PDF). S.C. Trager. Retrieved 31 May 2022

# Syntax

Currently `tinydocs` only supports [NumpyDoc](#https://numpydoc.readthedocs.io/en/latest/format.html) syntax. This might change in the future. For a detailed guide check out numpy's style guidelines you can also check-out the [example directory](#https://github.com/antonio-leitao/tinydocs/tree/master/example) of this project.

Here is the docstring that generates the documentation on the example above, taken mostly from [numpydoc's example](#https://numpydoc.readthedocs.io/en/latest/example.html#example).

```python
def function(var1, var2, long_var_name=None, *args):
    """This is an example documentation.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`.

    Parameters
    ----------
    var1 : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    var2 : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.
    *args : iterable
        Other arguments.

    Returns
    -------
    var3 : int
        Returns `var3` which is of type ``int``.

    Notes
    -----
    Look at this really big equation that I took from [1]_

    $$( \sum_{k=1}^n a_k b_k )^2 \leq ( \sum_{k=1}^n a_k^2 ) ( \sum_{k=1}^n b_k^2 )$$

    Warnings
    --------
    Deprecation Warning: `deprecated_function` will be removed in version 2.0.0, it is replaced by `better_function` because the new one is blazingly fast.

    References
    ----------
    .. [1] Trager, Scott. "The Earth's atmosphere: seeing, background, absorption & scattering" (PDF). S.C. Trager. Retrieved 31 May 2022

    Examples
    --------
    These are written in doctest format, and should illustrate how to
    use the function.

    >>> a = [1, 2, 3]
    >>> b = deprecated_function(a)
    >>> print(b)
    [4,5,6]
    """
    pass
```

# Basic Usage

`tinydocs` can be run directly from the command line using:

```sh
tinydocs <options>
```

> **Note** By design `--tinydocs` only looks at `.py` files and skips over hidden directories or files/functions/methods that start with "\_"(underscore).

- `--dir`: Directory to document. Defaults to working directory.
- `--output`: Output path and name of documentation file. Defaults to `--dir/TINYDOCS.md` when not supplied.
- `--exclude-dirs`: List of directories to exclude entirely from the documentation.
- `--exclude-files`: List of files to exclude individually from the documentation.
- `--help`: Help will always be given to those who ask for it.

# Github Workflow

`tinydocs` incorporates very well with automatic deployment allowing you to update your documentation on every push. Here's an example workflow on
`.github/workflows/tinydocs.yaml`:

```yaml
name: Update TINYDOCS.md

on:
  push:
    branches:
      - "*"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.10

      - name: Install tinydocs
        run: pip install tinydocs

      - name: Run tinydocs
        run: tinydocs

      - name: Commit and push TINYDOCS.md
        run: |
          git config --local user.email "github-actions@example.com"
          git config --local user.name "GitHub Actions"
          git add TINYDOCS.md
          git commit -m "Update TINYDOCS.md"
          git push
```
