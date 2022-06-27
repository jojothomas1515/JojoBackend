from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import CustomUser
from users.serializer import UserSerializers


@api_view(['GET'])
def userInfo(request):
    user = CustomUser.objects.get(pk=request.user.id)
    serialized = UserSerializers(user)
    print(serialized.data)
    return Response(serialized.data)

