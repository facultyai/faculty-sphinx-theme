faculty-sphinx-theme
====================

``faculty-sphinx-theme`` is a `Sphinx <https://www.sphinx-doc.org/>`_ theme for
`Faculty <https://faculty.ai/>`_ projects. It's based on `the Read the Docs
theme <https://sphinx-rtd-theme.readthedocs.io/>`_, but with Faculty branding
and an optional navigation bar for use in the `Faculty platform docs
<https://docs.faculty.ai>`_.

Installation
------------

.. code-block:: bash

    pip install faculty-sphinx-theme

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

The theme provides an optional extra navbar with custom links. To enable it,
use the ``navbar`` settings. You'll probably also want to set the
``navbar_root`` setting which defines the link on the "Faculty logo":

.. code-block:: python

    html_theme_options = {
        "navbar": True,
        "navbar_root": "https://docs.faculty.ai/",
    }

To add entries to the navbar, use the ``navbar_{0,1,2,3,4}_heading`` settings.
It's expected to be a string with the heading and linked URL separated by a
space, for example:

.. code-block:: python

    html_theme_options = {
        "navbar": True,
        "navbar_root": "https://docs.faculty.ai/",
        "navbar_0_heading": "Other https://other.faculty.ai/",
        "navbar_1_heading": "More https://more.faculty.ai/",
    }

You can also add menu items that appear under navbar entries with the
``navbar_{0,1,2,3,4}_content`` settings. They are in the same format as the
``_heading`` settings, with comma separation, for example:

.. code-block:: python

    html_theme_options = {
        "navbar": True,
        "navbar_root": "https://docs.faculty.ai/",
        "navbar_0_heading": "Other https://other.faculty.ai/",
        "navbar_0_content": "Sub 1 https://other.faculty.ai/one, Sub 2 https://other.faculty.ai/two",
        "navbar_1_heading": "More https://more.faculty.ai/",
    }
