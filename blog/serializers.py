from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]

        extra_kwargs = {
            'password':{'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "facebook",
                   "bio", "profile_picture", "youtube", "twitter", "instagram"]
        
class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id",  "username", "first_name", "last_name",]

class BlogSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = fields = [
    'title',
    'slug',
    'content',
    'author',
    'created_at',
    'updated_at',
    'published_date',
    'is_draft',
    'category',
    'feature_image',
]
