from django.urls import path
from . import views as _
from ConnectAdmin import views as contact

urlpatterns = [
    path('', _.index, name="home"),
    path('send/', _.formget),
    path('subscribe/', _.subscribe, name="subscribe"),
    path('maktab_jamoasi/', _.team, name="team"),
    path("news/<str:news_id>/", _.news, name="news"),
    path("contact/", contact.contact_admin, name="contact_admin"),
    path("contact/<str:id>/<str:generate>/", contact.generate_message, name="generate"),
]