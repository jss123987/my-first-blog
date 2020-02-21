from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
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
    )
    ssubcategories=[
     (WORLD,'World'),
     (US,'U.S.'),
     (ENTERTAINMENT,'Entertainment'),
     (SCIENCE,'Science'),
    ]
    subcategory= models.CharField(
     max_length=15,
     choices=ssubcategories,
     default=US)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
