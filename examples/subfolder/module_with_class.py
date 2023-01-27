"""Docstring for the module `module_with_class.py`.

Modules names should have short, all-lowercase names.  The module name may
have underscores if this improves readability.

Every module should have a docstring at the very top of the file.  The
module's docstring may extend over multiple lines.  If your docstring does
extend over multiple lines, the closing three quotation marks must be on
a line by itself, preferably preceded by a blank line.

"""


class BigClass:
    r"""Summarize the class in one line.

    Several sentences providing an extended description. Refer to
    variables using back-ticks, e.g. `var`. [1]_.

    Parameters
    ----------
    data : array_like
        Array_like means all those objects -- lists, nested lists, etc. --
        that can be converted to an array.  We can also refer to
        variables like `var1`.
    n_clusters : int
        The type above can either refer to an actual Python type
        (e.g. ``int``), or describe the type of the variable in more
        detail, e.g. ``(N,) ndarray`` or ``array_like``.
    *args : iterable
        Other arguments.
    long_var_name : {'hi', 'ho'}, optional
        Choices in brackets, default first when optional.

    Returns
    -------
    self : BigClass
        Returns self which is of type ``BigClass``.

    Other Parameters
    ----------------
    only_seldom_used_keyword : int, optional
        Infrequently used parameters can be described under this optional
        section to prevent cluttering the Parameters section.
    **kwargs : dict
        Other infrequently used keyword arguments. Note that all keyword
        arguments appearing after the first parameter specified under the
        Other Parameters section, should also be described under this
        section.

    Attributes
    ----------
    score : float
        Evaluation of the fit method ``BigClass``.
    slope : float
        Slope of the best-fit line according to OLS regression.

    Notes
    -----
    Notes about the implementation algorithm (if needed). Cite the relevant literature, e.g. [2]_.  You may also cite these
    references in the notes section above.

    This can have multiple paragraphs.

    You may include some math:

    $$X(e^{j\omega } ) = x(n)e^{ - j\omega n}$$

    And even use a Greek symbol like $\omega$ inline.

    References
    ----------
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    .. [2] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    .. [3] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.

    """

    def __init__(self):
        pass

    def _check_params(self, X):
        """Hidden functions as this should not be present in documentation"""
        self._check_params(X)

    def fit(self, X, y=None, sample_weight=None, *args):
        r"""Summarize the function in one line.

        Several sentences providing an extended description. Refer to
        variables using back-ticks, e.g. `var`.

        Parameters
        ----------
        X : array_like
            Array_like means all those objects -- lists, nested lists, etc. --
            that can be converted to an array.  We can also refer to
            variables like `var1`.
        y : int, optional
            The type above can either refer to an actual Python type
            (e.g. ``int``), or describe the type of the variable in more
            detail, e.g. ``(N,) ndarray`` or ``array_like``.
        sample_weight : array_like, optional
            The type above can either refer to an actual Python type
            (e.g. ``int``), or describe the type of the variable in more
            detail, e.g. ``(N,) ndarray`` or ``array_like``.
        *args : iterable
            Other arguments.

        Returns
        -------
        type
            Explanation of anonymous return value of type ``type``.
        describe : type
            Explanation of return value named `describe`.
        out : type
            Explanation of `out`.
        type_without_description

        Examples
        --------
        These are written in doctest format, and should illustrate how to
        use the function.

        >>> obj = BigClass().fit(X)
        >>> print(obj.attributes)
        [4, 5, 6]
        >>> print("a\nb")
        a
        b
        """

        return self

    def transform(self, X, *args):
        r"""Summarize the function in one line.

        Several sentences providing an extended description. Refer to
        variables using back-ticks, e.g. `var`.

        Parameters
        ----------
        X : array_like
            Array_like means all those objects -- lists, nested lists, etc. --
            that can be converted to an array.  We can also refer to
            variables like `var1`.
        *args : iterable
            Other arguments.

        Returns
        -------
        Y : numpy_array
            Numpy array with all the with the transformed values of the input

        Examples
        --------
        These are written in doctest format, and should illustrate how to
        use the function.

        >>> obj = BigClass().fit(X)
        >>> obj = BigClass().transform(Y)
        [4, 5, 6]
        >>> print("a\nb")
        a
        b

        You can separate tests by adding blank lines.

        >>> obj = BigClass().fit(X)
        >>> obj = BigClass().transform(Y)
        [4, 5, 6]
        >>> print("a\nb")
        a
        b
        """

        return self
