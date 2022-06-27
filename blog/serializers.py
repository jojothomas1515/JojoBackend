from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    profile_image = serializers.ReadOnlyField(source='author.profile_image.url')

    class Meta:
        model = BlogPost
        fields = '__all__'
