from django.shortcuts import render
from .models import Post

# Create your views here.
def bloggirls(request):
	mylist = Post.objects.all()

	return render(request, 'blog/plantillablog.html', {"mylist":mylist})