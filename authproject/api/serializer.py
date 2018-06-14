from blog.models import Article,ArticleCategory
from rest_framework import serializers

class ArticleSerilizer(serializers.ModelSerializer):

    unique_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    category_data = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id','title','description','date_created','date_modified','unique_name',
                'author','author_name','article_category','category_data']

    def get_unique_name(self,obj):
        return str(obj.id) + "-"+obj.title[:10]

    def get_author_name(self,obj):
        return obj.author.first_name

    def get_category_data(self,obj):
        all_cat_objects = obj.article_category.all()
        return_list = []
        for cat in all_cat_objects:
            temp_dict = dict()
            temp_dict["id"] = cat.id
            temp_dict["name"] = cat.name
            return_list.append(temp_dict)
        return return_list

class CategorySerializer(serializers.ModelSerializer):

    articles = serializers.SerializerMethodField()

    class Meta:
        model = ArticleCategory
        fields = ['name','description','articles']

    def get_articles(self,obj):
        article_set = obj.article_set.all()
        return_list = []
        for art in article_set:
            temp_dict = dict()
            temp_dict['id'] = art.id
            temp_dict['title'] = art.title
            temp_dict['date_created'] = art.date_created
            author_dict = dict()
            author_dict['id'] = art.author.id
            author_dict['first_name'] = art.author.first_name
            author_dict['last_name'] = art.author.last_name
            temp_dict['author'] = author_dict
            return_list.append(temp_dict)
        return return_list

