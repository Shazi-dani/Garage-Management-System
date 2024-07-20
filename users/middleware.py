from django.http import JsonResponse
from .models import BlacklistedToken

def check_blacklist(get_response):
    def middleware(request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if auth_header and ' ' in auth_header:
            token = auth_header.split(' ')[1]
        else:
            token = None  # or handle the error appropriately
        if BlacklistedToken.objects.filter(token=token).exists():
            return JsonResponse({'detail': 'Token has been blacklisted'}, status=401)
        response = get_response(request)
        return response
    return middleware
