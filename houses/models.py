from django.db import models

# Create your models here.
class Hosuse(models.Model):
    title = models.CharField(max_length=100)  # House name/title
    description = models.TextField(blank=True)  # Optional details about the house
    image = models.ImageField(upload_to='hosuses/', blank=True, null=True)  # Optional house image
    date_posted = models.DateTimeField(auto_now_add=True)  # When the house was added

    head_of_house = models.CharField(max_length=100)  # Name of head of the family
    total_members = models.PositiveIntegerField()  # Number of members in the house
    contact_number = models.CharField(max_length=15, blank=True)  # Optional

    address = models.TextField(blank=True)  # Optional full address or street
    zone = models.CharField(max_length=100, blank=True)  # Optional: area or zone in mahal

    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return self.title