from rest_framework.test import APITestCase
from erros.models import Erros


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.erros = Erros.objects.create(
            #id= 1,
            level='TesteApi',
            descricao='Produção',
            origem= '2020-07-15T18:49:39-03:00',
            eventos= "404",
            categoria= 'Produção',
            arquivar= False
        )

        self.valid_params = {
            "level": "Teste",
            "descricao": "Desenvolvimento",
            "origem": "2020-07-15T18:49:39-03:00",
            "eventos": "403",
            "categoria": "Desenvolvimento",
            "arquivar": False
        }

        self.invalid_params = {
            "level": " ",
            "descricao": "Desenvolvimento",
            "origem": "2020-07-15T18:49:39-03:00",
            "eventos": "403",
            "categoria": "Desenvolvimento",
            "arquivar": False
        }

        self.url_erros = "/api/erros/"
