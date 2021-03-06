"""
This doesn't really belong here, but you can't create
commands at the main config package :(.
"""
import sys

from django.core.management.commands import runserver

from honcho.manager import Manager


class Command(runserver.Command):
    help = 'Runs the devserver with all dependencies'

    def handle(self, *args, **options):
        m = Manager()
        m.add_process('web', './manage.py runserver')
        m.add_process('celery', 'celery -A config worker --beat -l info')
        m.loop()

        sys.exit(m.returncode)
