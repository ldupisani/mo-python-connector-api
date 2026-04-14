"""Minimal fake Meteomatics API for local development.

Serves canned responses for a small subset of endpoints so example scripts
and downstream code can run without credentials or network access.
"""
from flask import Flask, jsonify, Response

app = Flask(__name__)


@app.route("/user_stats_json", methods=["GET"])
def user_stats_json():
    return jsonify({
        "user statistics": {
            "requests total": {"used": 42, "hard limit": 10000},
            "requests since last UTC midnight": {"used": 7, "hard limit": 500},
            "requests since HH:00:00": {"used": 3, "hard limit": 100},
            "requests in the last 60 seconds": {"used": 1, "hard limit": 10},
            "requests in parallel": {"used": 1, "hard limit": 5},
        }
    })


@app.route("/find_station", methods=["GET", "POST"])
def find_station():
    csv = (
        "Station Category;Station Type;ID Hash;WMO ID;Alternative IDs;Name;"
        "Location Lat,Lon;Elevation;Start Date;End Date\n"
        "SYNOP;SYNOP;abc123;066700;;ZURICH / KLOTEN;47.4800,8.5360;432;"
        "1980-01-01T00:00:00Z;2100-01-01T00:00:00Z\n"
        "SYNOP;SYNOP;def456;066100;;GENEVA / COINTRIN;46.2470,6.1280;412;"
        "1980-01-01T00:00:00Z;2100-01-01T00:00:00Z\n"
    )
    return Response(csv, mimetype="text/csv")
