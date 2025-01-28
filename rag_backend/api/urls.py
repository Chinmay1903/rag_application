from django.urls import path
from .views import DocumentIngestionView, QandAView, DocumentSelectionView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('documents/', DocumentIngestionView.as_view(), name='document_ingestion'),
    path('qa/', QandAView.as_view(), name='qa'),
    path('documents/select/', DocumentSelectionView.as_view(), name='document_selection'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
