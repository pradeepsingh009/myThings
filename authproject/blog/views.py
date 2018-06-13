from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, ArticleCategory, ArticleCategoryJoin, Author
from django.core.paginator import Paginator
import sys
# Create your views here.


def listing(request):
    print(dir(request))

    print(request.method)
    print(request.get_host())
    print(request.get_port())
    print(request.session)
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 2)

    requestedPage = request.GET.get('page')
    articles = paginator.get_page(requestedPage)

    # fetching all the categories
    all_categories = ArticleCategory.objects.all()
    categories_dict = {}
    for category in all_categories:
        article_count = ArticleCategoryJoin.objects.filter(category=category).count()
        categories_dict[category.id] = {"category": category, "article_count": article_count}

    # fetching all the authors
    all_authors = Author.objects.all()
    authors_dict = {}
    for author in all_authors:
        article_count = author.article_set.all().count()        
        authors_dict[author.id] = {'author': author, "article_count": article_count}

    context = {
        'articles': articles,
        'categories_dict': categories_dict,
        'authors_dict': authors_dict,
    }
    return render(request, 'blog/listing.html', context)


def detail(request, blog_id):
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles, 2)

    # fetching all the categories
    all_categories = ArticleCategory.objects.all()
    categories_dict = {}
    for category in all_categories:
        article_count = ArticleCategoryJoin.objects.filter(category=category).count()
        categories_dict[category.id] = {
            "category": category, "article_count": article_count}

    # fetching all the authors
    all_authors = Author.objects.all()
    authors_dict = {}
    for author in all_authors:
        article_count = author.article_set.all().count()
        authors_dict[author.id] = {'author': author, "article_count": article_count}

    try:
        article = Article.objects.get(id=blog_id)

        context = {
            'article': article,
            'categories_dict': categories_dict,
            'authors_dict': authors_dict,
        }

        return render(request, 'blog/detail.html', context)
    except Article.DoesNotExist:
        return render(request, 'blog/article_not_found.html')
