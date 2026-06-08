import json
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt_tab', quiet=True)

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

with open('intents.json', 'r') as f:
    intents_data = json.load(f)

def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t.isalpha() and t not in stop_words]
    return tokens

def get_response(user_input):
    user_tokens = set(preprocess(user_input))
    best_match = None
    best_score = 0
    for intent in intents_data['intents']:
        if intent['tag'] == 'unknown':
            continue
        for pattern in intent['patterns']:
            pattern_tokens = set(preprocess(pattern))
            if not pattern_tokens:
                continue
            intersection = user_tokens & pattern_tokens
            union = user_tokens | pattern_tokens
            score = len(intersection) / len(union) if union else 0
            if score > best_score:
                best_score = score
                best_match = intent
    if best_score < 0.2 or best_match is None:
        for intent in intents_data['intents']:
            if intent['tag'] == 'unknown':
                return random.choice(intent['responses'])
    return random.choice(best_match['responses'])
