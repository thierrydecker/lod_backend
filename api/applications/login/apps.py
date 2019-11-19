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
    #
    # Application description
    #
    verbose_name = 'Credentials administration'

    def ready(self):
        from api.applications.login import signals
        #
        # Call this dummy function in signals to avoid suppression of the above import statement
        # as it can be considered as unused by PyCharm "optimize import"
        #
        signals.loaded()
