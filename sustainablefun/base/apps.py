from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.conf import settings

TESTING = getattr(settings, "TESTING", False)

def callback(**kwargs):
    from .seeds import populate, populate_test

    if TESTING in [True, 'True']:
        populate_test()
    else:
        populate()

class baseConfig(AppConfig):
    name = 'base'
    def ready(self):
        post_migrate.connect(callback, sender=self)
