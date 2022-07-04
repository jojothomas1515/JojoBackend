from rest_framework import serializers

from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    profile_image = serializers.ReadOnlyField(source='author.profile_image.url')

    class Meta:
        model = BlogPost
        fields = '__all__'

class NewPostSerializer(serializers.ModelSerializer):
    #experimental
    # def __int__(self, *args, **kwargs):
    #     author = args['author']
    #     super().__init__(*args, **kwargs)

    class Meta:
        model= BlogPost
        fields = ['heading', 'cover_image', 'post_field']