from django.urls import path
from app1 import views
app_mame="app1"
urlpatterns = [
    path("",views.samp1, name="samp1")
]
