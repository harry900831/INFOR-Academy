from django.db import models

class Course(models.Model):
	Topic = models.CharField(max_length = 50)

	def __str__(self):
		return self.Topic

class Article(models.Model):
	Title = models.CharField(max_length = 50, unique = True)
	Author = models.CharField(max_length = 20, blank = True)
	Time = models.DateTimeField()
	Content = models.TextField(max_length = 5000)
	Course = models.ForeignKey(Course, related_name = "Article", on_delete=models.PROTECT)

	def  __str__(self):
		return self.Title
