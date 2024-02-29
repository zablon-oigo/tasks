from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task
from django.urls import reverse


class TaskTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user=User.objects.create_user(
            username='testuser',
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

    def test_model_content(self):
        self.assertEqual(self.task.title, "New task")
        self.assertEqual(self.task.slug, "new-task")
        self.assertEqual(self.task.body, "testing task app")
        self.assertEqual(self.task.status, "pending")
        self.assertEqual(self.task.created_by.username, "testuser")
        self.assertEqual(str(self.task), "New task")
        self.assertEqual(self.task.get_absolute_url(), "/detail/1/new-task/")
