import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Add the user's entry into the database --> DONE
        # getting data from database and storing it in variables (name, month and day)
        name, month, day = request.form.get("name"), request.form.get("month"), request.form.get("day")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?,?,?)", name, month, day)
        return redirect("/")
    else:
        # Display the entries in the database on index.html --> DONE
        people = db.execute("SELECT * from birthdays")
        return render_template("index.html", people=people)
