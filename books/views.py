from rest_framework import viewsets, permissions
from .permissions import BookOwnerPermission
from dj_rql.drf import RQLFilterBackend
from .models import Author, Book
from .serializers import AuthorModelSerializer, BookModelSerializer
from .filters import AuthorFilterClass, BookFilterClass


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = AuthorFilterClass


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BookFilterClass
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions, BookOwnerPermission,]
