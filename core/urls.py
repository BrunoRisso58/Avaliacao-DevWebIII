from django.urls import path
from . import views

# URLConf
urlpatterns = [
	path('', views.presenceForm),
    path('listar', views.presentStudents)
]