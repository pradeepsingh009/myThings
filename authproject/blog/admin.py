from django.contrib import admin
from blog.models import User,Author,ArticleCategoryJoin,ArticleCategory,Article

models = [User,Author,ArticleCategoryJoin,ArticleCategory,Article]

admin.site.register(models)

