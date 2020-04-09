faculty-sphinx-theme
====================

``faculty-sphinx-theme`` is a `Sphinx <https://www.sphinx-doc.org/>`_ theme for
`Faculty <https://faculty.ai/>`_ projects. It's based on `the Read the Docs
theme <https://sphinx-rtd-theme.readthedocs.io/>`_, but with Faculty branding
and an optional navigation bar for use in the `Faculty platform docs
<https://docs.faculty.ai>`_.

Usage
-----

Install ``faculty-sphinx-theme`` and configure your Sphinx project to use the
theme. In your project's ``conf.py``, add ``faculty_sphinx_theme`` to the list
of enabled extensions:

.. code-block:: python

    extensions = [
        "faculty_sphinx_theme",
        # Plus any other extensions you are using
    ]

and modify the ``html_theme`` setting to:

.. code-block:: python

    html_theme = "faculty-sphinx-theme"

Theme options
+++++++++++++

To enable the Faculty platform docs navigation bar, set the ``navigation``
option to ``True``. The navigation bar will, by default, link to the actual
docs at `<https://docs.faculty.ai/>`_, but this can be overridden with the
``navigation_root`` setting.

Example entry in ``conf.py``:

.. code-block:: python

    html_theme_options = {
        "navigation": True,
        "navigation_root": "/my/local/directory",
    }
