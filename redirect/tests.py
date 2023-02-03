from django.test import TestCase
from django.urls import reverse

from api.models import Link
# Create your tests here.


class APIEndPointsTestCase(TestCase):
    def setUp(self):
        Link.objects.create(
            original_url='https://www.testeriesteri.com/testeri',
            url_hash='102549103d'
        )

    def test_redirect(self):
        response = self.client.get(reverse('redirect', kwargs={'url_hash': '102549103d'}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'https://www.testeriesteri.com/testeri')
