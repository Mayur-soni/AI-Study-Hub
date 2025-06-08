from django.urls import path

from . import views
from .views import  (run_python_code)
# ,ai_chat)

urlpatterns = [
    # path('',views.index),
    # path("api/ai-chat/", ai_chat, name="ai_chat"),
    path("run-python/", run_python_code),
]
