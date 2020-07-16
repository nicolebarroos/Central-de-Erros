from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token
from rest_api.views import ErrosApiViewSet, UserApiViewSet, CategoriaList, ErrosOrderList, ErrosShearch, ArquivadosList

router = routers.DefaultRouter()
router.register(r'erros', ErrosApiViewSet)
router.register(r'contas', UserApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/login', include('rest_framework.urls')),
    path('get_token', obtain_auth_token),
    path('categorias/', CategoriaList.as_view()),
    path('ordenar/', ErrosOrderList.as_view()),
    path('buscar/', ErrosShearch.as_view()),
    path('arquivados/', ArquivadosList.as_view())
    # username e um password
]
