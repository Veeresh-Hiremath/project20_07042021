from django.urls import path
from app2 import views
app_mame="app2"
urlpatterns = [
    path("",views.samp2,name="samp2")
]
