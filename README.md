# Table of Contents
- [Module](#module)
   - [Class Name](#module.class)
      - [Fit](#module.class.method)
   - [Function](#module.function)
   - [Different Function](#module.different_function)




<h1 id="module">Module</h1>
Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on

<h2 id="module.class">Class</h2>

```python
dbsampler.DBS(X=X,y=y,n_points=1000,n_epochs=5, distribution='uniform', metric='euclidean')
```
> **Note** Something here This is a pretty good note formatting
> This is the continutations

> **Warning** Deprecation Warning or some sort, will be destroyed or something etc.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.Here is a simple footnote[^1].
A footnote can also have multiple lines[^2].  
You can also use words, to fit your writing style more closely[^3].


[^1]: My reference.
[^2]: Every new line should be prefixed with 2 spaces.  
  This allows you to have a footnote with multiple lines.
[^3]:
    Named footnotes will still render with numbers instead of the text but allow easier identification and linking.  
    This footnote also has been made with a different syntax using 4 spaces for new lines.

$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$


<details closed>
  <summary>&emsp;<b>Parameters</b></summary>
  <p/>
  <ul>
    <li><code>X</code>: numpy array of shape (samples,features) with the points of every class.</li>
    <li><code>Y</code>: 1-dimensional numpy array with labels of each points. Array must be flattened.</li>
    <li><code>n_points</code>: This determines the number of points sampled from the decision boundary. More points equates for a denser sample but slows the algorithm. Default is 1000.</li>
    <li><code>n_epochs</code>: This determines the number of epochs to be used. It is an iterative algorithm but it is very fast to converge. Default is 5. Currently working on a proof for an upper bound on the number of necessary iterations. </li>
    <li><code>distribution</code>: Initial point distribution, it is also the distribution of the points in the decision boundary. Currently supports only _uniform_ (default).</li>
    <li><code>metric</code>: metric used to compute the nearest neighbours. Currently only supports euclidean.</li>
  </ul>
</details>

 
<details closed>
  <summary>&emsp;<b>Attributes</b></summary>
  <ul>
    <li><code>n_parameters</code>: This tell you the number of points, it should be something cool but I dont really rememeber</li>
    <li><code>n_parameters</code>: This tell you the number of points, it should be something cool but I dont really rememeber</li>
    <li><code>n_parameters</code>: This tell you the number of points, it should be something cool but I dont really rememeber</li>
  </ul>
</details>


&nbsp;&nbsp;&nbsp;**Methods:**
<details closed>
  <summary>&nbsp;&nbsp;&nbsp;<code>Fit_transform</code></summary>
  This tell you the number of points, it should be something cool but I dont really rememeber
 
```python
dbsampler.DBS(X=X,y=y,n_points=1000,n_epochs=5, distribution='uniform', metric='euclidean')
```

</details>

<details closed>
  <summary>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>n_parameters</code></summary>
  This tell you the number of points, it should be something cool but I dont really rememeber
 
```python
dbsampler.DBS(X=X,y=y,n_points=1000,n_epochs=5, distribution='uniform', metric='euclidean')
```

</details>



<h2 id="module.function">Function</h2>

```python
dbsampler.DBS(X=X,y=y,n_points=1000,n_epochs=5, distribution='uniform', metric='euclidean')
```
> **Note** Something here This is a pretty good note formatting
> This is the continutations

> **Warning** Deprecation Warning or some sort, will be destroyed or something etc.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$


<details closed>
  <summary>&emsp;<b>Parameters</b></summary>
  <p/>
  <ul>
    <li><code>X</code>: numpy array of shape (samples,features) with the points of every class.</li>
    <li><code>Y</code>: 1-dimensional numpy array with labels of each points. Array must be flattened.</li>
    <li><code>n_points</code>: This determines the number of points sampled from the decision boundary. More points equates for a denser sample but slows the algorithm. Default is 1000.</li>
    <li><code>n_epochs</code>: This determines the number of epochs to be used. It is an iterative algorithm but it is very fast to converge. Default is 5. Currently working on a proof for an upper bound on the number of necessary iterations. </li>
    <li><code>distribution</code>: Initial point distribution, it is also the distribution of the points in the decision boundary. Currently supports only _uniform_ (default).</li>
    <li><code>metric</code>: metric used to compute the nearest neighbours. Currently only supports euclidean.</li>
  </ul>
</details>

 
<details closed>
  <summary>&emsp;<b>Returns</b></summary>
  <ul>
    <li><cover>n_parameters</code>: numpy array (n_points, n_features) of points in the decision boundary.</li>
  </ul>
</details>


**Examples**
```python
import dbsampler
X = dbsampler.DBS(data)
print(X.mean())
```


<h2 id="module.different_function">Different Function</h2>

```python
dbsampler.DBS(X=X,y=y,n_points=1000,n_epochs=5, distribution='uniform', metric='euclidean')
```
> **Note** Something here This is a pretty good note formatting
> This is the continutations

> **Warning** Deprecation Warning or some sort, will be destroyed or something etc.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

$$\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$


<details closed>
  <summary>&emsp;<b>Parameters</b></summary>
  <p/>
  <ul>
    <li><code>X</code>: numpy array of shape (samples,features) with the points of every class.</li>
    <li><code>Y</code>: 1-dimensional numpy array with labels of each points. Array must be flattened.</li>
    <li><code>n_points</code>: This determines the number of points sampled from the decision boundary. More points equates for a denser sample but slows the algorithm. Default is 1000.</li>
    <li><code>n_epochs</code>: This determines the number of epochs to be used. It is an iterative algorithm but it is very fast to converge. Default is 5. Currently working on a proof for an upper bound on the number of necessary iterations. </li>
    <li><code>distribution</code>: Initial point distribution, it is also the distribution of the points in the decision boundary. Currently supports only _uniform_ (default).</li>
    <li><code>metric</code>: metric used to compute the nearest neighbours. Currently only supports euclidean.</li>
  </ul>
</details>

 
<details closed>
  <summary>&emsp;<b>Returns</b></summary>
  <p/>
  <ul>
    <li><code>cover</code>: numpy array (n_points, n_features) of points in the decision boundary.</li>
    
  </ul>
</details>


**Examples**
```python
import dbsampler
X = dbsampler.DBS(data)
print(X.mean())
```
