from django.urls import include, path, re_path
from rest_framework import routers

from rest_api.views import ErrosApiViewSet, UserApiViewSet

router = routers.DefaultRouter()
router.register(r'erros', ErrosApiViewSet)
router.register(r'contas', UserApiViewSet)

urlpatterns = router.urls