from django.contrib.auth.hashers import BCryptSHA256PasswordHasher


class MyBCryptSHA256PasswordHasher(BCryptSHA256PasswordHasher):
    prefix = b'2a'
