from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, CommentsViewSet, FollowViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<id>\d+)/comments', CommentsViewSet, basename='comments'
)
router.register(r'follow', FollowViewSet, basename='follows')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
]
