from django.shortcuts import render
from blog.models import Article
from api import serializer
from django.http import JsonResponse
from rest_framework import status
# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    article_serializer = serializer.ArticleSerilizer(articles,many=True)
    print(type(article_serializer.data))
    print(articles.count())

    return_dict = {
        "count" : articles.count(),
        "data" : article_serializer.data
    }

    return JsonResponse(return_dict,status = status.HTTP_200_OK)
