from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from django.contrib.auth.models import User


class MemberListView(ListView):
    model = User
    paginate_by = 4
    queryset = User.objects.order_by('last_name')


@login_required
def member_index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        data = {'user': username}
    # return render_to_response("member.html")
    return render(request, "member.html", data)
