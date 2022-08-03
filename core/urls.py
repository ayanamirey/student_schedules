from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Timetable API',
        description='Test description',
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='sanjar.ravshanbekov@gmail.com'),
        license=openapi.License(name="Timeatable project"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authorization.urls')),
    path('api/v1/timetable/', include('app.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
]
