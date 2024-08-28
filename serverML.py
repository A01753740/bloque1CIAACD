# Python Libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
from load import joblib
# Files management
import os
from werkzeug.utils import secure_filename

# Load model
df = joblib.load('dt1.joblib')
# Create flask app
server = Flask(__name__)

# Define a route to send JSON data
@server.route('/predictjson', methods=['POST']) # Send data to the server