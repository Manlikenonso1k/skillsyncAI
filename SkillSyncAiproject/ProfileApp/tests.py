from django.test import TestCase
from django.contrib.auth.models import User
from .models import userprofile, CVDETAILS, Certificate, Project, Language, Skills

class UserProfileTestCase(TestCase):
    def setUp(self):
        # Set up a user for the UserProfile
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = userprofile.objects.create(user=self.user)

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.user.username, 'testuser')
        self.assertTrue(isinstance(self.user_profile, userprofile))

class CVDETAILSTestCase(TestCase):
    def setUp(self):
        # Set up the necessary data for testing CVDETAILS
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = userprofile.objects.create(user=self.user)
        self.language = Language.objects.create(name='English')
        self.skill = Skills.objects.create(name='Python')
        
        self.cv_details = CVDETAILS.objects.create(
            user_profile=self.user_profile,
            Full_name='John Doe',
            Job_Title='Software Developer',
            phonenumber=1234567890,
            email='johndoe@example.com',
            role='Developer',
            level='Junior',
            start_date='2020-01-01',
            end_date='2022-01-01',
            company_name='Tech Corp',
            company_description='A tech company',
            responsibilities='Development and testing',
            location='New York',
            school_name='ABC University',
            degree='Bachelor'
        )
        self.cv_details.languages.add(self.language)
        self.cv_details.skills.add(self.skill)

    def test_cv_details_creation(self):
        self.assertEqual(self.cv_details.Full_name, 'John Doe')
        self.assertEqual(self.cv_details.level, 'Junior')
        self.assertTrue(isinstance(self.cv_details, CVDETAILS))

    def test_cv_details_relations(self):
        self.assertIn(self.language, self.cv_details.languages.all())
        self.assertIn(self.skill, self.cv_details.skills.all())

class CertificateTestCase(TestCase):
    def setUp(self):
        # Set up the necessary data for testing Certificate
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = userprofile.objects.create(user=self.user)
        self.cv_details = CVDETAILS.objects.create(
            user_profile=self.user_profile,
            Full_name='John Doe',
            Job_Title='Software Developer',
            phonenumber=1234567890,
            email='johndoe@example.com',
            role='Developer',
            level='Junior',
            start_date='2020-01-01',
            end_date='2022-01-01',
            company_name='Tech Corp',
            company_description='A tech company',
            responsibilities='Development and testing',
            location='New York',
            school_name='ABC University',
            degree='Bachelor'
        )
        self.certificate = Certificate.objects.create(
            cv_details=self.cv_details,
            name='Django Certification',
            issuer='Django Organization',
            issue_date='2021-01-01',
            expiry_date='2023-01-01',
            description='Certified Django Developer'
        )

    def test_certificate_creation(self):
        self.assertEqual(self.certificate.name, 'Django Certification')
        self.assertTrue(isinstance(self.certificate, Certificate))

class ProjectTestCase(TestCase):
    def setUp(self):
        # Set up the necessary data for testing Project
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = userprofile.objects.create(user=self.user)
        self.cv_details = CVDETAILS.objects.create(
            user_profile=self.user_profile,
            Full_name='John Doe',
            Job_Title='Software Developer',
            phonenumber=1234567890,
            email='johndoe@example.com',
            role='Developer',
            level='Junior',
            start_date='2020-01-01',
            end_date='2022-01-01',
            company_name='Tech Corp',
            company_description='A tech company',
            responsibilities='Development and testing',
            location='New York',
            school_name='ABC University',
            degree='Bachelor'
        )
        self.project = Project.objects.create(
            cv_details=self.cv_details,
            title='Portfolio Website',
            description='A personal portfolio website',
            start_date='2020-01-01',
            end_date='2020-12-31',
            url='https://example.com'
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, 'Portfolio Website')
        self.assertTrue(isinstance(self.project, Project))
