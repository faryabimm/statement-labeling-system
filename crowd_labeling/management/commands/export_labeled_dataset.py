import pandas as pd
from django.core.management.base import BaseCommand

from crowd_labeling.models import Label


class Command(BaseCommand):
    help = "Exports crowed-labeled statements to a .CSV file"

    def add_arguments(self, parser):
        parser.add_argument('output', nargs=1, type=str)

    def handle(self, *args, **options):
        file_path = options['output'][0]

        self.stdout.write('retrieve labeled data.')
        labeled_statements = Label.objects.all()
        self.stdout.write('process labeled data.')
        data = []
        for record in labeled_statements:
            data.append({
                'user': record.user.username,
                'time': record.answer_time,
                'label': record.label,
                'statement': record.statement.text,
            })

        data_frame = pd.DataFrame(data)

        self.stdout.write('write to file.')
        data_frame.to_csv(file_path, index=False)
        self.stdout.write('done.')
