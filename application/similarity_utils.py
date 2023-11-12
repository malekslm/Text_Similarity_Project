# similarity_utils.py

import math

# Fonction pour lire un fichier .txt et créer une liste de mots
def create_word_list(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    words_file = file_content.split()
    return words_file

# Fonction pour compter les fréquences des mots et créer un dictionnaire
def count_word_frequencies(words):
    word_frequencies = {}
    for word in words:
        cleaned_word = word.strip('.,!?()[]{}"\'').lower()
        word_frequencies[cleaned_word] = word_frequencies.get(cleaned_word, 0) + 1
    return word_frequencies

# Fonction pour calculer la similarité entre deux fichiers texte
def similarity_two_files(file1path, file2path):
    words_file1 = create_word_list(file1path)
    words_file2 = create_word_list(file2path)
    
    word_frequencies_file1 = count_word_frequencies(words_file1)
    word_frequencies_file2 = count_word_frequencies(words_file2)
    
    all_keys = set(word_frequencies_file1.keys()) | set(word_frequencies_file2.keys())
    dis = math.sqrt(sum([(word_frequencies_file1.get(key, 0) - word_frequencies_file2.get(key, 0)) ** 2 for key in all_keys]))
    dis = dis / (len(word_frequencies_file1) * len(word_frequencies_file2))
    
    return dis
