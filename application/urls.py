from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('similarity2/', views.similarity, name='similarity'),
    

#levenshtein_similarity
    #path('levenshtein/', views.calculate_similarity_view, name='calculate_leven'),
#saleh 
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    #tp1
    path('similarity_deg/', views.similarity_deg, name='similarity_deg'),
]
