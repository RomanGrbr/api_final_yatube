from django.urls import path, include
from rest_framework import routers

from api.views import PostViewSet, CommentsViewSet, FollowViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='posts')
router.register(
    r'v1/posts/(?P<id>\d+)/comments', CommentsViewSet, basename='comments'
)
router.register(r'v1/follow', FollowViewSet, basename='follow')
router.register(r'v1/groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
