from django.core.management.base import BaseCommand

from park.models import Sighting

import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *arg, **options):
        import datetime
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            
            counter=0

            for item in data:
                sighting=Sighting(
                    Latitude=item['Y'],
                    Longitude=item['X'],
                    unique_squirrel_id=item['Unique Squirrel ID'],
                    Shift=item['Shift'],
                    Date=item['Date'],
                    Age=item['Age'],
                    Primary_Fur_Color=item['Primary Fur Color'],
                    Location=item['Location'],
                    Specific_Location=item['Specific Location'],
                    Running=item['Running'],
                    Chasing=item['Chasing'],
                    Climbing=item['Climbing'],
                    Eating=item['Eating'],
                    Foraging=item['Foraging'],
                    Other_Activities=item['Other Activities'],
                    Kuks=item['Kuks'],
                    Quaas=item['Quaas'],
                    Moans=item['Moans'],
                    Tail_flags=item['Tail flags'],
                    Tail_twitches=item['Tail twitches'],
                    Approaches=item['Approaches'],
                    Indifferent=item['Indifferent'],
                    Runs_from=item['Runs from'],
                    )

                sighting.save()
