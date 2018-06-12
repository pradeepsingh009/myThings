from blog.models import Article
from rest_framework import serializers

class ArticleSerilizer(serializers.ModelSerializer):

    unique_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['title','description','date_created','date_modified','unique_name']

    def get_unique_name(self,obj):
        return str(obj.id) + "-"+obj.title[:10]
