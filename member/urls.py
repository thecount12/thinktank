"""
blog urls
"""
# from django.conf.urls import url, include

from django.urls import path

from member.views import member_index

# from member.views import PostListView
# from blog.views import PostDetailView
# from blog.views import PostCommentView

urlpatterns = [
        path('', member_index, name='member-main'),
        # path('', PostListView.as_view(), name='post-list'),
        # path('<int:pk>', PostDetailView.as_view(), name='post-detail'),
        # path('<int:pk>/comment/', PostCommentView, name='postcomment'),
]
