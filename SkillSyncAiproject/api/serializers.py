from rest_framework import serializers
from ProfileApp.models import userprofile, CVDETAILS, Certificate, Project, Language, Skills

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userprofile
        fields = '__all__'

class CVDETAILSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVDETAILS
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
