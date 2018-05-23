from django.db import models

class Course(models.Model):
	Topic = models.CharField(max_length = 50)
	def __str__(self):
		return self.Topic

class Article(models.Model):
	Title = models.CharField(max_length = 50)
	Author = models.CharField(max_length = 20, blank = True)
	Time = models.DateTimeField(auto_now = True)
	Content = models.TextField(max_length = 10000)
	Quantity = models.PositiveIntegerField(default = 0)
	Course = models.ForeignKey(Course, related_name = "Article",
                               on_delete=models.PROTECT)
	def  __str__(self):
		return (self.Title)