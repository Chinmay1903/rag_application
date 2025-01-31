from django.urls import path
from .views import RegisterView, UploadDocumentView, AskQuestionView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('upload/', UploadDocumentView.as_view(), name='upload-document'),
    path('ask/<int:doc_id>/', AskQuestionView.as_view(), name='ask-question'),
]
