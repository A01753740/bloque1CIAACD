# Python Libraries
from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
# Files management
import os
from werkzeug.utils import secure_filename

# Load model
df = joblib.load('dt1.joblib')
# Create flask app
server = Flask(__name__)

# Define a route to send JSON data
@server.route('/predictjson', methods=['POST']) # Send data to the server

def predictjson():
    # Process the input data
    data = request.json
    print(data)
    inputData = np.array([
        data['pH'],
        data['sulphates'],
        data['alcohol']
    ])

    # Make a prediction
    result = df.predict([inputData.reshape(1, -1)])
    # Return the prediction
    return jsonify({'Prediction': str(result[0])})

if __name__ == '__main__':
    server.run(debug='False', host='0.0.0.0', port=8080)