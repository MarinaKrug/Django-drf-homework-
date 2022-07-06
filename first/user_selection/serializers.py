from rest_framework import serializers
from user_selection.models import User

class UserSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('role_choice', 'Offer')