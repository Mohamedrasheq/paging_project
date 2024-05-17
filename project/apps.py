from django.apps import AppConfig



class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'



class MyAppConfig(AppConfig):
    name = 'project'

    def ready(self):
        # Import the function and register it
        from .custom_functions import create_custom_function
        create_custom_function()

