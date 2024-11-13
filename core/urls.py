from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Book Management API",
      default_version='v1',
      description="API for book management.",
      terms_of_service="",
      contact=openapi.Contact(email="lyalima0328@gmail.com"),
      license=openapi.License(name=""),
   ),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
        name='token_refresh'),

    path('api/v1/', include('books.urls')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
