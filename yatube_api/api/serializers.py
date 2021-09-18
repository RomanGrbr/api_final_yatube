from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Follow, Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('author', 'post', 'text', 'created')
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = ('text', 'pub_date', 'author', 'group')
        model = Post


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('user', 'following')
        model = Follow


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'slug', 'description')
        model = Group
