from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.home, name = 'home'),
    # path('1250', views.q_1250, name = 'kiloman'), 
    # path('1401', views.q_1401, name = 'Gerando Permutações'),
    path("Home/<int:question_id>/", views.questoes),
]
