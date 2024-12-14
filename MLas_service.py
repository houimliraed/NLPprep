from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# Initialize the Flask app
app = Flask(__name__)

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        # Get input text from the form
        user_input = request.form['text_input']
        
        # Perform sentiment analysis
        sentiment_score = sia.polarity_scores(user_input)['compound']

        # Check if the sentiment is positive
        if sentiment_score > 0:
            result = "Positive"
        else:
            result = "Negative"

    return render_template('index.html', result=result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
