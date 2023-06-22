from django.contrib import admin
from .models import Contact
# Register your models here.
class contatAdmin(admin.ModelAdmin):
    list_display = ('email','name','is_resolved','Created_at')
    list_editable=('is_resolved',)
    list_filter = ('is_resolved','Created_at')
    
admin.site.register(Contact,contatAdmin)
