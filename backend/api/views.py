from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import AnalyticsData
from .serializers import AnalyticsDataSerializer

class AnalyticsDataViewSet(viewsets.ModelViewSet):
    queryset = AnalyticsData.objects.all()
    serializer_class = AnalyticsDataSerializer
    permission_classes = [permissions.IsAuthenticated]

# Custom token view can be created here if needed for authentication.
