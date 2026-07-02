from django.apps import AppConfig


class PluginApp(AppConfig):
    default = True
    name = "django_querytagger"
    verbose_name = "Query tagger"

    def ready(self):
        from . import signals  # NOQA
