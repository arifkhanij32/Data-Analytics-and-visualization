from rest_framework import serializers
from .models import UserProfile, AnalyticsData
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'role']

class AnalyticsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalyticsData
        fields = ['user', 'event_type', 'timestamp', 'details']
