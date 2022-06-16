from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    post = get_list_or_404(BlogPost)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)
