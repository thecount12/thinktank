from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# from django.shortcuts import render_to_response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from signup.models import Profile


# @login_required(redirect_field_name='/login') # deprecated or old way
class MemberListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    redirect_field_name = 'next'  # to proper page
    model = User
    paginate_by = 4
    queryset = User.objects.order_by('last_name')


class MemberDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login'
    redirect_field_name = 'next'
    model = Profile


@login_required
def member_index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        user_id = request.user.id
        print(username)
        print(request.user.id)
        data = {'user': username, 'user_id': user_id}
    # return render_to_response("member.html")
    return render(request, "member.html", data)
