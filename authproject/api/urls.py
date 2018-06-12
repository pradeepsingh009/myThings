from django.urls import path,include
from api import views


urlpatterns = [
     path('articles/',views.article_list),
]