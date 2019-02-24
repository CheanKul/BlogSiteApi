import graphene
from graphene_django.types import DjangoObjectType
from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class Query(object):
    Post = graphene.Field(PostType,
                          id=graphene.String(),
                          Header=graphene.String())
    all_Posts = graphene.List(PostType)

    def resolve_all_Posts(self, info, **kwargs):
        return Post.objects.all()

    def resolve_Post(self, info, **kwargs):
        id = kwargs.get('id')
        Header = kwargs.get('Header')

        if id is not None:
            return Post.objects.get(pk=id)

        if Header is not None:
            return Post.objects.get(Header=Header)

        return None
