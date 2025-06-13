"""
URL configuration for ai_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views



from aiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),
    path('jobs/', views.jobs_list, name='jobs_list'),  # your main jobs listing page
    path('coding/', views.coding, name='coding'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('coding/blank/', views.blank_view, name='blank'),
    path('', include('aiapp.urls')),
    path("api/", include("aiapp.urls")),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('login/logincheck', views.verifyuser, name='logincheck'),
    path('logincheck',views.verifyuser),
    path('signup', views.show_signup_page, name='signup'),
    path('signupuser', views.signupuser),
    path('insert',views.user_signup),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
