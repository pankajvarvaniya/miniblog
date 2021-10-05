from django.contrib import admin
from .models import Post,Image
# Register your models here.
class Mypost(admin.ModelAdmin):
	list_display=['title','description']

admin.site.register(Post,Mypost)	


class Myimage(admin.ModelAdmin):
	list_display=['id','image','date']

admin.site.register(Image,Myimage)	