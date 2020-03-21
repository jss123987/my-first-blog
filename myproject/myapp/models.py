from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='original')
    contributers=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='contributers')
    caption = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=55,blank=True,null=True)
    Text=models.TextField(blank=True)
    b=models.TextField(blank=True)
    c=models.TextField(blank=True)
    d=models.TextField(blank=True)
    e=models.TextField(blank=True)
    f=models.TextField(blank=True)
    g=models.TextField(blank=True)
    h=models.TextField(blank=True)
    i=models.TextField(blank=True)
    j=models.TextField(blank=True)
    k=models.TextField(blank=True)
    l=models.TextField(blank=True)
    m=models.TextField(blank=True)
    upload = models.FileField(upload_to='documents/', default="")
    p1 = models.FileField(upload_to='documents/', default="t")
    p2= models.FileField(upload_to='documents/', default="t")
    p3 = models.FileField(upload_to='documents/', default="t")
    p4 = models.FileField(upload_to='documents/', default="t")
    p5 = models.FileField(upload_to='documents/', default="t")
    p6 = models.FileField(upload_to='documents/', default="t")
    p7 = models.FileField(upload_to='documents/', default="t")
    p8 = models.FileField(upload_to='documents/', default="t")
    p9 = models.FileField(upload_to='documents/', default="t")
    p10 = models.FileField(upload_to='documents/', default="t")
    p11 = models.FileField(upload_to='documents/', default="t")
    p12 = models.FileField(upload_to='documents/', default="t")
    p13 =  models.FileField(upload_to='documents/', default="t")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    lastedit=models.DateTimeField(blank=True,null=True)
    ARCHEOLOGY='Archeology'
    CRIME='Crime'
    EDUCATION='Education'
    IMMIGRATION='Immigration'
    CONFLICTS='Conflicts'
    DISASTER='Disaster'
    ENVIRONMENT='Environment'
    RELIGION='Religion'
    SCANDALS='Scandals'
    MUSICNEWS='Music News'
    CELEBRITYNEWS='Celebrity News'
    WILDNATURE='Wild Nature'
    NATURALSCIENCE='Natural Science'
    US ='U.S.'
    OPINION='Opinion'
    ENTERTAINMENT='Entertainment'
    SCIENCE='Science'
    WORLD='World'
    news_categories = [
     (ARCHEOLOGY, 'Archeology'),
     (CELEBRITYNEWS,'Celebrity News'),
     (CONFLICTS,'Conflicts'),
     (CRIME,'Crime'),
     (DISASTER,'Disaster'),
     (EDUCATION,'Education'),
     (ENVIRONMENT,'Environment'),
     (IMMIGRATION,'Immigration'),
     (MUSICNEWS,'Music News'),
     (NATURALSCIENCE,'Natural Science'),
     (RELIGION,'Religion'),
     (SCANDALS,'Scandals'),
     (WILDNATURE,'Wild Nature'),
     (OPINION, 'Opinion'),
    ]
    category = models.CharField(
     max_length=15,
     choices=news_categories,
     default=ARCHEOLOGY,
     blank=True,null=True
    )
    subcategory= models.CharField(
     max_length=15)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


