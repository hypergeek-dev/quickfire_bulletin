from django.http import HttpResponse

def home(request):
    return HttpResponse("This is in the qfb_main")

def test_page(request):
    return HttpResponse("This is in the qfb_main")
