# Copyright 2020-2021 Faculty Science Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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
    install_requires=["sphinx-rtd-theme==0.4.3"],
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
        "sphinx.html_themes": ["faculty-sphinx-theme = faculty_sphinx_theme"],
    },
)
