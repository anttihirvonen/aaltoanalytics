# Create your views here.
from django.http import HttpResponse

def development_index(request):
    return HttpResponse("works")
