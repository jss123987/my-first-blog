from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Messages(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='from+')
    recipient=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='to+')
    message=models.TextField()
    published_date= models.DateTimeField(blank=True, null=True)

class Trashphoto(models.Model):
    trashphoto=models.FileField(upload_to='documents/originals/',)
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='original')
    contributers=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='contributers')
    caption = models.CharField(max_length=200)
    title = models.CharField(max_length=55, null=True)
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
    y1 = models.FloatField(null=True, blank=True, default=None)
    y2 = models.FloatField(null=True, blank=True, default=None)
    x1 = models.FloatField(null=True, blank=True, default=None)
    x2 = models.FloatField(null=True, blank=True, default=None)
    p1 = models.FileField(upload_to='documents/', default="t")
    p1y1 = models.FloatField(null=True, blank=True, default=None)
    p1y2 = models.FloatField(null=True, blank=True, default=None)
    p1x1 = models.FloatField(null=True, blank=True, default=None)
    p1x2 = models.FloatField(null=True, blank=True, default=None)
    p2= models.FileField(upload_to='documents/', default="t")
    p2y1 = models.FloatField(null=True, blank=True, default=None)
    p2y2 = models.FloatField(null=True, blank=True, default=None)
    p2x1 = models.FloatField(null=True, blank=True, default=None)
    p2x2 = models.FloatField(null=True, blank=True, default=None)
    p3 = models.FileField(upload_to='documents/', default="t")
    p3y1 = models.FloatField(null=True, blank=True, default=None)
    p3y2 = models.FloatField(null=True, blank=True, default=None)
    p3x1 = models.FloatField(null=True, blank=True, default=None)
    p3x2 = models.FloatField(null=True, blank=True, default=None)
    p4 = models.FileField(upload_to='documents/', default="t")
    p4y1 = models.FloatField(null=True, blank=True, default=None)
    p4y2 = models.FloatField(null=True, blank=True, default=None)
    p4x1 = models.FloatField(null=True, blank=True, default=None)
    p4x2 = models.FloatField(null=True, blank=True, default=None)
    p5 = models.FileField(upload_to='documents/', default="t")
    p5y1 = models.FloatField(null=True, blank=True, default=None)
    p5y2 = models.FloatField(null=True, blank=True, default=None)
    p5x1 = models.FloatField(null=True, blank=True, default=None)
    p5x2 = models.FloatField(null=True, blank=True, default=None)
    p6 = models.FileField(upload_to='documents/', default="t")
    p6y1 = models.FloatField(null=True, blank=True, default=None)
    p6y2 = models.FloatField(null=True, blank=True, default=None)
    p6x1 = models.FloatField(null=True, blank=True, default=None)
    p6x2 = models.FloatField(null=True, blank=True, default=None)
    p7 = models.FileField(upload_to='documents/', default="t")
    p7y1 = models.FloatField(null=True, blank=True, default=None)
    p7y2 = models.FloatField(null=True, blank=True, default=None)
    p7x1 = models.FloatField(null=True, blank=True, default=None)
    p7x2 = models.FloatField(null=True, blank=True, default=None)
    p8 = models.FileField(upload_to='documents/', default="t")
    p8y1 = models.FloatField(null=True, blank=True, default=None)
    p8y2 = models.FloatField(null=True, blank=True, default=None)
    p8x1 = models.FloatField(null=True, blank=True, default=None)
    p8x2 = models.FloatField(null=True, blank=True, default=None)
    p9 = models.FileField(upload_to='documents/', default="t")
    p9y1 = models.FloatField(null=True, blank=True, default=None)
    p9y2 = models.FloatField(null=True, blank=True, default=None)
    p9x1 = models.FloatField(null=True, blank=True, default=None)
    p9x2 = models.FloatField(null=True, blank=True, default=None)
    p10 = models.FileField(upload_to='documents/', default="t")
    p10y1 = models.FloatField(null=True, blank=True, default=None)
    p10y2 = models.FloatField(null=True, blank=True, default=None)
    p10x1 = models.FloatField(null=True, blank=True, default=None)
    p10x2 = models.FloatField(null=True, blank=True, default=None)
    p11 = models.FileField(upload_to='documents/', default="t")
    p11y1 = models.FloatField(null=True, blank=True, default=None)
    p11y2 = models.FloatField(null=True, blank=True, default=None)
    p11x1 = models.FloatField(null=True, blank=True, default=None)
    p11x2 = models.FloatField(null=True, blank=True, default=None)
    p12 = models.FileField(upload_to='documents/', default="t")
    p12y1 = models.FloatField(null=True, blank=True, default=None)
    p12y2 = models.FloatField(null=True, blank=True, default=None)
    p12x1 = models.FloatField(null=True, blank=True, default=None)
    p12x2 = models.FloatField(null=True, blank=True, default=None)
    p13 =  models.FileField(upload_to='documents/', default="t")
    p13y1 = models.FloatField(null=True, blank=True, default=None)
    p13y2 = models.FloatField(null=True, blank=True, default=None)
    p13x1 = models.FloatField(null=True, blank=True, default=None)
    p13x2 = models.FloatField(null=True, blank=True, default=None)
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

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[str(self.pk)])


class Profile(models.Model):
 Firstname = models.CharField(max_length=20, null=True)
 Lastname = models.CharField(max_length=20, null=True)
 EmailAddress = models.EmailField(null=True)
 Bio = models.TextField(max_length=95, null=True)
 Username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='usrname')
 profilepic = models.FileField(upload_to='documents/', default='', )
 y1 = models.FloatField(null=True, blank=True, default=None)
 y2 = models.FloatField(null=True, blank=True, default=None)
 x1 = models.FloatField(null=True, blank=True, default=None)
 x2 = models.FloatField(null=True, blank=True, default=None)
