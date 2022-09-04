from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import findDelegate

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
    submitted = False
    if request.method == "POST": 
        form = findDelegate(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('results/')
    
    form = findDelegate
    return render(request, 'values_quiz/home.html', {'form':form})

def results(request): 
    context = {
        'delegates': delegates
    }
    return render(request, 'values_quiz/results.html', context)
