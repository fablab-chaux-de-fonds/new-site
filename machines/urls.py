from django.urls import path

from . import views

app_name = 'machines'

urlpatterns = [
    path('trainings/<int:pk>/show', views.training_show, name='trainings-show'),
    path('trainings/<int:pk>/validation/', views.trainingValidation.as_view(), name='training-validation'),
    path('machines/<int:pk>/show', views.training_show, name='machines-show'),
]