from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse


class TastTest(TestCase):
    @classmethod
    def SetUpTestData(cls):
        cls.user=User.objects.create_user(
            username='testiser',
            email='testuser@mail.com',
            password='secret'
        )
        cls.task=Task.objects.create(
            title='New task',
            slug='new-task',
            body='testing task app',
            status='pending',
            created_by=cls.user
        )
