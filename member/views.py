from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def member_index(request):
    return render_to_response("member.html")
