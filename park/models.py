from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    Latitude = models.FloatField(
        help_text = _('latitude of sighting'),
    )


    Longitude = models.FloatField(
        help_text = _('longitude of sighting'),
    )


    unique_squirrel_id = models.CharField(
        primary_key=True,
        max_length=32,
        help_text=_("Unique squirrel id.")
    )

    PM = 'pm'
    AM = 'am'
    
    Shift_CHOICES = (
        (PM, 'PM'),
        (AM, 'AM'),
    )


    Shift = models.CharField(
        max_length=2,
        choices=Shift_CHOICES,
        default=AM,
        help_text=_("Sighting session"),
    )
 

    Date = models.DateField(
        help_text = _("Sighting date in YYYY-MM-DD format"),
    )
    
    
    ADULT = 'adult'
    JUVENILE = 'juvenile'

    Age_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'Juvenile'),
        ('', ''),
    )

    Age = models.CharField(
        max_length=16,
        choices=Age_CHOICES,
        default=ADULT,
        help_text=_("Age of Squirrel"),
        null=True,
        blank=True,
    )
    

    GRAY="gray"
    BLACK="black"
    CINNAMON="cinnamon"
                
    FUR_CHOICES=(
        (GRAY,"Gray"),
        (BLACK,"Black"),
        (CINNAMON,"Cinnamon"),
        ('',''),
    )
                        
    
    Primary_Fur_Color = models.CharField(
        max_length=16,
        choices=FUR_CHOICES,
        default=GRAY,
        help_text=_("Fur color of Squirrel"),
        null=True,
        blank=True,
    )

    
    
    GROUND_PLANE="ground_plane"
    ABOVE_GROUND="above_ground"
            
    LOC_CHOICES=(
        (GROUND_PLANE,"Ground_Plane"),
        (ABOVE_GROUND,"Above_Ground"),
        ('','')
    )
                    
    Location = models.CharField(
        max_length=20,
        choices=LOC_CHOICES,
        default=GROUND_PLANE,
        help_text=_("Location of Squirrel"),
        null=True,
        blank=True,
    )
                        

    Specific_location = models.CharField(
        max_length=20,
        help_text=_("Specific location of Squirrel"),
        null=True,
        blank=True,
    )

    
    Running = models.BooleanField(
        default=False,
    )
        
    Chasing = models.BooleanField(
        default=False,
    )
            
    Climbing = models.BooleanField(
        default=False,
    )
                
    Eating = models.BooleanField(
        default=False,
    )
                    
    Foraging = models.BooleanField(
        default=False,
    )
                        
    Other_activities = models.CharField(
        max_length=20,
        help_text=_("Other activity"),
        null=True,
        blank=True,
    )
                            
    Kuks = models.BooleanField(
        default=False,
    )
                                
    Quaas = models.BooleanField(
        default=False,
    )
                                    
    Moans = models.BooleanField(
        default=False,
    )

    Tail_flags = models.BooleanField(
        default=False,
    )
                                            
    Tail_twitches = models.BooleanField(
        default=False,
    )
                                                
    Approaches = models.BooleanField(
        default=False,
    )
                                                    
    Indifferent = models.BooleanField(
        default=False,
    )
                                                        
    Runs_from = models.BooleanField(
        default=False,
    )






# Create your models here.
