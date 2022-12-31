from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
import openai

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'workout/index.html')

    else:
        prompt = "Imagine you are a personal fitness trainer. You are knowledgable and descriptive.\n\n"
        prompt += f"Client: I weigh {request.POST['weight']}" 
        if request.POST['location']:
            prompt += f" pounds and I will be exercising {request.POST['location']} {request.POST['frequency']} times a week."
        prompt += f"\nClient: My goal is {request.POST['goal']}\n"
        if request.POST['extra'] != '':
            prompt += f"Client: Some important additional information is that {request.POST['extra']}\n"
        
        prompt += f"Client: Create a detailed workout plan for me."

        print(prompt)

        openai.api_key = "SECRET_KEY"
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

        print(response.choices[0].text)
        return render(request, 'workout/result.html', {
            'plan': response.choices[0].text
        })