from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('api/v1/', include('users.urls')),
    
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# using the media in the frontend section
# that's how we do this
