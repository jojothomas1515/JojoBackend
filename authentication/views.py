from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from authentication.serializers import MyTokenObtainPairSerializer, SignupSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




@api_view(['POST'])
def signup_view(request):
    user = SignupSerializer(data=request.data)
    if user.is_valid():
        user = user.save()
        return Response({'success': f'{user.username} account created successfully'})
    else:
        return Response(user.errors, status=400)
