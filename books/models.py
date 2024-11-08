from django.db import models
import uuid
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self):
        self.delete = True
        self.save()


class BaseModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Author(BaseModel):
    name = models.CharField(max_length=100)
    objects = BaseModelManager()

    class Meta:
        ordering = ['name']
        verbose_name = 'Autore'

    def __str__(self):
        return self.name


class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    resume = models.TextField(max_length=500, blank=True, null=True)
    creation_date = models.DateField()
    update_date = models.DateField(blank=True, null=True)
    objects = BaseModelManager()

    class Meta:
        ordering = ['title']
        verbose_name = 'Livro'

    def __str__(self):
        return self.title
