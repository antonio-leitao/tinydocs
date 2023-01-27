# Table of Contents

- [Submodule](#example.submodule)
  - [Classes and funcs](#example.submodule.classes_and_funcs)
    - [UMAP](#example.submodule.classes_and_funcs.UMAP)
    - [UMAP_foo](#example.submodule.classes_and_funcs.UMAP_foo)
  - [Bigclass](#example.submodule.bigclass)
    - [BigClass](#example.submodule.bigclass.BigClass)
- [Utils module](#example.utils_module)
  - [bar](#example.utils_module.bar)
  - [foo](#example.utils_module.foo)
- [Module many classes](#example.module_many_classes)
  - [DBScan](#example.module_many_classes.DBScan)
  - [KMeans](#example.module_many_classes.KMeans)

<h1 id="example.submodule.classes_and_funcs">Classes and funcs</h1>
Docstring for the example.py module.

Modules names should have short, all-lowercase names. The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file. The
module's docstring may extend over multiple lines. If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

<h2 id="example.submodule.classes_and_funcs.UMAP">UMAP</h2>

```python
example.submodule.classes_and_funcs.UMAP(n_clusters=8)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

$$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

And even use a Greek symbol like $\omega$ inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details><details closed><summary>&emsp;<b>Methods</b></summary><p/><ul><li><details closed><summary>&emsp;<b><code>fit</code></b></summary><p/>

```python
.fit(self, X, y=None, sample_weight=None)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

$$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

And even use a Greek symbol like $\omega$ inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

Below is another example

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

</details></li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

<h2 id="example.submodule.classes_and_funcs.UMAP_foo">UMAP_foo</h2>

```python
example.submodule.classes_and_funcs.UMAP_foo(var1, var2, *args, long_var_name='hi', only_seldom_used_keyword=0, **kwargs)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

And even use a Greek symbol like :math:`\omega` inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

<h1 id="example.submodule.bigclass">Bigclass</h1>
Docstring for the example.py module.

Modules names should have short, all-lowercase names. The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file. The
module's docstring may extend over multiple lines. If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

<h2 id="example.submodule.bigclass.BigClass">BigClass</h2>

```python
example.submodule.bigclass.BigClass(n_clusters=8)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

$$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

And even use a Greek symbol like $\omega$ inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details><details closed><summary>&emsp;<b>Methods</b></summary><p/><ul><li><details closed><summary>&emsp;<b><code>fit</code></b></summary><p/>

```python
.fit(self, X, y=None, sample_weight=None)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

And even use a Greek symbol like :math:`\omega` inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

</details></li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

<h1 id="example.utils_module">Utils module</h1>
Docstring for the example.py module.

Modules names should have short, all-lowercase names. The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file. The
module's docstring may extend over multiple lines. If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

<h2 id="example.utils_module.bar">bar</h2>

```python
example.utils_module.bar(var1, var2, *args, long_var_name='hi', only_seldom_used_keyword=0, **kwargs)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

And even use a Greek symbol like :math:`\omega` inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

<h2 id="example.utils_module.foo">foo</h2>

```python
example.utils_module.foo(var1, var2, *args, long_var_name='hi', only_seldom_used_keyword=0, **kwargs)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

And even use a Greek symbol like :math:`\omega` inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

<h1 id="example.module_many_classes">Module many classes</h1>
Docstring for the example.py module.

Modules names should have short, all-lowercase names. The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file. The
module's docstring may extend over multiple lines. If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

<h2 id="example.module_many_classes.DBScan">DBScan</h2>

```python
example.module_many_classes.DBScan(n_clusters=8)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

And even use a Greek symbol like :math:`\omega` inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details><details closed><summary>&emsp;<b>Methods</b></summary><p/><ul><li><details closed><summary>&emsp;<b><code>fit</code></b></summary><p/>

```python
.fit(self, X, y=None, sample_weight=None)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

.. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

And even use a Greek symbol like :math:`\omega` inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

</details></li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

<h2 id="example.module_many_classes.KMeans">KMeans</h2>

```python
example.module_many_classes.KMeans(n_clusters=8)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

$$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

And even use a Greek symbol like $$\omega$$ inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details><details closed><summary>&emsp;<b>Methods</b></summary><p/><ul><li><details closed><summary>&emsp;<b><code>fit</code></b></summary><p/>

```python
.fit(self, X, y=None, sample_weight=None)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.
Notes about the implementation algorithm (if needed).

This can have multiple paragraphs.

You may include some math:

$$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

And even use a Greek symbol like $$\omega$$ inline.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>:array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array. We can also refer to
variables like `var1`.</li><li><code>var2</code>:int<br>&emsp;The type above can either refer to an actual Python type
(e.g. `int`), or describe the type of the variable in more
detail, e.g. `(N,) ndarray` or `array_like`.</li><li><code>\*args</code>:iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>:{'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>:int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>\*\*kwargs</code>:dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>:type<br>&emsp;Explanation of anonymous return value of type `type`.</li><li><code>describe</code>:type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>:type<br>&emsp;Explanation of `out`.</li><li><code></code>:type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```

</details></li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.

```python
>>> a = [1, 2, 3]
>>> print([x + 3 for x in a])
[4, 5, 6]
>>> print("a\nb")
a
b
```
