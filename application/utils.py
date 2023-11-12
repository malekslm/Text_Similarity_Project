# Fonction pour lire un fichier .txt et créer une liste de mots
def create_word_list(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    words_file = file_content.split()
    # words_file = [word.lower() for word in words_file]
    # stop_words = set(["le", "la", "les", "de", "à", "et"])
    # words_file = [word for word in words_file if word not in stop_words]
    return words_file

# Fonction pour compter les fréquences des mots et créer un dictionnaire
def count_word_frequencies(words):
    word_frequencies = {}
    for word in words:
        cleaned_word = word.strip('.,!?()[]{}"\'').lower()
        word_frequencies[cleaned_word] = word_frequencies.get(cleaned_word, 0) + 1
    return word_frequencies

import math
from operator import length_hint

# Fonction pour calculer le produit scalaire entre deux vecteurs
def dot_product(D1, D2):
    return sum(D1.get(word, 0) * D2.get(word, 0) for word in set(D1.keys()) & set(D2.keys()))

# Fonction pour calculer la norme euclidienne d'un vecteur
def vector_norm(D):
    return math.sqrt(sum(frequency ** 2 for frequency in D.values()))

import math

def sim(file_path1, file_path2):
    words_file1 = create_word_list(file_path1)
    words_file2 = create_word_list(file_path2)

    word_frequencies_file1 = count_word_frequencies(words_file1)
    word_frequencies_file2 = count_word_frequencies(words_file2)

    similarity = dot_product(word_frequencies_file1, word_frequencies_file2) / (
            vector_norm(word_frequencies_file1) * vector_norm(word_frequencies_file2))

    return similarity
