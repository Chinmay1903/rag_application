from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Document, Question
from django.core.files.uploadedfile import SimpleUploadedFile
import json

class APITestCase(TestCase):
    def setUp(self):
        """Set up test user and authentication"""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

    def test_register_user(self):
        """Test user registration API"""
        response = self.client.post("/api/register/", {
            "username": "newuser",
            "password": "newpass123",
            "email": "newuser@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        """Test user login API"""
        response = self.client.post("/api/login/", {
            "username": "testuser",
            "password": "testpass"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_upload_document(self):
        """Test document upload API"""
        file_content = b"Sample text content"
        file = SimpleUploadedFile("test.txt", file_content, content_type="text/plain")
        
        response = self.client.post("/api/upload/", {"file": file})
        self.assertEqual(response.status_code, 201)
        self.assertIn("document_id", response.data)

    def test_ask_question(self):
        """Test asking a question API"""
        document = Document.objects.create(user=self.user, file="test.txt")
        
        response = self.client.post(f"/api/ask/{document.id}/", {
            "question": "What is this document about?"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("answer", response.data)

    def test_unauthorized_access(self):
        """Test accessing API without authentication"""
        client = APIClient()  # New client without authentication
        response = client.get("/api/upload/")
        self.assertEqual(response.status_code, 401)  # Unauthorized
