from setuptools import setup

setup(
    name="faculty-sphinx-theme",
    packages=["faculty_sphinx_theme"],
    install_requires=["sphinx_rtd_theme"],
    package_data={
        "faculty_sphinx_theme": [
            "theme.conf",
            "*.html",
            "static/css/*.css",
            "static/images/*.svg",
            "static/images/*.ico",
        ]
    },
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "sphinx.html_themes": ["faculty-sphinx-theme = faculty_sphinx_theme"]
    },
)
