#!/usr/bin/env python3
"""
Flask web application that serves a single route at '/'.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    Handles the root route and returns the rendered index.html template.
    
    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)

