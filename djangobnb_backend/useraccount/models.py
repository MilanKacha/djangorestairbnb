import uuid  # use for generate unique id 
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
from django.db import models


# modal for how to creat user and super user

class CustomUserManager(UserManager):
    def _create_user(self, name, email, password, **extra_fields):
        print(">>> _create_user called")
        print(">>> Input name:", name)
        print(">>> Input email:", email)
        # print(">>> Extra fields:", extra_fields)
        if not email:
            raise ValueError("You have not specified a valid e-mail address")
    
        email = self.normalize_email(email)  # automatic validation for email
        user = self.model(email=email, name=name, **extra_fields)  #Create a new User instance with the given email and name.
        user.set_password(password)  #Securely hashes the password
        user.save(using=self.db)    

        return user
    
    #  helper function for create user 
    def create_user(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, email, password, **extra_fields)
    
    # helper function for create 
    def create_superuser(self, name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField(upload_to='uploads/avatars')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()  # Attech your custom user manager in to USER modal

    USERNAME_FIELD = 'email' # Tells Django to use email instead of username to authenticate.
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name',] # REQUIRED_FIELDS are required when creating a superuser via createsuperuser.

    def avatar_url(self):
        if self.avatar:
            return f'{settings.WEBSITE_URL}{self.avatar.url}'
        else:
            return ''

