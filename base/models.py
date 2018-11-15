from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django.db.models import Model, EmailField, TextField, Manager, CharField


class Company(Model):
    name = CharField(
        blank=True,
        max_length=255
    )
    email = EmailField(
        verbose_name='email address',
        max_length=255,
        db_index=True,
    )
    domain = CharField(
        verbose_name='domain',
        blank=True,
        max_length=255
    )


    objects = Manager()

    def __str__(self):
        return self.name


@admin.register(Company)
class SilentAdmin(ModelAdmin):

    def log_addition(self, request, object, message):
        pass

    def log_change(self, request, object, message):
        pass

    def log_deletion(self, request, object, object_repr):
        pass