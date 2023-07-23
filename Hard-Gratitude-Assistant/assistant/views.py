from django.shortcuts import render
from .assistant_logic import get_response
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
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
    