import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse
from .functions import upload_image



""" 
* all models: 
MySchool 
Team 
Subscribe 
Subject 
School_info 
News
Quote
OnlineService
*
"""

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class MySchool(UUIDModel):
    alt = models.CharField("Nomi",max_length=35)
    image = models.ImageField("Rasm")

    class Meta:
        verbose_name = "Mening Maktabim"
        verbose_name_plural = "Mening Maktabim"

    def __str__(self):
        return self.alt


class Team(UUIDModel):
    abr = "team"
    name = models.CharField(max_length=80)
    surename = models.CharField(max_length=80)
    jobs = models.CharField("Lavozim", max_length=80)
    contact = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image)
    telegram = models.URLField(null=True, blank=True)
    instagaram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)


    class Meta:
        verbose_name = "Maktab o'qituvchisi"
        verbose_name_plural = "Maktab o'qituvchilari"

    def __str__(self):
        return f"{self.name.capitalize()} {self.surename.capitalize()}"

    def get_absolute_url(self):
        return reverse("member_detail", kwargs={"pk": self.pk})


class Subscribe(UUIDModel):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Obuna"
        verbose_name_plural = "Obunalar"


class News(UUIDModel):
    abr = "news"
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Sarlavha",max_length=150)
    description = models.CharField("Ta'rif", max_length=350)
    image = models.ImageField("Maqola uchun rasm", upload_to=upload_image)
    body = models.TextField("To'liq matn")

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"
    
    def __str__(self):
        print("url is:", self.image.url)
        return self.title


class School_info(UUIDModel):
    phone = models.CharField(max_length=20)
    email = models.EmailField("School email")
    location = models.CharField(max_length=200)
    all_children = models.PositiveIntegerField("All Childrens")
    all_team = models.PositiveIntegerField("All Teachers")
    all_classes = models.PositiveIntegerField("All classes")
    all_extra_lessons = models.PositiveIntegerField("All extra lessons")

    class Meta:
        verbose_name = "School info"
        verbose_name_plural = "School info"

    def __str__(self):
        return "School info"
    

class Quote(UUIDModel):
    author = models.CharField("muallif", max_length=50)
    body = models.TextField("Maqol")

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = "Maqollar"
        verbose_name_plural = "Maqollar"


class OnlineService(UUIDModel):
    CHOISE = [
        ("bx bxl-dribbble", "sport"),
        ( "bx bx-file","hujjatlar"),
        ("bx bx-world", "web"),
        ("bx bx-git-branch", "linklar"),
    ]

    title = models.CharField("title", max_length=80)
    description = models.CharField("tarif", max_length=200)
    link = models.URLField(max_length=80)
    icon = models.CharField(choices=CHOISE, max_length=80)

    def __str__(self):
        return self.title[:20]

    class Meta:
        verbose_name = "Online Xizmatlar"
        verbose_name_plural = "Online Xizmatlar"
 

class MailToAdmin(UUIDModel):
    email = models.EmailField("email")
    name = models.CharField("ism", max_length=50)
    subject = models.CharField("mavzu", max_length=200)
    message = models.CharField(max_length=700)
    checked = models.BooleanField(default=False, editable=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "maktabga xat"
        verbose_name_plural = "maktabga xat"

    def __str__(self):
        return self.subject
