from django.shortcuts import render
from .assistant_logic import get_response
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def assistant(request):
    query = ""
    response = ""
    if request.method == 'POST':
        query = request.POST.get('input_text', '')
        prompt = f'''
        generate thoughtful, compassionate, and personalized responses that express gratitude based on the user's input. Generate an appropriate gratitude response.

        Input: Prompts provided by the user. These prompts could range from simple thank you messages to more complex expressions of gratitude and could be in response to a variety of situations.

        Your Response: Textual responses that effectively express gratitude. These responses should be contextually accurate, convey genuine gratitude, and be personalized to the user's input.

        some examples of user input : 
        1. I'm really grateful to my friends for throwing me a surprise birthday party.
        2. Thank you for helping me with the project. I couldn't have done it without you.
        3. My coworkers surprised me with a farewell party. I feel so loved and appreciated.
        and etc.

        i want you to give the response with thoughtful, compassionate, personalized gratitude
        do not mention in the response by confirming sure...
        generate a response directly without double quote

        And your name is Semicolon Assistant, do not label your name

        User Input : {query}
        '''
        response = get_response(prompt)
        response = response.replace('\n', '<br>')
        response = response.replace('Response: ', '')
        return HttpResponse(response, content_type="text/html")
    else:
        context = {
            'query' : query,
            'response' : response
        }
        return render(request, 'assistant.html', context)
    