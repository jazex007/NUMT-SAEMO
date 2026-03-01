"""
Routes and views for the flask application.
"""

from datetime import datetime
import json
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import Flask, jsonify
from NUMT_SAEMO import SCHEDULE_SERVER
from NUMT_SAEMO.verify_user import verify
from .verify_user import verify
from flask import request, session

from NUMT_SAEMO import app






@app.route('/')
@app.route('/SAEMO')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='DOMOV',
        year=datetime.now().year,
    )



@app.route('/NÚMT')
def NÚMT():
    """Renders the home page."""
    return render_template(
        'NÚMT.html',
        title='NÚMT',
        year=datetime.now().year,
    )

@app.route('/NÚMT/Vyhľadávanie', methods=["GET", "POST"])
def NÚMT_search():
    if request.method == "POST":
        subject = request.form.get("subject")
        session["subject"] = subject  

    return render_template(
        'NÚMT_search.html',
        title='NÚMT-Vyhľadávanie',
        year=datetime.now().year,
        subject=session.get("subject")
    )
@app.route('/NÚMT/Popis')

def RESULT_description():
     

    return render_template(
        'NÚMT_result.html',
        title='NÚMT-Vyhľadávanie',
        year=datetime.now().year,
        subject=session.get("subject"),
        searchtype = "ZOBRAZUJE SA POPIS"
      )
@app.route('/NÚMT/Vlastnosti')

def RESULT_parameters():
     

    return render_template(
        'NÚMT_result.html',
        title='NÚMT-Vyhľadávanie',
        year=datetime.now().year,
        subject=session.get("subject"),
        searchtype = "ZOBRAZUJÚ SA VLASTNOSTI"
      )
@app.route('/NÚMT/Merania')

def RESULT_measurements():
     

    return render_template(
        'NÚMT_result.html',
        title='NÚMT-Vyhľadávanie',
        year=datetime.now().year,
        subject=session.get("subject"),
        searchtype = "ZOBRAZUJÚ SA MERANIA"
      )



@app.route("/api/data", methods=["POST"])
def api_data():
    data = request.get_json()
    schedule = SCHEDULE_SERVER.get_schedule_table(data["clientID"])
    return jsonify({"schedule": schedule})

@app.route("/user_verification", methods=["GET", "POST"])
def verification():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        is_valid = verify(username, password)

        if is_valid:
            return redirect(url_for("home"))
        else:
            return render_template(
                "user_verification.html",
                title="OVERENIE POUŽÍVATEĽA",
                error="Nesprávne prihlasovacie údaje"
            )

    return render_template(
        "user_verification.html",
        title="OVERENIE POUŽÍVATEĽA"
    )

    
    

