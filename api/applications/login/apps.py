from django.apps import AppConfig


class LoginConfig(AppConfig):
    name = 'api.applications.login'
    label = 'login'
    verbose_name = 'Credentials administration'

    def ready(self):
        from api.applications.login import signals
        #
        # Call this dummy function in signals to avoid suppression of the above import statement
        # as it can be considered as unused by PyCharm "optimize import"
        #
        signals.loaded()
