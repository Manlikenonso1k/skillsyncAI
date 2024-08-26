from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True, null=True)
    def __str__(self) -> str:
        return self.user.username


# CV details
class CVDETAILS(models.Model):
  
    user_profile = models.ForeignKey('userProfile', on_delete=models.CASCADE, related_name='cv_details')
  
    Full_name = models.CharField(max_length=255)
    
    Job_Title = models.CharField(max_length=255)
    
    phonenumber = models.IntegerField(blank=False, null=False)
    
    email = models.EmailField(max_length=50, blank=False, null=False)
    
    #SKILLS
    skills = models.ManyToManyField('skills', related_name='CVDETAILS', blank=False)

    # Languages
    languages = models.ManyToManyField('Language', related_name='cv_details', blank=True)

    # Passions
    passions = models.TextField(blank=True, null=True)
    
    #Experence fields 
    role = models.CharField ( max_length=70, blank=True, null=True)
    
    LEVEL_CHOICES = [('Junior', 'Junior'), ('Intermediate', 'Intermediate'), ('Experienced', 'Experienced')]
    
    level = models.CharField(max_length=15, choices=LEVEL_CHOICES, blank=False, null=False)
    
    start_date = models.DateField()
    
    end_date = models.DateField(blank=True, null=True)
    
    company_name = models.CharField(max_length=255, blank=False, null=False)
    
    company_description = models.CharField(max_length=255, blank=False, null=False)
    
    responsibilities = models.TextField(blank=True, null=True)
    
    location = models.CharField(max_length=255, blank=False, null=False)
    
    #EDUCATION FIELD
    
    school_name = models.CharField(max_length=255)
    
    DEGREE_CHOICES = [
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
    ]

    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, blank=False, null=False)

    def __str__(self) -> str:
        return f'{self.full_name} - {self.job_title}'

# Certificate model
class Certificate(models.Model):
    cv_details = models.ForeignKey(CVDETAILS, on_delete=models.CASCADE, related_name='certificates')
    
    name = models.CharField(max_length=255)
    
    issuer = models.CharField(max_length=255)
    
    issue_date = models.DateField()
    
    expiry_date = models.DateField(blank=True, null=True)
    
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.issuer}'

# Project model
class Project(models.Model):
    cv_details = models.ForeignKey(CVDETAILS, on_delete=models.CASCADE, related_name='projects')
    
    title = models.CharField(max_length=255)
    
    description = models.TextField()
    
    start_date = models.DateField()
    
    end_date = models.DateField(blank=True, null=True)
    
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.title


# Language model
class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


# Skills model
class Skills(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

  
