from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser
from users.serializer import ProfileImageSerializer, ProfileInfoSerializer, UserSerializers


@swagger_auto_schema(
    methods=['GET'],
    operation_description='Get The Logged in User Profile',
    responses={200: UserSerializers(many=False)}
)
@swagger_auto_schema(
    methods=['PUT'],
    operation_description='Update the Logged in User Profile',
    request_body=ProfileInfoSerializer(),
    responses={201: ProfileInfoSerializer(many=False)}
)
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def userInfo(request):
    if request.method == 'GET':
        user = CustomUser.objects.get(pk=request.user.id)
        serialized = UserSerializers(user)
        return Response(serialized.data)
    elif request.method == 'PUT':
        form = ProfileInfoSerializer(data=request.data, instance=request.user)
        if form.is_valid():
            form.save()
            return Response(form.data)
        return Response(form.data)


@swagger_auto_schema(
    methods=['PUT'],
    operation_description='Update the Logged in User Profile Picture',
    request_body=ProfileImageSerializer(),
    responses={201: ProfileImageSerializer(many=False)}
)
@api_view(['PUT'])
def changeProfileImage(request):
    form = ProfileImageSerializer(data=request.data, instance=request.user)
    if form.is_valid():
        form.save()

        return Response(form.data)


@swagger_auto_schema(
    methods=['GET'],
    operation_description='Get the user profile information',
    responses={200: UserSerializers(many=False)}
)
@api_view(['GET'])
def users_profile_view(request, username):
    print(username)
    try:
        user = CustomUser.objects.get(username__iexact=username)
        serialized_data = UserSerializers(user)
        return Response(serialized_data.data)
    except Exception:
        return Response(status=404)
