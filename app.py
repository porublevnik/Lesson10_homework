from utils import *
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_all():
    return f"<pre>\n{get_all()}\n</pre>"


@app.route("/candidates/<int:x>")
def page_candidate(x):
    return f"<pre>\n{get_by_pk(x)}\n"f"</pre>"


@app.route("/skills/<x>")
def page_skills(x):
    return f"<pre>\n{get_by_skill(x)}\n</pre>"


app.run()