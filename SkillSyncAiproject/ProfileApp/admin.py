from django.contrib import admin
from .models import userprofile, CVDETAILS, Certificate, Project, Language, Skills
# Register your models here.
admin.site.register(userprofile)
admin.site.register(CVDETAILS)
admin.site.register(Certificate)
admin.site.register(Project)
admin.site.register(Language)
admin.site.register(Skills)

