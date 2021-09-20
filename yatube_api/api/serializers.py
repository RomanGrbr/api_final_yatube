from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Post, Follow, Group, User


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    # def validate(self, data):
    #     if data['following'] == data['username']:
    #         raise ValidationError('Нельзя подписаться на себя')

    class Meta:
        fields = ('user', 'following')
        model = Follow

    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message='Такая подписка уже существует'
        )
    ]


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group
