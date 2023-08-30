
from rest_framework import serializers
from .models import Article, User

class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    
    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "description",
            "content",
            "author",
            "author_name",  # Include the new field here
            "get_image",
            "get_thumbnail",
        )


    
        
class UserSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True)  # Use the ArticleSerializer for the articles
    # for this to work we must serialize it from the Article model since it is from the artcle model serilizer 

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "bio",
            "articles",  # Include the 'articles' field
            "position",
            "get_image",
            "get_thumbnail",
        )