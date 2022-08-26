from django.shortcuts import render
from django.http import HttpResponse

delegates = [
    {
        'delegate': 'Flipside', 
        'blockchain': 'MakerDAO'
    }, 
     {
        'delegate': 'Flipside', 
        'blockchain': 'Optimism'
    }, 
    {
        'delegate': 'Flipside', 
        'blockchain': 'AAVE'
    }
]

# Create your views here.
def home(request):
    return render(request, 'values_quiz/home.html')

def results(request): 
    context = {
        'delegates': delegates
    }
    return render(request, 'values_quiz/results.html', context)
