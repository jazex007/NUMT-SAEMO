"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "something_secure"
import NUMT_SAEMO.views
