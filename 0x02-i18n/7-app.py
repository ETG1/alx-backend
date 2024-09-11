#!/usr/bin/env python3
"""
Flask web application with user login emulation and localization.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz.exceptions import UnknownTimeZoneError

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
    the locale preferences in the following order:
    1. Locale from URL parameters.
    2. Locale from user settings.
    3. Locale from request headers.
    4. Default locale.

    Returns:
        str: The best matched language (either 'en' or 'fr').
    """
    # 1. Check locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # 2. Check locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Check locale from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@babel.timezoneselector
def get_timezone() -> str:
    """
    Determines the best match for the timezone preferences in the following order:
    1. Timezone from URL parameters.
    2. Timezone from user settings.
    3. Default to UTC.

    Returns:
        str: The best matched timezone.
    """
    # 1. Check timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass  # Invalid timezone, fall through to next option

    # 2. Check timezone from user settings
    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except UnknownTimeZoneError:
            pass  # Invalid timezone, fall through to default

    # 3. Default to UTC
    return app.config['BABEL_DEFAULT_TIMEZONE']

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
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run(debug=True)

