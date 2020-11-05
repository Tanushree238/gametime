from app import app
# import functools
# import json
# import os

# import flask

# from authlib.client import OAuth2Session
# import google.oauth2.credentials
# import googleapiclient.discovery

# import googleauth

# app = flask.Flask(__name__)
# app.secret_key = "sdbvhwblvibewu2781ue8u12bdhw"

# app.register_blueprint(googleauth.app)

# @app.route('/')
# def index():
#     if googleauth.is_logged_in():
#         user_info = googleauth.get_user_info()
#         return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

#     return 'You are not currently logged in.'