import subprocess



from django.contrib import messages

from .models import Signup

# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from gpt4all import GPT4All
from rest_framework.response import Response

# Set your OpenAI API key




# model = GPT4All("C:/gpt4all/models/gpt4all-falcon.q4_0.bin")  # Change to your downloaded model
#
# def ai_chat(request):
#     if request.method == "POST":
#         user_input = request.POST.get("message", "")
#
#         if user_input:
#             response = model.generate(user_input)
#             return JsonResponse({"reply": response})
#
#     return JsonResponse({"reply": "Invalid request"})




@api_view(["POST"])
def run_python_code(request):
    code = request.data.get("code", "")

    try:
        # Run the Python code in a subprocess
        process = subprocess.run(
            ["python3", "-c", code], capture_output=True, text=True, timeout=5
        )
        output = process.stdout if process.stdout else process.stderr
    except Exception as e:
        output = str(e)

    return Response({"output": output})

def index(request):
    return render(request,'index.html')

def internship(request):
    return render(request,'internship.html')

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def login(request):
    return render(request,'login.html')

def verifyuser(request):
    uemail=request.POST.get('email')
    upassword=request.POST.get('pass')
    try:
        userdata=Signup.objects.get(EMAIL=uemail,PAS=upassword)

        request.session['login_id']=userdata.id
        request.session['login_email']=userdata.EMAIL
        request.session['login_name']=userdata.NAME

        request.session.save()
        messages.success(request,'Login Successful')
        return render(request,'index.html')
    except:
        messages.error(request,'Invail Email OR Password')
        return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def user_signup(request):
    uname=request.POST.get('name')
    uemail=request.POST.get('email')
    upas = request.POST.get('pass')

    if Signup.objects.filter(EMAIL=uemail).exists():
        messages.error(request,'Account already exists')
        return render(request,'signup.html')
    else:
        insertquery=Signup(NAME=uname,EMAIL=uemail,PAS=upas)
        insertquery.save()
        messages.success(request,'Registeration Successfull')
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['login_id']
        del request.session['login_email']
        messages.success(request,'Logout Successful')
    except:
        messages.error(request,'Error occured')
    return render(request,'index.html')