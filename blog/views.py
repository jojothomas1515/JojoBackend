from django.shortcuts import get_list_or_404
from requests import status_codes

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import BlogPost
from .serializers import BlogPostSerializer, NewPostSerializer


# Create your views here.

@swagger_auto_schema(
    method='get',
    operation_description='Get all post on the platform',
    responses={200: BlogPostSerializer(many=True)},
    tags=["BlogPosts", ]
)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    post = get_list_or_404(BlogPost)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)


@swagger_auto_schema(
    method='get',
    operation_description='Retrieve all the posts made by current user',
    responses={200: BlogPostSerializer(many=True)},
    tags=["BlogPosts", ]

)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_post(request):
    post = get_list_or_404(BlogPost, author=request.user)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)


@swagger_auto_schema(
    method='get',
    operation_description='Retrieve all the posts made by a specific user',
    responses={200: BlogPostSerializer(many=True)},
    tags=["BlogPosts", ]

)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_post(request, username):
    post = BlogPost.objects.filter(author__username=username)
    serialPost = BlogPostSerializer(post, many=True)
    return Response(serialPost.data)


@swagger_auto_schema(
    method='POST',
    operation_description='Create and publish a post by the current user.',
    responses={200: NewPostSerializer()},
    tags=["BlogPosts", ]
)
@api_view(["POST"])
def add_post(request):
    newpost = NewPostSerializer(data=request.data)
    if newpost.is_valid():
        newpost = newpost.save()
        newpost.author = request.user
        newpost.save()

        return Response(status=200)


@swagger_auto_schema(
    method='DELETE',
    operation_description='Delete the post it the id, and long as the person requesting for the post remover is the '
                          'owner.',
    responses={200: ""},
    tags=["BlogPosts", ]

)
@api_view(['DELETE'])
def remove_post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    post.delete()
    return Response(status=200)


@swagger_auto_schema(
    method='GET',
    operation_description='The the content of a post specified by the id',
    responses={200: ""},
    tags=["BlogPosts", ]
)
@api_view(['GET'])
def view_post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    post = BlogPostSerializer(post)
    return Response(post.data)
