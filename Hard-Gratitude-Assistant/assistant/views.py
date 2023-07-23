from django.shortcuts import render
from .assistant_logic import get_response
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def query(request):
    now = datetime.now()
    if now.hour < 12:
        greeting = "Good morning"
    elif now.hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    if request.method == 'POST':
        query = request.POST.get('input_text', '')
        response = get_response(query)
        response = response.replace('\n', '<br>')
        return HttpResponse(response, content_type="text/html")
    else:
        context = {
            'greeting': greeting
        }
        return render(request, 'query.html', context)
    
def assistant(request):

    if request.method == 'POST':
        query = request.POST.get('input_text', '')
        response = get_response(query)
        response = response.replace('\n', '<br>')
        return HttpResponse(response, content_type="text/html")
    else:
        context = {
            
        }
        return render(request, 'assistant.html', context)
    