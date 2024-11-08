from django.db import models
from django.urls import reverse

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = "Food Items"