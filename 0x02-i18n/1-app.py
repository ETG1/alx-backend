#!/usr/bin/env python3
"""
Flask web application with Babel integration for i18n/l10n.
"""

from flask import Flask, render_template
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

@app.route('/')
def index() -> str:
    """
    Handles the root route and returns the rendered index.html template.
    
    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True)

