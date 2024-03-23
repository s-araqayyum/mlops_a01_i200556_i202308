from flask import Flask, request, jsonify
import joblib

# Loading trained model
pipeline = joblib.load("model/emotion_classifier.joblib")

# Initializing our Flask application
app = Flask(__name__)


# Defining a route for the predict function
@app.route('/predict', methods=['POST'])
def predict():
    # Get the text from the request's body
    data = request.get_json(force=True)
    text = data['text']

    # Predict the emotion of the text
    prediction = pipeline.predict([text])

    # Return the prediction
    return jsonify({'emotion': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
