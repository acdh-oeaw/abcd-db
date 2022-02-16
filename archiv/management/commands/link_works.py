
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import Event, Work
import re


class Command(BaseCommand):
    help = 'Links works to Events'

    def handle(self, *args, **kwargs):
        print('hello')