from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

EXCLUDED_PATHS = [
    '/register',  # The register page
    # Add other paths or URL names as needed
]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path is in the list of excluded paths
        if request.path not in EXCLUDED_PATHS:
            if not request.user.is_authenticated:
                return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)