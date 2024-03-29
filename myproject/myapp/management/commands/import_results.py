# In your app's management/commands directory, create a Python file, e.g., import_csv.py

import csv
from django.core.management.base import BaseCommand
from myapp.models import *  # Import your model


class Command(BaseCommand):
    help = 'Import data from CSV file into database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Open the CSV file and read its contents
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Assuming your CSV columns match your model fields,
                # you can create instances of your model and save them to the database
                obj = RESULTS(
                    Date=row['Date'],
                    Team_1=row['Team_1'],
                    Team_2=row['Team_2'],
                    Winner=row['Winner'],
                    Margin=row['Margin'],
                    Ground=row['Ground'],

                    # Add more fields as needed
                )
                obj.save()

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))