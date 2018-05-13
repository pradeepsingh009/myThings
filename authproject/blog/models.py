from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 20,blank = False)
    last_name = models.CharField(max_length = 20,blank = False)
    email = models.EmailField(max_length = 100,blank = False)
    password = models.CharField(max_length = 20,blank= False)    #add validator
    age = models.IntegerField(blank=True)     #add validator

    def __str__(self):
        return self.first_name+ " " + self.last_name

class Author(User):
    is_author = models.BooleanField()
    writing_skills = models.TextField(blank=True)
    mobile = models.CharField(max_length = 15,blank=True)      #add validator

    def __str__(self):
        return "(Author) " + self.first_name + " " + self.last_name

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 20,blank = False)
    description = models.TextField(blank=True)
    image  = models.ImageField(upload_to="blog/category/",blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(blank=False)
    long_description = models.TextField(blank=False)

    publish_date = models.DateTimeField(blank = True,null = True)
    expriry_date = models.DateTimeField(blank = True,null = True)
    image = models.ImageField(upload_to = "blog/article/",blank = True)

    date_created  = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    #many to one relationship with author
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    #many to many relationship with articlecategory
    article_category = models.ManyToManyField(ArticleCategory,through='ArticleCategoryJoin')

    class Meta():
        ordering = ['-date_modified']

    def __str__(self):
        return "(" +  str(self.id) + ") " +self.title

class ArticleCategoryJoin(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    category = models.ForeignKey(ArticleCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title[:30] + " - " + self.category.name





