# Import required modules
import flask
import pickle
from flask import Flask, request

# Create an instance of Flask and declare variables for our model
application = Flask(__name__)
modelname = 'ML_Model.pkl'
vecname = 'Vector.pkl'

# Homepage, render input prompt HTML
@application.route('/')
def index():
    return flask.render_template('index.html')
    
# Result page, get prediction result and render
@application.route('/words', methods=['POST'])
# Handle request
def form():
    # Document content was sent with POST request
    if request.method == 'POST':
        # Preparation
        data = request.form['content']
        model = pickle.load(open(modelname, 'rb'))
        vec = pickle.load(open(vecname, 'rb'))
        # Get result
        result = getresult(model, vec, data)[0]
        return flask.render_template('result.html', result=result)

# Get prediction
def getresult(model, vec, data):
    transformed_data = vec.transform([data])
    return model.predict(transformed_data)
if __name__ == "__main__":
    application.run()
