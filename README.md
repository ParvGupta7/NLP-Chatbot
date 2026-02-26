Simple Intent-Based Chatbot
A Python-based conversational AI that uses Machine Learning to categorize user queries and provide relevant responses. This project demonstrates a complete NLP pipeline: from data preprocessing and vectorization to model training and deployment.

Overview
This chatbot uses a Bag-of-Words approach combined with Logistic Regression to understand user "intents." It reads from a structured JSON file, learns patterns, and saves the trained brain as a serialized file for fast inference.

Key Features
NLP Pipeline: Uses CountVectorizer for text-to-numerical conversion.

Fast Classification: Powered by scikit-learn Logistic Regression.

Model Persistence: Saves training states using pickle so you don't have to retrain every time.

Customizable: Simply edit intents.json to teach the bot new skills.
