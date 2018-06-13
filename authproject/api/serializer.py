from blog.models import Article
from rest_framework import serializers

class ArticleSerilizer(serializers.ModelSerializer):

    unique_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
    category_data = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id',
                'title',
                'description',
                'date_created',
                'date_modified',
                'unique_name',
                'author',
                'author_name',
                'article_category',
                'category_data'
                ]

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
