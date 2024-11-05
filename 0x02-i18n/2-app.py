#!/usr/bin/env python3
"""
Create a get_locale function with the babel.localeselector decorator
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    configures the class
    """

    DEBUG = True
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localselector
def get_locale() -> str:
    """
    returns best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    returns html homepage
    """


if __name__ == "__main__":
    app.run()
