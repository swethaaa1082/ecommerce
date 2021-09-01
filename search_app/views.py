from django.shortcuts import render
from ecommerce_app.models import Category
from django.db.models import Q

# Create your views here.
def searchResult(request):
    category=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        category=Category.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,"search.html",{'query':query,'category':category})