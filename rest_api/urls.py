from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_api.views import ErrosApiViewSet, UserApiViewSet

router = routers.DefaultRouter()
router.register(r'erros', ErrosApiViewSet)
router.register(r'contas', UserApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('get_token', obtain_auth_token)
    # username e um password
]