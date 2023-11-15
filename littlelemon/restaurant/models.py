from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, null=True, default=None)
    No_of_guests = models.IntegerField(default=0)
    Bookingdate = models.DateTimeField()
    
    class Meta:
        db_table = "Booking"
    
class Menu(models.Model):
    ID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(default=0)
    
    class Meta:
        db_table = "Menu"    