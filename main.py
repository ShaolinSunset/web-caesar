from flask import Flask
import cgi
import os
import jinja2

template

app = Flask(__name__)
app.config["DEBUG"] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                backgroud-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width:540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
        <form action="text" method = "POST">
            <label for="">LABEL NAME:</label>
            <input id="" type="text" name="rot"/>
            <textarea id="" type="text" name="text"/>
            <input type="submit" />
        </form>
    </body>
</html>"""


@app.route("/")
def index():
    return "Hello World"

app.run()