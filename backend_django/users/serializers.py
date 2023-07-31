
from rest_framework import serializers
from .models import Article, User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Article
        
        fields = (
            "id",
            "title",
            "description",
            "content",
            "author",
            "get_image",
            "get_thumbnail",
        )
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "bio",
            "position",
            "get_image",
            "get_thumbnail",
        )

        
        