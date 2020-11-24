from rest_framework.test import APITestCase
from erros.models import Erros


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.error = Erros.objects.create(
            level='Unauthorized',
            descricao='A 401 error response indicates that the client tried to operate on a protected resource without '
                      'providing the proper authorization',
            origem='2020-07-15T18:49:39-03:00',
            eventos="401",
            categoria='Development',
            arquivar=False
        )

        self.valid_params = {
            "level": "Unauthorized",
            "descricao": "A 401 error response indicates that the client tried to operate on a protected resource "
                         "without providing the proper authorization",
            "origem": "2020-07-15T18:49:39-03:00",
            "eventos": "401",
            "categoria": "Development",
            "arquivar": False
        }

        self.invalid_params = {
            "level": " ",
            "descricao": "A 401 error response indicates that the client tried to operate on a protected resource "
                         "without providing the proper authorization",
            "origem": "2020-07-15T18:49:39-03:00",
            "eventos": "401",
            "categoria": "Development",
            "arquivar": False
        }

        self.url_error = "/api/erros/"
