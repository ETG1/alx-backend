#!/usr/bin/env python3
"""
Flask web application with Babel integration for i18n/l10n.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

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

@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match between the supported languages and
    the language preferences sent by the user's browser.
    If a 'locale' query parameter is provided and valid, use it.

    Returns:
        str: The best matched language (either 'en' or 'fr').
    """
    # Check if 'locale' is provided in the request and if it is supported
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Fallback to the best match based on the browser's language preferences
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Handles the root route and returns the rendered index.html template.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template(4-'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

