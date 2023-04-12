"""Entry point for app."""
from flask import Flask, redirect, url_for

app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/', methods=['GET', 'POST'])
def main_page():
    """Root page."""
    return "Flask OK"


@app.route('/redirect', methods=['POST'])
def redirect_page():
    """Redirect page."""
    return redirect(url_for('main_page'))
