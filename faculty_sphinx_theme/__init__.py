import os


def setup(app):
    app.add_html_theme(
        "faculty-sphinx-theme", os.path.abspath(os.path.dirname(__file__))
    )
