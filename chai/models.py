from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class chaiVarity(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_add=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self):

        return self.name


#one to many relationship
class ChaiReview(models.Model):
    chai=models.ForeignKey(chaiVarity,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
# many to many
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varietes=models.ManyToManyField(chaiVarity,related_name='store')
    
    def __str__(self):
        return self.name

# one to one rlationship
class ChaiCertificate(models.Model):
    chai=models.OneToOneField(chaiVarity,on_delete=models.CASCADE,related_name='certificate')
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_untill=models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai}'


    #my protfolio models Databse#

 #About model
    
class About(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=True)
    degree=models.TextField(null=True)
    about_heading=models.CharField(max_length=100)
    personal_info=models.TextField(default='')
    date_of_birth=models.CharField(max_length=25)
    age=models.IntegerField()
    website=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=15)
    email=models.EmailField(max_length=256)
    city=models.CharField(max_length=50)
    freelance=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    image=models.ImageField(upload_to='profile/')
    about_me=models.TextField(default='')
    date=models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f" {self.name}"



#skill model

class Skill(models.Model):
    about=models.OneToOneField(About,on_delete=models.CASCADE)
    about_skill=models.TextField()
    htlm=models.IntegerField()
    css=models.IntegerField()
    java_script=models.IntegerField()
    python=models.IntegerField()
    django=models.IntegerField()
    linux=models.IntegerField()
      
    def __str__(self):
        return f" Skills"

#Resume model

class Resume(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name_of_degree=models.TextField()
    year=models.CharField(max_length=50)
    institute_name_and_address=models.TextField(default='')
   
    def __str__(self):
        return f" {self.name_of_degree}"
   


#Social Media LInk

class Socalmedia(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    facebook=models.URLField(blank=True)
    instagram=models.URLField(blank=True)
    twitter=models.URLField(blank=True)
    github=models.URLField(blank=True)
    linkedin=models.URLField(blank=True)
    cv_file=models.FileField(upload_to='cv_file/',default='')
    date=models.DateTimeField(timezone.now)

    def __str__(self):

        return f" {self.user}"
