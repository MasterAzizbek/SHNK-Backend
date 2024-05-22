from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email maydoni to\'ldirilishi kerak')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=255)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=500)
    degree = models.CharField(max_length=100)
    information = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='files/avatars')
    is_reviewer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_all_permissions(self, obj=None):
        return []

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def str(self) -> str:
        return self.email


class PasswordResets(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)
