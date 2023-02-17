from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, filters, serializers, mixins
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group
from api.serializers import (PostSerializer, GroupSerializer,
                             CommentSerializer, FollowSerializer)
from api.permissions import AuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    '''Функция представления для постов.'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    '''Функция представления для комментариев.'''
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        comments = post.comments.all()
        return comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    '''
    Функция представления для подписок.
    Только действия получения информации о подписках и их создания.
    '''
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        followings = user.follower.all()
        return followings

    def perform_create(self, serializer):
        if serializer.validated_data['following'] == self.request.user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.')
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    '''Функция представления для групп.'''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
