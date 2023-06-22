from django.db import models
from datetime import datetime

# Creater models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    message=models.TextField()
    is_resolved= models.BooleanField(default=False)
    Created_at=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'
    
    
    
    

