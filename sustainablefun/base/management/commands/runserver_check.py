"""
Includes prospector with runserver, command : $python manage.py runserver_check

file needs to be present in one of django app in following location: <your app name>/management/commands/runserver_check.py

´<your app name>´ should be present installed apps
"""
import subprocess
from multiprocessing import Process
from time import sleep
from django.contrib.staticfiles.management.commands.runserver import Command as StaticfilesRunserverCommand

def printcounter():
    print("\n****************************************")
    for i in range(5, -1, -1):
        print(f"Prospector will be ready in (about) {i} seconds!", end = '\r')
        sleep(1)

class Command(StaticfilesRunserverCommand):
    help = "Starts a lightweight Web server for development, serves static files and does some custom fancy stuff."

    def run_prospector(self):
        """Runs prospector on codebase with a subprocess, while start a counter
        on another so server can get running while prospector check .py files"""
        subprocess.Popen(['prospector'])
        p = Process(target=printcounter)
        p.start()

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def get_handler(self, *args, **options):
        """Overriden get handler method, call run_prospector for static analysis of code
        """
        handler = super(Command, self).get_handler(*args, **options)
        self.run_prospector()
        return handler