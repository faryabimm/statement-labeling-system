import json
from json.decoder import JSONDecodeError

from django.core.management.base import BaseCommand

from crowd_labeling.models import Statement


class Command(BaseCommand):
    help = "Imports Statements from a .JL file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str)

    def handle(self, *args, **options):
        file_path = options['file_path'][0]

        data = []
        try:
            with open(file_path) as f:
                for line in f:
                    for item in json.loads(line)['items']:
                        data.append(item['content'])
        except JSONDecodeError:
            with open(file_path) as f:
                for line in f:
                    data.append(line.strip())

        self.stdout.write('delete all previous statements')
        Statement.objects.all().delete()
        self.stdout.write('add all new statements')
        n = len(data)
        for i, record in enumerate(data):
            statement = Statement(text=record)
            statement.save()
            self.stdout.write('\rsaved {i} out of {n}'.format(i=i + 1, n=n), ending='')
        self.stdout.write('\ndone')
