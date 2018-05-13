from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator
# Create your views here.

def listing(request):
    all_articles = Article.objects.all()
    paginator = Paginator(all_articles,2)

    requestedPage = request.GET.get('page')
    articles = paginator.get_page(requestedPage)
    context = {
        'articles' : articles
    }
    return render(request,'blog/listing.html',context)