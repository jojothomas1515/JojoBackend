from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.serializers import MyTokenObtainPairSerializer, SignupSerializer, SuccessfulSignUpMessageSerializer, \
    UserAlreadyExistsMessageSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="Obtain access token for the user",
        tags=['Authentication', ],
        security=[],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, example='example_email@mail.com'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, example='password12345'),
            }
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'refresh': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example='<JWT REFRESH TOKEN >'
                    ),
                    'access': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example='<JWT ACCESS TOKEN >'
                    )
                }
            ),
            401: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING),
                    'status': openapi.Schema(type=openapi.TYPE_STRING),
                    'code': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        }
    )
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class MyTokenRefreshView(TokenRefreshView):

    @swagger_auto_schema(
        operation_description="Obtain access token for the user",
        tags=['Authentication', ],
        security=[],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refreshToken': openapi.Schema(type=openapi.TYPE_STRING, example='refresh_token'),
            }
        ),
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example='<JWT ACCESS TOKEN>'
                    ),
                    'refresh': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example='<JWT REFRESH TOKEN>'
                    )
                }
            )
        }
    )
    def post(self, request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


@swagger_auto_schema(
    method='POST',
    operation_description="Create a new user",
    tags=["Authentication"],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, example='username'),
            'firstname': openapi.Schema(type=openapi.TYPE_STRING),
            'lastname': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING, example='<EMAIL>'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, example='password'),
            'password2': openapi.Schema(type=openapi.TYPE_STRING, example='password2'),
        },
    ),

    security=[],
    responses={
        201: SuccessfulSignUpMessageSerializer(),
        409: UserAlreadyExistsMessageSerializer()
    },

)
@api_view(['POST'])
def signup_view(request):
    user = SignupSerializer(data=request.data)
    if user.is_valid():
        user = user.save()
        return Response({'success': f'{user.username} account created successfully',
                         'code': 'registration_success', 'status': 'Success'}, 201)
    else:
        return Response(user.errors, status=400)
