from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render_to_response


@login_required
def member_index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        data = {'user': username}
    # return render_to_response("member.html")
    return render(request, "member.html", data)