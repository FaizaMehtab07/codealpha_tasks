import nltk
import string
import random
from responses import load_intents, get_all_intents, get_intent_responses

# Downloading required NLTK data files
nltk.download('punkt')
nltk.download('punkt_tab')

def preprocess_text(text):
    # Tokenizing the input text into words
    tokens = nltk.word_tokenize(text)
    # Creating a translation table to remove punctuation
    table = str.maketrans('', '', string.punctuation)
    # Converting tokens to lowercase and remove punctuation
    cleaned_tokens = [token.lower().translate(table) for token in tokens if token.translate(table)]
    return cleaned_tokens

import math
from collections import Counter

def cosine_similarity(vec1, vec2):
    # Calculating cosine similarity between two frequency vectors
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([v**2 for v in vec1.values()])
    sum2 = sum([v**2 for v in vec2.values()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def bag_of_words(tokens):
    # Creating a frequency dictionary of tokens
    return Counter(tokens)

def match_intent(user_tokens, intents, threshold=0.5):
    # Matching user input tokens to an intent using cosine similarity
    user_vec = bag_of_words(user_tokens)
    best_match = None
    highest_similarity = 0.0

    for intent in intents:
        for pattern in intent['patterns']:
            pattern_tokens = preprocess_text(pattern)
            pattern_vec = bag_of_words(pattern_tokens)
            similarity = cosine_similarity(user_vec, pattern_vec)
            if similarity > highest_similarity and similarity >= threshold:
                highest_similarity = similarity
                best_match = intent['tag']

    return best_match

def chatbot():
    # This main chatbot loop to interact with user
    print("Chatbot: Hello! I am your friendly chatbot. Type 'exit' to quit.")
    intents_data = load_intents()
    intents = get_all_intents(intents_data)
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        user_tokens = preprocess_text(user_input)
        intent_tag = match_intent(user_tokens, intents)
        
        if intent_tag:
            responses = get_intent_responses(intents_data, intent_tag)
            print("Chatbot:", random.choice(responses))
        else:
            print("Chatbot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
