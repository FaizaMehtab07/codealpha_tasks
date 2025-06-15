import json
import random

def load_intents(file_path='intents.json'):
    # Load intents data from a JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_intent_responses(intents_data, tag):
    # Retrieve responses for a specific intent tag
    for intent in intents_data['intents']:
        if intent['tag'] == tag:
            return intent['responses']
    return []

def get_all_intents(intents_data):
    # Get all intents with their tags and patterns
    return intents_data['intents']
