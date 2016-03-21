from django.http import HttpResponse


# TODO Create proper response


def index(request):
    return HttpResponse("Hello World!")
