from django.urls import path,include
from api import views


urlpatterns = [
     path('articles/',views.article_list),
     path('categories/',views.category_list),
     path('article/<int:article_id>',views.article),
]