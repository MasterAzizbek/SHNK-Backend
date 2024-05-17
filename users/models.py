from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
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
    birth_date = models.DateField()
    email = models.EmailField(unique=True)
    organization = models.CharField(max_length=255)
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=70)
    degree = models.CharField(max_length=100)
    information = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='avatars')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


class PasswordResets(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)