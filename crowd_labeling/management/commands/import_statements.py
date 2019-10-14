from django.core.management.base import BaseCommand

from crowd_labeling.models import Statement


class Command(BaseCommand):
    help = "Imports statements from a .TXT file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str)

    def handle(self, *args, **options):
        file_path = options['file_path'][0]

        data = []
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
            self.stdout.write('\r{p}% | saved {i}/{n}'.format(p=(i + 1) * 100 / n, i=i + 1, n=n), ending='')
        self.stdout.write('\ndone')
