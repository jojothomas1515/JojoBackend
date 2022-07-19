from django.shortcuts import get_list_or_404
from requests import status_codes

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import BlogPost
from .serializers import BlogPostSerializer, NewPostSerializer


# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    post = get_list_or_404(BlogPost)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userPosts(request):
    post = get_list_or_404(BlogPost, author=request.user)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)\

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userProfilePosts(request, username):
    post = BlogPost.objects.filter(author__username=username)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)

@api_view(["POST"])
def addPost(request):
    newpost = NewPostSerializer(data=request.data)
    if newpost.is_valid():
        newpost = newpost.save()
        newpost.author = request.user
        newpost.save()

        return Response(status=200)

@api_view(['DELETE'])
def removePost(request, pk):
    post = BlogPost.objects.get(pk=pk)
    post.delete()
    return Response(status=200)

@api_view(['GET'])
def viewPost(request, pk):
    post = BlogPost.objects.get(pk=pk)
    post = BlogPostSerializer(post)
    return Response(post.data)