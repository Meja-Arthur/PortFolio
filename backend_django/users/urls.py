from django.urls import path
from django.urls import path, register_converter
from . import views
from .views import DownloadArticleView

# Define a custom converter for UUID
class UUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return str(value)

register_converter(UUIDConverter, 'uuid')

urlpatterns = [
    path('latest-articles/', views.ArticleListView.as_view()),
    path('article/<uuid:pk>/', views.ArticleDetailsView.as_view()),
    path('api/v1/article/<str:article_id>/download/', DownloadArticleView.as_view(), name='download_article'),
]



