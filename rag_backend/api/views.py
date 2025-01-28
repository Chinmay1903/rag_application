import openai
import numpy as np
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Document
from .serializers import DocumentSerializer, RegisterSerializer


# Document Ingestion API
class DocumentIngestionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')

        # Generate embeddings using OpenAI API
        embedding = openai.Embedding.create(
            input=content,
            model="text-embedding-ada-002"
        )['data'][0]['embedding']

        # Save document to the database
        doc = Document.objects.create(title=title, content=content, embedding=embedding)
        return Response({'message': 'Document ingested successfully', 'document_id': doc.id})


# Q&A API
class QandAView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        question = request.data.get('question')

        # Generate question embedding
        question_embedding = openai.Embedding.create(
            input=question,
            model="text-embedding-ada-002"
        )['data'][0]['embedding']

        # Retrieve relevant documents
        documents = Document.objects.all()
        similarities = [
            (doc, np.dot(np.array(doc.embedding), np.array(question_embedding)))
            for doc in documents
        ]
        sorted_docs = sorted(similarities, key=lambda x: x[1], reverse=True)
        top_doc = sorted_docs[0][0] if sorted_docs else None

        if top_doc:
            # Generate answer using OpenAI's GPT model
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Answer based on the document: {top_doc.content}. {question}"}
                ]
            )
            answer = response['choices'][0]['message']['content']
            return Response({'answer': answer, 'document': top_doc.title})
        else:
            return Response({'answer': 'No relevant document found'})


# Document Selection API
class DocumentSelectionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        documents = Document.objects.values('id', 'title')
        return Response({'documents': list(documents)})

    def post(self, request):
        selected_ids = request.data.get('document_ids', [])
        selected_docs = Document.objects.filter(id__in=selected_ids)
        titles = [doc.title for doc in selected_docs]
        return Response({'selected_documents': titles})
    
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
