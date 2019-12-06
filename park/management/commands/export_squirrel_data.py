from django.core.management.base import BaseCommand,CommandError
from park.models import Squirrel
from django.http import HttpResponse

import csv
class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('csv_file')

    def handle(self,*arg,**options):
        with open(options['csv_file'],'w') as fp:
            fieldnames=['Latitude',
                    'Longitude',
                    'Unique_Squirrel_ID',
                    'Shift',
                    'Date',
                    'Age',
                    'Primary_Fur_Color',
                    'Location',
                    'Specific_Location',
                    'Running',
                    'Chasing',
                    'Climbing',
                    'Eating',
                    'Foraging',
                    'Other_Activities',
                    'Kuks',
                    'Quaas',
                    'Moans',
                    'Tail_flags',
                    'Tail_twitches',
                    'Approaches',
                    'Indifferent',
                    'Runs_from',]
            writer = csv.DictWriter(fp,fieldnames=fieldnames)
            writer.writeheader()
            squirrels=Squirrel.objects.all()
            for data in squirrels:
                writer.writerow({'Latitude':data.Latitude,
                                 'Longitude':data.Longitude,
                                 'Unique_Squirrel_ID':data.unique_squirrel_id,
                                 'Shift':data.Shift,
                                 'Date':data.Date,
                                 'Age':data.Age,
                                 'Primary_Fur_Color':data.Primary_fur_color,
                                 'Location':data.Location,
                                 'Specific_Location':data.Specific_location,
                                 'Running':data.Running,
                                 'Chasing':data.Chasing,
                                 'Climbing':data.Climbing,
                                 'Eating':data.Eating,
                                 'Foraging':data.Foraging,
                                 'Other_Activities':data.Other_activities,
                                 'Kuks':data.Kuks,
                                 'Quaas':data.Quaas,
                                 'Moans':data.Moans,
                                 'Tail_flags':data.Tail_flags,
                                 'Tail_twitches':data.Tail_twitches,
                                 'Approaches':data.Approaches,
                                 'Indifferent':data.Indifferent,
                                 'Runs_from':data.Runs_from})
