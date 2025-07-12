from django.db import models

class Programs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    organizer = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=255, blank=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    income = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return self.title

    @property
    def balance(self):
        return self.income - self.spend
