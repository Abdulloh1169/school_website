from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from . import models
from . import forms


# home page view
def index(request):
    school_info = models.School_info.objects.first()
    teachers = models.Team.objects.all()
    news = models.News.objects.order_by('date_added')
    my_school = models.MySchool.objects.all()
    quotes = models.Quote.objects.all()
    services = models.OnlineService.objects.all()
    try: 
        request.GET['submitted']
        sent = True
    except: 
        sent = False
    
    context = {
        "info": school_info,
        "teachers": teachers,
        "news": news[:10],
        "my_school": my_school,
        "sent": sent,
        "quotes": quotes,
        "services": services,
    }
    return render(request, 'index.html', context)


# view for getting info from user
def formget(request):
    if request.method == "POST":
        mail_form = forms.ContactAdminForm(request.POST)
        if mail_form.is_valid():
            mail_form.save()
            return HttpResponseRedirect("/?submitted")
    return redirect(request, "home")


# view for getting email from subscribe form
def subscribe(request):
    if request.method == "POST":
        email, created = models.Subscribe.objects.get_or_create(email=request.POST["email"])
    return HttpResponseRedirect("/")


# teams page view
def team(request):
    teachers = models.Team.objects.all()
    context = {
        "info": models.School_info.objects.first(),
        "teachers": teachers,
    }
    return render(request, "team.html", context)


# news detail view
def news(request, news_id):
    news = get_object_or_404(models.News, pk=news_id)
    info = models.School_info.objects.first()
    return render(request, "news.html", {"news": news, "info": info})
