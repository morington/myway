from typing import Optional

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models import Model
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, login: str, first_name: str, last_name: str, password: str = None, **extra_fields) -> "User":
        if not login:
            raise ValueError('User must have a login')

        user = self.model(
            login=login,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login: str, first_name: str, last_name: str, password: str, **extra_fields) -> "User":
        user = self.create_user(
            login=login,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        db_table = 'Пользователи'
        verbose_name = 'ПОЛЬЗОВАТЕЛЬ'
        verbose_name_plural = 'ПОЛЬЗОВАТЕЛИ'
        ordering = ['-created_at']

    email = models.EmailField(unique=True, blank=True, null=True, verbose_name='E-mail')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    login = models.CharField(max_length=50, verbose_name='Логин', unique=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    is_active = models.BooleanField(default=True, verbose_name='Активность уч. записи')
    is_admin = models.BooleanField(default=False, verbose_name='Является персоналом')

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    @property
    def is_staff(self) -> bool:
        return self.is_admin

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm: Permission, obj: Optional[Model] = None) -> bool:
        return self.is_staff

    def has_module_perms(self, app_label: str) -> bool:
        return self.is_staff

    def get_all_permissions(self):
        if self.is_staff:
            return set()
