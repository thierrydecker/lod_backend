from django.apps import AppConfig


class WorkspaceConfig(AppConfig):
    #
    # Full Python path to the application
    #
    name = 'api.applications.workspace'
    #
    # label
    #
    label = 'workspace'
    #
    # Application description
    #
    verbose_name = 'Workspaces administration'
