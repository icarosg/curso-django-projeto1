from django.urls import path
from . import views

# recipes:(nome)
app_name = 'recipes'

urlpatterns = [
    path('', views.my_view, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
