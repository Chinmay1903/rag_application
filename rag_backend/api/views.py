from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from .models import Document, Question
from .serializers import RegisterSerializer
from .utils import generate_answer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UploadDocumentView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        document = Document.objects.create(user=request.user, file=file)
        return Response({"message": "Document uploaded successfully", "document_id": document.id}, status=201)

class AskQuestionView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, doc_id):
        document = get_object_or_404(Document, id=doc_id, user=request.user)
        question_text = request.data.get("question")
        if not question_text:
            return Response({"error": "Question is required"}, status=400)

        # Read the document content
        with open(document.file.path, 'r') as f:
            document_text = f.read()
        
        # # Convert encoding (Auto-detect)
        # encoding = chardet.detect(raw_data)['encoding']
        # document_text = raw_data.decode(encoding or 'utf-8', errors='replace')  # Replace bad characters

        # Generate answer using OpenAI
        try:
            answer = generate_answer(question_text, document_text)
            question = Question.objects.create(
                user=request.user,
                document=document,
                question=question_text,
                answer=answer
            )
            return Response({"question": question_text, "answer": answer}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
