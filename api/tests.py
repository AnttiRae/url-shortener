from django.test import TestCase
from django.urls import reverse
from .models import Link
# Create your tests here.


class APIEndPointsTestCase(TestCase):
    def setUp(self):
        Link.objects.create(
            original_url='https://www.testeriesteri.com/testeri',
            url_hash='102549103d'
        )

    def test_url_encoding(self):
        request_data = {
            'url': 'https://www.testeriesteri.com/loremipsumdolor'
        }
        response = self.client.post(reverse('encode'), request_data, content_type='application/json', SERVER_NAME="testserver.com")
        self.assertJSONEqual(
            response.content.decode('utf-8'),
            {'short_url': 'http://testserver.com/d1eb24c401'}
        )

    def test_invalid_url_encoding(self):
        request_data = {
            'url': 'steriesteri/loremipsumdolor'
        }
        response = self.client.post(reverse('encode'), request_data, content_type='application/json', SERVER_NAME="testserver.com")
        self.assertJSONEqual(
            response.content.decode('utf-8'),
            '{"error": {"url": ["Enter a valid URL."]}}'
        )

    def test_invalid_json_input(self):
        request_data = None
        response = self.client.post(reverse('encode'), request_data, SERVER_NAME="testserver.com")
        self.assertJSONEqual(
            response.content.decode('utf-8'),
            '{"error": "Invalid JSON"}'
        )

    def test_url_decoding(self):
        request_data = {
            'short_url': 'http://testserver.com/102549103d'
        }
        response = self.client.post(reverse('decode'), request_data, content_type='application/json', SERVER_NAME="testserver.com")
        self.assertJSONEqual(
            response.content.decode('utf-8'),
            '{"original_url": "https://www.testeriesteri.com/testeri"}'
        )

