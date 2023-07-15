from django.contrib.auth.hashers import check_password
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.db.models import Q
from typing import Optional


class Authenticate(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs) -> Optional[get_user_model()]:
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username=username) | Q(email=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None