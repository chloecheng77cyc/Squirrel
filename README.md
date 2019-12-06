# Group information
 - Group 57, Section 1
 - UNIs: [ss5435, yc3703]
 - Link to the 
[server](https://)
 - Link to 
[Github repository](https://github.com/chloecheng77cyc/Squirrel.git)

# Squirrel

Project Squirrel is an application to track squirrel data in Central Park, NY. The information includes location coordinates, age, primary fur color, activities, communications, and interactions between squirrels and with humans.

## Built with
- Python 3.7
- Django 2.2.7
- sqlite3 
- sqlparse 0.3.0
- html5
- Bootstrap 4
- pytz 2019.3

## Acknowledgements
- OpenStreetMaps and Leaflet for map location display

# Management commands
## Import
To import data from the [2018 Central Park Squirrel Census](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw), you need to run the following code specifying the path to the file at the command line after the name of the management command.
```python
python manage.py import_squirrel_data /path/to/file.csv
```

## Export
To export the data from your django database into a csv file, you need to run the following code specifing the path to save the csv file at the command line after the name of the management command.
```python
python manage.py export_squirrel_data /path/to/file.csv
```

# Views
## Map
 - This function shows a map that displays the location of all squirrel sightings on an OpenStreets map.
 - The link to the map is [here](https://)

## Sightings
 - This function shows the list of all squirrel sightings with links to edit and add sightings.
 - The link to Sightings is [here](https:///).
 
## Update the sighting for specific squirrels
 - This function can be used to update the information of a specific squirrel.
 - It can be called by clicking the 'edit' button beside the squirrel.
 
## Create a new sighting
 - This function can be used to create a new sighting of a squirrel.
 - The link to the creating a new sighting is [here](https://)
 
## General stats
 - This function shows the general statistics of the squirrel information in the database.
- The link to the general stats is [here](https:///)








