# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth.models import User
#
# from authapp.models import CustomUser
#
#
# class CaseInsensitiveModelBackend(ModelBackend):
#     def authenticate(self, username, password, request):
#         try:
#             user = CustomUser.objects.get(username__iexact=username)
#         except CustomUser.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user