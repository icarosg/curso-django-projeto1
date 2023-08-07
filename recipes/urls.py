from django.urls import path
from recipes.views import contats, my_view, about


urlpatterns = [
    path('', my_view),
    path('contats/', contats),
    path('about/', about)
]
