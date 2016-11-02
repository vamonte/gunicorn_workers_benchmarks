# coding=utf-8
import argparse

from django.core.management.base import BaseCommand
from test_views.models import A, B, C, D, E


class Command(BaseCommand):
    help = "Add a list of domain to a project"

    def handle(self, *args, **options):
        pass
