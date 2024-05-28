#!/usr/bin/env python3
""" The basic flask app """

from flask import Flask, josnify


@app.route("/", methods=["GET"])
def home():
    return josnify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
