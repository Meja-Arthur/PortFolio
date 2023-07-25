


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from.models import Article
from.serializers import ArticleSerializer
from django.http import FileResponse
from docx import Document
from django.views.generic import View

class ArticleListView(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serilizer = ArticleSerializer(articles, many=True)
        return Response(serilizer.data)
    

class ArticleDetailsView(APIView): 
    # we are using the get_object function that 
    def get_object(self, pk): 
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
              
    
    def get(self, request, pk,format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    




# views.py
from django.http import FileResponse
from docx import Document
from django.views.generic import View

class DownloadArticleView(View):
    def get(self, request, article_id):
        # Retrieve the article content from the database or wherever it's stored
        article_content = "The content of the article goes here."

        # Generate the Word document
        document = Document()
        document.add_heading('Article Title', level=1)
        document.add_paragraph(article_content)

        # Save the Word document to a BytesIO object (in-memory file)
        from io import BytesIO
        output = BytesIO()
        document.save(output)
        output.seek(0)

        # Create a FileResponse and send the Word document as a downloadable file
        response = FileResponse(output, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = f'attachment; filename=article_{article_id}.docx'
        return response

    
        
    



    

