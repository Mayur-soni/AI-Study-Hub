from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.http import HttpResponse

from aiapp import views

def intellectai_home(request):
    return HttpResponse("✅ IntellectAI backend is live!")

urlpatterns = [
    path('admin/', admin.site.urls),

    # Redirects
    path('IntellectAI/', lambda request: redirect('/')),

    # Static Pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Courses and Coding
    path('courses/', views.courses, name='courses'),
    path('coding/', views.coding, name='coding'),
    path('coding/blank/', views.blank_view, name='blank'),

    # Jobs
    path('jobs/', views.jobs_list, name='jobs_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),

    # Auth
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/logincheck/', views.verifyuser, name='logincheck'),
    path('signup/', views.show_signup_page, name='signup'),
    path('signupuser/', views.signupuser, name='signupuser'),
    path('insert/', views.user_signup, name='insert'),

    # API or additional routes
    path('api/', include('aiapp.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
