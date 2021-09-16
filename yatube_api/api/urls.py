from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions

from django.conf.urls import url

from api.views import PostViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'groups', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]
