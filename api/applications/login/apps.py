from django.apps import AppConfig


class LoginConfig(AppConfig):
    #
    # Full Python path to the application
    #
    name = 'api.applications.login'
    #
    # label used in AUTH_USER_MODEL
    #
    label = 'login'
