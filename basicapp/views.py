from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response


def index(request):
    return render_to_response("index.html")


def calendar(request):
    return render_to_response("calendar.html")


def faq(request):
    return render_to_response("faq.html")
