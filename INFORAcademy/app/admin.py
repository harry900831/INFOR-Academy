from django.contrib import admin
from app import models

class ArticleAdmin(admin.ModelAdmin):
	list_display=('Title',)
	ordering=('Course','id',)
	list_filter = ('Course',)

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Course)
admin.site.register(models.Visitor)



