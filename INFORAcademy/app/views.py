from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app.models import Course,Visitor

def index(request):
	Views = Visitor.objects.get(id = 1)
	courses = Course.objects.all()
	if not ("counter" in request.COOKIES):
		Views.View = Views.View + 1
		Views.save()
		response = render(request, "index.html", locals())
		response.set_cookie("counter", 1)
		return response
	return render(request, "index.html", locals())

def detail(request, course):
	try:
		unit = Course.objects.get(Topic = course)
		articles = unit.Article.all()
		for article in articles:
			if article.Show == True:
				return HttpResponseRedirect('/'+course+'/'+str(article.id))
		return HttpResponseRedirect('/')
	except:
 		return HttpResponseRedirect('/')

def article(request, course, id):
	try:
		Views = Visitor.objects.get(id = 1)
		courses = Course.objects.all()
		unit = Course.objects.get(Topic = course)
		article = unit.Article.get(id = id)
		if article.Show == False:
			return HttpResponseRedirect('/')
		if not ("counter" in request.COOKIES):
			Views.View = Views.View + 1
			Views.save()
			response = render(request, "article.html", locals())
			response.set_cookie("counter", 1)
			return response
		return render(request, "article.html", locals())
	except:
		return HttpResponseRedirect('/')
