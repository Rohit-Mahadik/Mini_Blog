from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class ModelAdmin(admin.ModelAdmin):
    list_display=['id','tittle','desc']