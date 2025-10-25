from django.shortcuts import render
from .models import LearningJourney, AboutMe, Reflection

def index(request):
    journeys = LearningJourney.objects.all()
    reflections = Reflection.objects.all()
    return render(request, 'index.html', {'journeys': journeys, 'reflections': reflections})

def about_me(request):
    about = AboutMe.objects.first()
    hobbies_list = []
    if about and about.hobbies:
        hobbies_list = [h.strip() for h in about.hobbies.split(",")]
    return render(request, 'aboutMe.html', {'about': about, 'hobbies_list': hobbies_list})