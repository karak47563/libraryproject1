text (# Create your views here.) from views.py and instead insert this content:
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world!")
