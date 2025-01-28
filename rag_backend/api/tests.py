from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Document

class APITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token_url = "/api/token/"
        self.document_url = "/api/documents/"
        self.qa_url = "/api/qa/"
        self.document_select_url = "/api/documents/select/"

        # Log in and get JWT token
        response = self.client.post(self.token_url, {"username": "testuser", "password": "testpassword"})
        self.token = response.data["access"]

        # Add token to default headers
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_token_authentication(self):
        response = self.client.post(self.token_url, {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_document_ingestion(self):
        data = {
            "title": "Test Document",
            "content": "This is a test document."
        }
        response = self.client.post(self.document_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("document_id", response.data)

    def test_document_selection(self):
        # Create a document
        Document.objects.create(title="Doc1", content="Content1", embedding=[0.1, 0.2, 0.3])

        # Fetch documents
        response = self.client.get(self.document_select_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data["documents"]) > 0)

        # Select documents
        document_id = response.data["documents"][0]["id"]
        response = self.client.post(self.document_select_url, {"document_ids": [document_id]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("selected_documents", response.data)

    def test_qa_api(self):
        # Create a document
        Document.objects.create(title="Doc1", content="This is a test document about AI.", embedding=[0.1, 0.2, 0.3])

        # Test QA API
        question = {"question": "What is this document about?"}
        response = self.client.post(self.qa_url, question)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("answer", response.data)
