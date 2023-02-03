from django.shortcuts import get_object_or_404, redirect
from django.views import View
from api.models import Link

# Create your views here.


class RequestRedirectView(View):

    @staticmethod
    def get(request, **kwargs):
        url_hash = kwargs.get('url_hash')
        link = get_object_or_404(Link, url_hash=url_hash)
        return redirect(link.original_url)
