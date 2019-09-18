from django.http import HttpResponse


def index(request):
    return HttpResponse("I used 'typeC' instead of 'type'. Hello, I couldn't use 'type' as the name of one of the arguments in calculatePrice graph because it is a keyword, and i wasn't allowed, so i used 'typeC'. ")
    