import json
# json module is used to work with JSON data in Python. It allows you to parse JSON strings and convert them into Python objects, as well as serialize Python objects into JSON format.

import pickle 
# pickle is used for saving and loading the model.
from sklearn.feature_extraction.text import CountVectorizer
#count vectorizer used for bag of words.
from sklearn.linear_model import LogisticRegression

# Load dataset

with open('intents.json') as file:
    data = json.load(file)
# The entire json file is loaded into the variable 'data' object as a Python dictionary.
patterns = []
tags = []

# We are taking two empty lists, one for patterns and one for tags. We will fill these lists with the data from the json file.
for intent in data['intents']:
    for i in intent['patterns']:
        patterns.append(i.lower())
        tags.append(intent['tag'])

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
model = LogisticRegression()
model.fit(X, tags)

# Save model and vectorizer
pickle.dump(model, open('chatbot_model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("Model and vectorizer saved successfully.")





