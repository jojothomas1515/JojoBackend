from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework import authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import settings

schema_view = get_schema_view(
    openapi.Info(title="Jojo Page API",
                 default_version='v1',
                 description="Backend for jojo page react version",
                 contact=openapi.Contact(email="jojothomas1515@gmail.com", name="Joseph Thomas Ehigie",
                                         url="https://www.jojothomas.tech"),
                 license=openapi.License(name="MIT")
                 ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(authentication.SessionAuthentication, authentication.BasicAuthentication,),
    validators=['ssv']
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/user/', include('users.urls')),
    path('api/auth/', include('authentication.urls'))
]
# for debug mode
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
