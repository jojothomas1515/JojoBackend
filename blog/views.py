from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    post = get_list_or_404(BlogPost)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)
