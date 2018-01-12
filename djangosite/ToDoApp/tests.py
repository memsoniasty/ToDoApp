from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import AnonymousUser, User

from .views import index


class StatusTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="Mick", email="mickey@m0ck.com", password="")

    def test_index_anonymous(self):
        request = self.factory.get('/index')
        request.user = AnonymousUser()

        resp = index(request)

        self.assertEqual(resp.status_code, 200)

    def test_index_user(self):
        request = self.factory.get('/index')
        request.user = self.user

        resp = index(request)

        self.assertEqual(resp.status_code, 200)


# class ClientTest(TestCase):
#
#     def setUp(self):
#         pass
#
#     def test_mozilla5(self):
#         c = Client(HTTP_USER_AGENT='Mozilla/5.0')
#         resp = c.get('index')
#         self.assertEqual(resp.status_code, 200)
