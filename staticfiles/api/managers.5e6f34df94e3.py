from django.db import models
from django.contrib.auth.models import BaseUserManager,GroupManager

class GroupManager(GroupManager):
    pass

class UserManager(BaseUserManager):
    """ User Model Manager """
    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError('Users must have email Address')
        if not password:
            raise ValueError('User must have Password')
        # if not full_name:
        #     raise ValueError('User must have a full name')
        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin
        user_obj.is_active = is_active
        user_obj.save(using=self._db)

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user
       
    def create_superuser(self, email, password=None,is_admin=True):
        user = self.create_user(
            email,
            password=password,
            
            is_staff=True,
            is_admin=True
        )
        
       
        return user
