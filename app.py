from flask import Flask, render_template, request, jsonify
import prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# API listening to POST requests and predicting sentiments
@app.route('/predict', methods=['POST'])
def predict():
    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status': 'error',
                    'message': 'Empty Review'}
    else:
        # Calling the predict method from prediction.py module
        sentiment, path = prediction.predict(review)
        response = {'status': 'success',
                    'message': 'Got it',
                    'sentiment': sentiment,
                    'path': path}

    return jsonify(response)

# Creating an API to save the review when the user clicks on the Save button
@app.route('/save', methods=['POST'])
def save():
    # Extracting date, product name, review, and sentiment associated from the JSON data
    date = request.json.get('date')
    product = request.json.get('product')
    review = request.json.get('review')
    sentiment = request.json.get('sentiment')

    # Creating a final variable separated by commas
    data_entry = f"{date},{product},{review},{sentiment}"

    # Open the file in 'append' mode
    # Log the data in the file

    # Return a success message
    return jsonify({'status': 'success',
                    'message': 'Data Logged'})

if __name__ == "__main__":
    app.run(debug=True)
