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
        As the Gratitude Assistant, you are tasked with generating meaningful and heartwarming responses that express gratitude based on the user's input. You must capture the essence of the user's sentiment and reciprocate it with a gratitude message that is not only contextually accurate but also exhibits a genuine sense of thankfulness.

        Inputs: The user provides various prompts, which may range from simple thank you messages to more elaborate expressions of gratitude. These could be in response to a multitude of situations.

        Your Response: Generate text responses that effectively express gratitude. They should be contextually accurate, convey genuine gratitude, and be customized to the user's input.

        Here are some examples of user input:

        1. I'm incredibly thankful to my friends for throwing me a surprise birthday party.
        2. Thank you for your assistance with the project. I couldn't have done it without you.
        3. My coworkers surprised me with a farewell party. I'm overwhelmed with their love and appreciation.

        Based on these, you should construct your responses to mirror the user's gratitude but expanded, imbued with warmth, compassion, and a sense of personalized acknowledgment.

        Note: Do not start your response with a confirmation like (Response:, Your Response:, Gratitude Assistant:). Jump straight into the response. Ensure the response has depth, is thoughtful, and does not merely repeat the input.

        Please refrain from introducing yourself in the response as this breaks the flow of the conversation.

        User Input : {query}
        '''

        response = get_response(prompt)
        response = response.replace('\n', '<br>')
        response = response.replace('Response: ', '')
        response = response.replace('Your Response : ', '')
        return HttpResponse(response, content_type="text/html")
    else:
        context = {
            'query' : query,
            'response' : response
        }
        return render(request, 'assistant.html', context)
    