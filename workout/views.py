from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
import openai
import json
import smtplib

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return render(request, 'workout/index.html')

    else:
        prompt = "Imagine you are a personal fitness trainer. You are knowledgable and descriptive.\n\n"
        prompt += f"Client: I weigh {request.POST['weight']} pounds.\n" 
        if request.POST['frequency']:
            prompt += f"I will be exercising {request.POST['location']} {request.POST['frequency']} times a week."
        prompt += f"\nClient: My fitness goal is: {request.POST['goal']}\n"
        if request.POST['extra'] != 'No' and request.POST['extra'] != '':
            prompt += f"Client: Some important additional information is that {request.POST['extra']}\n"
        
        prompt += f"Client: Create a detailed, {request.POST['frequency']} day workout plan for me."

        print(prompt)

        openai.api_key = "sk-secret key"
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

@csrf_exempt
def email(request):
    data = json.loads(request.body)
    address = data.get("address", "")
    plan = data.get("plan", "")

    try:
        msg = f"From: Virtual Trainer\nTo: {address}\nSubject: Workout Plan\n\n{plan}"
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("max.karamurzin@gmail.com", "czfpuhghroxyhaow")
        server.sendmail("max.karamurzin@gmail.com", address, msg)
        server.quit()
    except:
        return JsonResponse({"msg": "An Error occurred"})
    
    return JsonResponse({"msg": "Success! Check spam"})