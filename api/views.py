from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import hashlib
from .serializers import EncodeJsonSerializer, DecodeJsonSerializer
from .models import Link
from django.utils.decorators import method_decorator
import json


@method_decorator(csrf_exempt, name='dispatch')
class EncodeUrlView(View):

    @staticmethod
    def post(request):
        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON'
            }, status=400)
        valid_data = EncodeJsonSerializer(data=request_data)
        if not valid_data.is_valid():
            return JsonResponse({
                'error': valid_data.errors
            }, status=400)
        url_hash = hashlib.sha256(valid_data.data['url'].encode('utf-8')).hexdigest()[:10]
        link, created = Link.objects.get_or_create(
            original_url='https://www.google.com',
            url_hash=url_hash
        )
        return JsonResponse({
            'short_url': request.build_absolute_uri(f'/{link.url_hash}')
        })


@method_decorator(csrf_exempt, name='dispatch')
class DecodeUrlView(View):

    @staticmethod
    def post(request):
        try:
            request_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON'
            }, status=400)
        valid_data = DecodeJsonSerializer(data=request_data)
        if not valid_data.is_valid():
            return JsonResponse({
                'error': valid_data.errors
            })
        url_hash = valid_data.data['short_url'].split('/')[-1]
        link = get_object_or_404(Link, url_hash=url_hash)
        return JsonResponse({
            'original_url': link.original_url
        })
