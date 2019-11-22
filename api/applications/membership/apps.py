from django.apps import AppConfig


class MembershipConfig(AppConfig):
    #
    # Full Python path to the application
    #
    name = 'api.applications.membership'
    #
    # label
    #
    label = 'membership'
    #
    # Application description
    #
    verbose_name = 'Memberships administration'
