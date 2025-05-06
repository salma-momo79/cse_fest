from django.shortcuts import render

def cgpa_improvement_plan(request):
    return render(request, 'planner/index.html')


from django.conf import settings
import requests

def fetch_movies():
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={settings.TMDB_API_KEY}&with_genres=18&sort_by=popularity.desc'
    response = requests.get(url)
    data = response.json()
    return data.get('results', [])


