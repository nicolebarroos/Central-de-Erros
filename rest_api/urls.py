from django.urls import include, path, re_path
from rest_framework import routers

from rest_api.views import ErrosApiViewSet

router = routers.DefaultRouter()
router.register(r'erros', ErrosApiViewSet)

urlpatterns = router.urls