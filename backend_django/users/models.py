from io import BytesIO
from PIL import Image
import uuid

from django.core.files import File
from django.db import models

# Create your models here.

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default='', null=True)
    bio = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_added',)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
    def get_image(self):
        
        if self.image:
            return 'http://127.0.0.1:8200' + self.image.url
        return ''
    
    def get_thumbnail(self):
        
        if self.thumbnail:
            return 'http://127.0.0.1:8200' + self.thumbnail.url
        
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8200' + self.thumbnail.url
            
            else:
                return ''
            
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)        
        
        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail