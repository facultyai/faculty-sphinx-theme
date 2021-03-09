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
use the ``faculty_navbar`` settings. You'll probably also want to set the
``faculty_navbar_root`` setting which defines the link on the "Faculty logo":

.. code-block:: python

    html_theme_options = {
        "faculty_navbar": True,
        "faculty_navbar_root": "https://docs.faculty.ai/",
    }

To add entries to the navbar, add sections to the ``faculty_navbar_content``
setting:

.. code-block:: python

    html_theme_options = {
        "faculty_navbar": True,
        "faculty_navbar_root": "https://docs.faculty.ai/",
        "faculty_navbar_content": [
            {"title": "Section 1", "url": "https://sectionone.com/"},
            {"title": "Section 2", "url": "https://sectiontwo.com/"},
        ]
    }

You can also add menu items that appear on hover below the section headings.
To add these, use the ``entries`` key on a section:

.. code-block:: python

    html_theme_options = {
        "faculty_navbar": True,
        "faculty_navbar_root": "https://docs.faculty.ai/",
        "faculty_navbar_content": [
            {
                "title": "Section 1",
                "url": "https://sectionone.com/",
                "entries": [
                    {
                        "title": "Section 1.1",
                        "url": "https://sectionone.com/one",
                    },
                    {
                        "title": "Section 1.2",
                        "url": "https://sectionone.com/one",
                    },
                ]
            },
            {"title": "Section 2", "url": "https://sectiontwo.com/"},
        ]
    }

It's also possible to mark sections and entries as ``external``, meaning they
will open in a separate tab, or to omit the URL entirely for e.g. section
headings:

.. code-block:: python

    html_theme_options = {
        "faculty_navbar": True,
        "faculty_navbar_root": "https://docs.faculty.ai/",
        "faculty_navbar_content": [
            {
                "title": "No URL",
                "entries": [
                    {
                        "title": "External link",
                        "url": "https://external.com/",
                        "external": True
                    },
                ]
            },
            {"title": "Section 2", "url": "https://sectiontwo.com/"},
        ]
    }
