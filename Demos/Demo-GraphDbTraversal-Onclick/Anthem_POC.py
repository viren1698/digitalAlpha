import json
import numpy as np
import random
import nltk
import math
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


def data_parsing():
    json_data = json.load(open('Anthem_data.json', 'r'))
    words = []
    for intent in json_data['intents']:
        for pattern in intent['patterns']:
            w = [word for word in nltk.word_tokenize(pattern.lower()) if word not in list(punctuation)+stopwords.words('english')]
            words.extend(w)
    # stem and lower each word and remove duplicates
    words = [stemmer.stem(w) for w in words]
    words = sorted(list(set(words)))
    return words


def clean_up_sentence(query):
    sentence_words = nltk.word_tokenize(query)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words if word not in list(punctuation)+stopwords.words('english')]
    return sentence_words


# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(query, words=data_parsing(), show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(query)
    # bag of words
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return bag


def classify(probability_score):
    if round(probability_score) > 0.5:
        return 'Benefits'
    else:
        return 'Claims'


def user_query_keywords(query):
    sentence_words = nltk.word_tokenize(query)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words if
                      word.lower() not in stopwords.words('english') + list(punctuation)]
    return sentence_words


def question_from_class(json_data, query, probability):
    class_name = classify(probability)
    # print(class_name)
    user_stemmed_keywords = user_query_keywords(query)
    maximum_match = 0
    list_of_json_question = []
    list_of_json_responses = []
    dictionary_of_json_question_response = {}
    dictionary_of_match = {}
    for intent in json_data['intents']:
        if intent['tag'] == class_name:
            for pattern in intent['patterns']:
                list_of_json_question.append(pattern)
            for responses in intent['responses']:
                list_of_json_responses.append(responses)
    for length in range(0, len(list_of_json_question)):
        dictionary_of_json_question_response[list_of_json_question[length]] = list_of_json_responses[length]
    # print(list_of_json_question)

    list_match_question = ""
    for question in list_of_json_question:
        no_of_matches = 0
        question_words = nltk.word_tokenize(question)
        question_words = [stemmer.stem(word.lower()) for word in question_words if
                          word.lower() not in stopwords.words('english') + list(punctuation) + list('i')]
        # print(question_words)
        for quest_words in question_words:

            if quest_words in user_stemmed_keywords:
                no_of_matches = no_of_matches + 1
        if maximum_match < no_of_matches:
            maximum_match = no_of_matches
            list_match_question = question
        dictionary_of_match[question] = no_of_matches
        # print(dictionary_of_match)
    return (dictionary_of_json_question_response[list_match_question])