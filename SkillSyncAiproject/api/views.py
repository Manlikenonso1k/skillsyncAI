from rest_framework import viewsets
from ProfileApp.models import userprofile, CVDETAILS, Certificate, Project, Language, Skills
from .serializers import UserProfileSerializer, CVDETAILSSerializer, CertificateSerializer, ProjectSerializer, LanguageSerializer, SkillsSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = userprofile.objects.all()
    serializer_class = UserProfileSerializer

class CVDETAILSViewSet(viewsets.ModelViewSet):
    queryset = CVDETAILS.objects.all()
    serializer_class = CVDETAILSSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
