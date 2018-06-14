from django.shortcuts import render
from blog.models import Article,ArticleCategory
from api import serializer
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('-id')
    article_serializer = serializer.ArticleSerilizer(articles,many=True)
    print(type(article_serializer.data))
    print(articles.count())

    return_dict = {
        "count" : articles.count(),
        "data" : article_serializer.data
    }

    return JsonResponse(return_dict,status = status.HTTP_200_OK)

def category_list(request):
    categories = ArticleCategory.objects.all()
    cat_serializer = serializer.CategorySerializer(categories,many=True)

    return JsonResponse(cat_serializer.data,safe = False,status= status.HTTP_200_OK)