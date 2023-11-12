from django.shortcuts import render
from .similarity_utils import similarity_two_files
from django.views.decorators.csrf import csrf_exempt

from sklearn.feature_extraction.text import TfidfVectorizer
import os
import math


#TP 2 destance 
@csrf_exempt
def similarity(request):
    if request.method == 'POST':
        # Vérifiez le jeton CSRF ici avant de traiter les données du formulaire
        # ...
        
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']
        
        # Enregistrez les fichiers sur le serveur (vous pouvez également stocker les fichiers dans un endroit temporaire)
        with open('file1.txt', 'wb+') as destination:
            for chunk in file1.chunks():
                destination.write(chunk)
        with open('file2.txt', 'wb+') as destination:
            for chunk in file2.chunks():
                destination.write(chunk)
        
        # Appelez votre fonction de similarité
        result = similarity_two_files('file1.txt', 'file2.txt')
        
        return render(request, 'result_dis.html', {'result': result})
    
    return render(request, 'index_dis.html')

   

def home(request):
    return render(request, 'home.html')

def calculate_cosine_similarity(vec1, vec2):
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(x**2 for x in vec1))
    magnitude2 = math.sqrt(sum(x**2 for x in vec2))

    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # Avoid division by zero

    cosine_similarity = dot_product / (magnitude1 * magnitude2)
    angle_in_radians = math.acos(cosine_similarity)
    angle_in_degrees = math.degrees(angle_in_radians)

    return cosine_similarity, angle_in_degrees

def calculate_euclidean_distance(vec1, vec2):
    euclidean_distance = math.sqrt(sum((x - y)**2 for x, y in zip(vec1, vec2)))

    # Normalize between 0 and 1
    normalized_distance = euclidean_distance /(len(vec1)* len(vec2))

    return normalized_distance

def calculate_tfidf_similarity(content1, content2):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([content1, content2])
    tfidf_similarity = (vectors * vectors.T).A[0, 1]
    
    return tfidf_similarity


def calculate_levenshtein_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i

    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Deletion
                dp[i][j - 1] + 1,  # Insertion
                dp[i - 1][j - 1] + cost,  # Substitution
            )
    
    return dp[len1][len2] / (len1*len2)


def index(request):
    similarity_cosine = None
    angle_in_degrees = None
    similarity_euclidean = None
    similarity_tfidf = None
    levenshtein = None
    if request.method == 'POST':
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']

        # Read content from the uploaded files
        content1 = file1.read().decode('utf-8')
        content2 = file2.read().decode('utf-8')

        # Tokenize the content (split into words)
        words1 = content1.split()
        words2 = content2.split()

        # Create vectors for each file based on word frequency
        vector1 = [words1.count(word) for word in set(words1 + words2)]
        vector2 = [words2.count(word) for word in set(words1 + words2)]

        # Compute cosine similarity and angle in degrees
        similarity_cosine, angle_in_degrees = calculate_cosine_similarity(vector1, vector2)

        # Compute Euclidean distance and normalize
        similarity_euclidean = calculate_euclidean_distance(vector1, vector2)

        # Compute TF-IDF similarity
        similarity_tfidf = calculate_tfidf_similarity(content1, content2)

        levenshtein = calculate_levenshtein_distance(content1, content1)
        print (levenshtein)
    return render(request, 'index2.html', {'similarity_cosine': similarity_cosine, 'angle_in_degrees': angle_in_degrees, 'similarity_euclidean': similarity_euclidean, 'similarity_tfidf': similarity_tfidf, 'levenshtein': levenshtein })



def about(request):
    return render(request, 'about.html')


#tp 1 
from .utils import sim
def similarity_deg(request):
    if request.method == 'POST':
        file1 = request.FILES['file1']
        file2 = request.FILES['file2']

        with open('file1.txt', 'wb+') as destination:
            for chunk in file1.chunks():
                destination.write(chunk)
        with open('file2.txt', 'wb+') as destination:
            for chunk in file2.chunks():
                destination.write(chunk)

        similarity_result = sim('file1.txt', 'file2.txt')
        print(similarity_result)
        return render(request, 'result_deg.html', {'result': similarity_result})

    return render(request, 'index_deg.html')



