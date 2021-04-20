from django.apps import AppConfig


class MdmusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MDMusers'

    def ready(self):
        import MDMusers.signals