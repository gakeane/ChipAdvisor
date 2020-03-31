
"""

Flask uses the jinja2 template engine which allows us to write code inside a template.
this code will be parsed by the jinja template engine.
"""


# This imports from __init__.py
from source import app
from source import routes


if __name__ == "__main__":
    app.run(debug=True)
