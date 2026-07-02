import re

from django.conf import settings
from django.urls import resolve

from .tagging import with_tag


request_id_header = getattr(settings, "REQUEST_ID_HEADER")
request_id_clean = re.compile("[^a-zA-Z0-9-.@_]")


class SetTagMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            resolver_match = request.resolver_match or resolve(request.path_info)
            tag = f"url={resolver_match.namespace}:{resolver_match.url_name}"
        except Exception:
            tag = "url=no-resolver-match"

        if request_id_header and request_id_header in request.headers:
            hval = request_id_clean.sub("", request.headers[request_id_header])
            tag += f" request={hval}"

        with with_tag(tag):
            return self.get_response(request)
