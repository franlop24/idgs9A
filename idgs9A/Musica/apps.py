from django.apps import AppConfig


class MusicaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Musica'

class ServicesConfig(AppConfig):
    name = 'services'
    verbose_name = 'Gestor de musica'

