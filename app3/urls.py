from django.urls import path
from app3 import views
app_mame="app3"
urlpatterns = [
    path("<data>/",views.index, name="data")
]
