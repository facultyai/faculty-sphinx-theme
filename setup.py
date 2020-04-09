from setuptools import setup
from pathlib import Path


README = Path(__file__).parent / "README.rst"


setup(
    name="faculty-sphinx-theme",
    description="A Sphinx theme for Faculty projects.",
    long_description=README.read_text(),
    author="Faculty",
    author_email="opensource@faculty.ai",
    license="Apache Software License",
    packages=["faculty_sphinx_theme"],
    use_scm_version={"version_scheme": "post-release"},
    setup_requires=["setuptools_scm"],
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
