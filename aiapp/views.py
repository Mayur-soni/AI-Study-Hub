import subprocess



from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import never_cache
from openai.resources.fine_tuning.jobs import jobs

from .models import Signup
from .jobs import jobs  # ✅ This imports the list inside the module


# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
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

@never_cache
def index(request):
    return render(request,'index.html')

def courses(request):
    return render(request,'courses.html')

def job(request):
    return render(request,'job.html')

def job_detail(request, job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job is None:
        return HttpResponseNotFound("Job not found")
    return render(request, 'job_detail.html', {'job': job})

def jobs_list(request):
    # jobs = [  # <-- Paste your job data here
    #     {
    #         'id': 1,
    #         'title': 'AI Engineer',
    #         'company': 'OpenAI',
    #         'location': 'San Francisco, CA',
    #         'description': 'Exciting role in AI research and product development.',
    #         'requirements': ['Python', 'Machine Learning', 'Deep Learning'],
    #         'application_link': 'https://openai.com/apply'
    #     },
    #     {
    #         'id': 2,
    #         'title': 'Data Scientist',
    #         'company': 'Google',
    #         'location': 'Mountain View, CA',
    #         'description': 'Work with big data to generate insights and build ML models.',
    #         'requirements': ['Python', 'SQL', 'TensorFlow', 'Statistics'],
    #         'application_link': 'https://careers.google.com/jobs'
    #     },
    #     {
    #         'id': 3,
    #         'title': 'Machine Learning Engineer',
    #         'company': 'Meta (Facebook)',
    #         'location': 'Menlo Park, CA',
    #         'description': 'Develop and optimize ML models for large-scale systems.',
    #         'requirements': ['PyTorch', 'C++', 'Distributed Systems'],
    #         'application_link': 'https://www.metacareers.com/'
    #     },
    #     {
    #         'id': 4,
    #         'title': 'Data Analyst',
    #         'company': 'Netflix',
    #         'location': 'Los Gatos, CA',
    #         'description': 'Analyze user data to guide content decisions.',
    #         'requirements': ['SQL', 'Tableau', 'Python', 'Business Intelligence'],
    #         'application_link': 'https://jobs.netflix.com'
    #     },
    #     {
    #         'id': 5,
    #         'title': 'NLP Researcher',
    #         'company': 'Anthropic',
    #         'location': 'Remote',
    #         'description': 'Conduct cutting-edge research in NLP and language models.',
    #         'requirements': ['NLP', 'Transformers', 'Python', 'Research Experience'],
    #         'application_link': 'https://www.anthropic.com/careers'
    #     },
    #     {
    #         'id': 6,
    #         'title': 'AI Product Manager',
    #         'company': 'Microsoft',
    #         'location': 'Redmond, WA',
    #         'description': 'Bridge technical and business teams to deliver AI products.',
    #         'requirements': ['Product Management', 'AI/ML Knowledge', 'Agile'],
    #         'application_link': 'https://careers.microsoft.com'
    #     },
    #     {
    #         'id': 7,
    #         'title': 'Computer Vision Engineer',
    #         'company': 'Tesla',
    #         'location': 'Palo Alto, CA',
    #         'description': 'Build vision systems for autonomous vehicles.',
    #         'requirements': ['OpenCV', 'Computer Vision', 'Python', 'C++'],
    #         'application_link': 'https://www.tesla.com/careers'
    #     },
    #     {
    #         'id': 8,
    #         'title': 'AI Research Intern',
    #         'company': 'DeepMind',
    #         'location': 'London, UK',
    #         'description': 'Join world-class researchers in solving AI problems.',
    #         'requirements': ['PhD/MSc in AI-related field', 'Python', 'Research Papers'],
    #         'application_link': 'https://www.deepmind.com/careers'
    #     }
    # ]
    return render(request, 'job.html', {'jobs': jobs})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blank_view(request):
    return render(request,'coding/blank.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # or wherever you want
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def verifyuser(request):
    if request.method == 'POST':
        uemail = request.POST.get('EMAIL')
        upassword = request.POST.get('PAS')

        try:
            userdata = Signup.objects.get(EMAIL=uemail)
            if check_password(upassword, userdata.PAS):
                request.session['login_id'] = userdata.id
                request.session['login_email'] = userdata.EMAIL
                request.session['login_name'] = userdata.NAME
                request.session['login_role'] = userdata.ROLE
                messages.success(request, 'Login Successful')
                return render(request, 'index.html', {"username": uemail})
            else:
                messages.error(request, 'Invalid Password')
        except Signup.DoesNotExist:
            messages.error(request, 'Email not registered')

    return render(request, 'login.html')

def show_signup_page(request):   # ✅ Renamed to avoid conflict
    return render(request, 'signup.html')

def user_signup(request):
    if request.method == 'POST':
        uname = request.POST.get('NAME')
        uemail = request.POST.get('EMAIL')
        upas = request.POST.get('PAS')

        if Signup.objects.filter(EMAIL=uemail).exists():
            messages.error(request, 'Account already exists')
            return render(request, 'signup.html')
        else:
            from django.contrib.auth.hashers import make_password
            Signup.objects.create(NAME=uname, EMAIL=uemail, PAS=make_password(upas))
            messages.success(request, 'Registration Successful')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['login_id']
        del request.session['login_email']
    except KeyError:
        pass
    return redirect('index')

def signupuser(request):
    if request.method == 'POST':
        uname = request.POST.get('NAME')
        uemail = request.POST.get('EMAIL')
        upas = make_password(request.POST.get('PAS'))  # hash here!

        if Signup.objects.filter(EMAIL=uemail).exists():
            messages.error(request, 'Account already exists')
            return render(request, 'signup.html')

        Signup(NAME=uname, EMAIL=uemail, PAS=upas).save()
        messages.success(request, 'Registration Successful')
        return render(request, 'login.html')


def coding(request):
    if not request.session.get('login_id'):
        return redirect('login')  # Redirect to login if not logged in
    return render(request, 'coding.html')


