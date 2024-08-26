from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, CVDETAILSViewSet, CertificateViewSet, ProjectViewSet, LanguageViewSet, SkillsViewSet

router = DefaultRouter()
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'cvdetails', CVDETAILSViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'skills', SkillsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
