#!/usr/bin/env python3
"""
Flask web application with user login emulation and localization.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config:
    """
    Config class for Flask application.
    Configures available languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match between the supported languages and
    the language preferences sent by the user's browser.
    If a 'locale' query parameter is provided and valid, use it.

    Returns:
        str: The best matched language (either 'en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user() -> dict:
    """
    Retrieves the user based on the 'login_as' query parameter.

    Returns:
        dict: The user dictionary if the ID is valid, else None.
    """
    user_id = request.args.get('login_as', type=int)
    return users.get(user_id)

@app.before_request
def before_request() -> None:
    """
    Executes before each request. Sets the global user based on the 'login_as' query parameter.
    """
    g.user = get_user()

@app.route('/')
def index() -> str:
    """
    Handles the root route and returns the rendered index.html template.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)

