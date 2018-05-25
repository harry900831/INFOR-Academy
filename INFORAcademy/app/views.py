from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app.models import Course

def index(request):
	courses = Course.objects.all()
	return render(request, "index.html", locals())

def detail(request, course):
	try:
		unit = Course.objects.get(Topic = course)
		articles = unit.Article.all()
		for article in articles:
			if article.Show == 1:
				return HttpResponseRedirect('/'+course+'/'+str(article.id))
		return HttpResponseRedirect('/')
	except:
 		return HttpResponseRedirect('/')

def article(request, course, id):
	try:
		unit = Course.objects.get(Topic = course)
		article = unit.Article.get(id = id)
		if article.Show == 0:
			return HttpResponseRedirect('/')
		articles = unit.Article.all()
		return render(request, "article.html", locals())
	except:
		return HttpResponseRedirect('/')

def test(request):
	return render(request, "test.html")
