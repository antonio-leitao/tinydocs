# Table of Contents 

- [Subfolder](#examples.subfolder)
  - [Module with class](#examples.subfolder.module_with_class)
    - [BigClass](#examples.subfolder.module_with_class.BigClass)
- [Module with functions](#examples.module_with_functions)
  - [better_function](#examples.module_with_functions.better_function)
  - [deprecated_function](#examples.module_with_functions.deprecated_function)

<h1 align="center" id="examples.subfolder.module_with_class">Module with class</h1>
Docstring for the module `module_with_class.py`.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.


<h2 id="examples.subfolder.module_with_class.BigClass">BigClass</h2>

```python
examples.subfolder.module_with_class.BigClass()
```

Summarize the class in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`. You can also add references here like [^1].
Or even in the seciont "Notes" below [2_]. Dont forget to add the link[^2] in the section "References otherwise it wont work".
Notes about the implementation algorithm (if needed). Cite the relevant literature, e.g. [^3]. This can include multiple paragraphs and even some math:

$$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

Math can be also inline: like $\omega$. Although you can put references in the Summary and Notes, you can only put am,th in this section.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>data</code>: array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array.  We can also refer to
variables like `var1`.</li><li><code>n_clusters</code>: int<br>&emsp;The type above can either refer to an actual Python type
(e.g. ``int``), or describe the type of the variable in more
detail, e.g. ``(N,) ndarray`` or ``array_like``.</li><li><code>*args</code>: iterable<br>&emsp;Other arguments.</li><li><code>long_var_name</code>: {'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>only_seldom_used_keyword</code>: int, optional<br>&emsp;Infrequently used parameters can be described under this optional
section to prevent cluttering the Parameters section.</li><li><code>**kwargs</code>: dict<br>&emsp;Other infrequently used keyword arguments. Note that all keyword
arguments appearing after the first parameter specified under the
Other Parameters section, should also be described under this
section.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code>self</code>: BigClass<br>&emsp;Returns self which is of type ``BigClass``.</li></ul></details><details closed><summary>&emsp;<b>Attributes</b></summary><p/><ul><li><code>score</code>: float<br>&emsp;Evaluation of the fit method ``BigClass``.</li><li><code>slope</code>: float<br>&emsp;Slope of the best-fit line according to OLS regression.</li></ul></details><details closed><summary>&emsp;<b>Methods</b></summary><p/><ul><li><details closed><summary>&emsp;<b><code>fit</code></b></summary><p/>

```python
.fit(self, X, y=None, sample_weight=None, *args)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>X</code>: array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array.  We can also refer to
variables like `var1`.</li><li><code>y</code>: int, optional<br>&emsp;The type above can either refer to an actual Python type
(e.g. ``int``), or describe the type of the variable in more
detail, e.g. ``(N,) ndarray`` or ``array_like``.</li><li><code>sample_weight</code>: array_like, optional<br>&emsp;The type above can either refer to an actual Python type
(e.g. ``int``), or describe the type of the variable in more
detail, e.g. ``(N,) ndarray`` or ``array_like``.</li><li><code>*args</code>: iterable<br>&emsp;Other arguments.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code></code>: type<br>&emsp;Explanation of anonymous return value of type ``type``.</li><li><code>describe</code>: type<br>&emsp;Explanation of return value named `describe`.</li><li><code>out</code>: type<br>&emsp;Explanation of `out`.</li><li><code></code>: type_without_description<br>&emsp;</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.
```python
>>> obj = BigClass().fit(X)
>>> print(obj.attributes)
[4, 5, 6]
>>> print("a\nb")
a
b
```
</details></li><li><details closed><summary>&emsp;<b><code>transform</code></b></summary><p/>

```python
.transform(self, X, *args)
```

Summarize the function in one line.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>X</code>: array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array.  We can also refer to
variables like `var1`.</li><li><code>*args</code>: iterable<br>&emsp;Other arguments.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code>Y</code>: numpy_array<br>&emsp;Numpy array with all the with the transformed values of the input</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.
```python
>>> obj = BigClass().fit(X)
>>> obj = BigClass().transform(Y)
[4, 5, 6]
>>> print("a\nb")
a
b
```

You can separate tests by adding blank lines.
```python
>>> obj = BigClass().fit(X)
>>> obj = BigClass().transform(Y)
[4, 5, 6]
>>> print("a\nb")
a
b
```
</details></li></ul></details>

[^1]: O. McNoleg, "The integration of GIS, remote sensing,
   expert systems and adaptive co-kriging for environmental habitat
   modelling of the Highland Haggis using object-oriented, fuzzy-logic
   and neural-network techniques," Computers & Geosciences, vol. 22,
   pp. 585-588, 1996.

[^2]: This is another footnote talking about footnotes. Very nice.

[^3]: Another one even, this is great actually. The system is not perfect yet but it will get there.
<h1 align="center" id="examples.module_with_functions">Module with functions</h1>
Docstring for the module `module_with_functions.py`.

This module as an example functions with some warnings and deprecations examples.
It is not much different than the other module but its put here for completeness and for adding content to the TOC.


<h2 id="examples.module_with_functions.better_function">better_function</h2>

```python
examples.module_with_functions.better_function(var1, var2, long_var_name=None, *args)
```



> **Warning** This function will replace the deprecated function in version 2.0.0.

> **Warning** This is another warning, warning the user that this function is blazingly fast!

This function is much better than the one that is deprecated.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`.<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>: array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array.  We can also refer to
variables like `var1`.</li><li><code>var2</code>: int<br>&emsp;The type above can either refer to an actual Python type
(e.g. ``int``), or describe the type of the variable in more
detail, e.g. ``(N,) ndarray`` or ``array_like``.</li><li><code>long_var_name</code>: {'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>*args</code>: iterable<br>&emsp;Other arguments.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code>var3</code>: int<br>&emsp;Returns `var3` which is of type ``int``.</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.
```python
>>> a = [1, 2, 3]
>>> b = better_function(a)
>>> print(b)
[10,11,12]
```
<h2 id="examples.module_with_functions.deprecated_function">deprecated_function</h2>

```python
examples.module_with_functions.deprecated_function(var1, var2, long_var_name=None, *args)
```



> **Warning** Deprecation Warning: `deprecated_function` will be removed in version 2.0.0, it is replaced by `better_function` because the new one is blazingly fast.

This function is deprecated.
Several sentences providing an extended description. Refer to
variables using back-ticks, e.g. `var`. 
Look at this really big equation that I took from [^4]

$$\left( \sum_{k=1}^n a_k b_k ight)^2 \leq \left( \sum_{k=1}^n a_k^2 ight) \left( \sum_{k=1}^n b_k^2 ight)$$<details closed><summary>&emsp;<b>Parameters</b></summary><p/><ul><li><code>var1</code>: array_like<br>&emsp;Array_like means all those objects -- lists, nested lists, etc. --
that can be converted to an array.  We can also refer to
variables like `var1`.</li><li><code>var2</code>: int<br>&emsp;The type above can either refer to an actual Python type
(e.g. ``int``), or describe the type of the variable in more
detail, e.g. ``(N,) ndarray`` or ``array_like``.</li><li><code>long_var_name</code>: {'hi', 'ho'}, optional<br>&emsp;Choices in brackets, default first when optional.</li><li><code>*args</code>: iterable<br>&emsp;Other arguments.</li></ul></details><details closed><summary>&emsp;<b>Returns</b></summary><p/><ul><li><code>var3</code>: int<br>&emsp;Returns `var3` which is of type ``int``.</li></ul></details>

These are written in doctest format, and should illustrate how to
use the function.
```python
>>> a = [1, 2, 3]
>>> b = deprecated_function(a)
>>> print(b)
[4,5,6]
```


[^4]: Trager, Scott. "The Earth's atmosphere: seeing, background, absorption & scattering" (PDF). S.C. Trager. Retrieved 31 May 2022
