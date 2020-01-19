from django.shortcuts import render
import datetime
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse
from .models import News
from .models import Category
from .models import Country
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import NewsForm
from django.db.models import Q
def index(request):
    latest_news_list = News.objects.order_by('-pub_date')
    category = Category.objects.all()
    countries = Country.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_news_list, 10)
    numofnews = len(News.objects.all())

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
            'latest_news_list': latest_news_list,
            'category': category,
            'countries': countries,
            'users': users,
            'numofnews': numofnews,
    }

    return render(request, 'home/index.html', context)

def detail(request, news_id):
    news = News.objects.get(pk=news_id)
    category = Category.objects.all()
    countries = Country.objects.all()
    return render(request, 'home/detail.html', {'news': news, 'category': category, 'countries': countries, })

def create(request):
    if request.method == "POST":
        #adding = News()
        #adding.likes = 0
        #adding.pub_date = timezone.now()
        #adding.article = request.POST.get("Article")
        #adding.content = request.POST.get("Content")
        #adding.category = request.POST.get("Category")
        #adding.country = request.POST.get("Country")
        #adding.save()
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.pub_date = timezone.now()
            news.likes = 0
            news.save()
            return HttpResponseRedirect("/home/")
    else:
        form = NewsForm()
    context = {'form': form}

    return render(request, 'home/create.html', context)
    '''
    Create a new html create and put posting news there. Edit views, urls, index.html, create.html
    
    
    '''


def delete_news(request, news_id):
    obj = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        obj.delete()

    return HttpResponseRedirect("/home/")


def edit_news(request, pk):
    post = get_object_or_404(News, pk=pk)
    template = 'home/create.html'

    if request.method == "POST":
        form = NewsForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = NewsForm(instance=post)


    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


def listofcategories(request, pk):
    categories = Category.objects.all()
    post = News.objects.all()
    category = get_object_or_404(Category, pk=pk)
    post = post.filter(category=category)
    template = 'home/listofcategories.html'
    context = {
        'categories': categories,
        'post': post,
        'category': category
    }
    return render(request, template, context)


def likepost(request, news_id):
    obj = get_object_or_404(News, id=news_id)
    if request.method == "POST":
        obj.likes = obj.likes + 1
        obj.save()
    return HttpResponseRedirect("../")


def search(request):
    template = 'home/index.html'
    query = request.GET.get('q')
    result = News.objects.filter(Q(article__contains=query) | Q(content__icontains=query))
    page = request.GET.get('page', 1)
    paginator = Paginator(result, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'result': result,
        'page': page,
        'paginator': paginator,
        'users': users,
    }
    return render(request, template, context)