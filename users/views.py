from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import CustomUser
from users.serializer import ProfileImageSerializer, ProfileInfoSerializer, UserSerializers


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userInfo(request):
    user = CustomUser.objects.get(pk=request.user.id)
    serialized = UserSerializers(user)
    return Response(serialized.data)


@api_view(['POST'])
def changeProfileImage(request):
    form = ProfileImageSerializer(data=request.data, instance=request.user)
    if form.is_valid():
        form.save()

        return Response(form.data)


@api_view(['POST'])
def changeName(request):
    form = ProfileInfoSerializer(data=request.data, instance=request.user)
    if form.is_valid():
        form.save()
        return Response(form.data)
    return Response(form.data)