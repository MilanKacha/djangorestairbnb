from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    # Use SerializerMethodField or source to include avatar_url
    avatar_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'avatar_url', 'email')  # added email for convenience
        read_only_fields = ('id', 'avatar_url', 'email')

    def get_avatar_url(self, obj):
        # Safely return avatar URL
        if obj.avatar and hasattr(obj.avatar, 'url'):
            return f"{self.context.get('request').build_absolute_uri(obj.avatar.url)}"
        return ""
    
    


class CustomRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['name'] = self.validated_data.get('name', '')
        return data
