from django.db import models
from django.urls import reverse # reverse used to generate URLs by reversing the URL patterns
import uuid

# Create your models here.
#class User(models.Model):
#    """Model representing a user."""
#    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique identifier for user')
#    username = models.EmailField(help_text='Email address')
#    verified = models.BooleanField(default=False, help_text='If True, user has been verified via email') 

class Category(models.Model):
    """Model representing a pomodoro category."""
    name = models.CharField(max_length=100, help_text='Enter the pomodoro category')
    categoryID = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, help_text='Unique identifier for category')
    description = models.TextField(max_length=250, default="", help_text='Brief description')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def display_category(self):
        """Create a string for the Category. This is required to display category in Admin."""
        return ', '.join(category.name for category in self.category.all()[:3])

    def get_absolute_url(self):
        """Returns the url to access a detail record for this category."""
        return reverse('category-detail', args=[str(self.id)])

    display_category.name = 'Category'




class Pomodoro(models.Model):
    """Model representing a pomodoro (but not specific pomodoro)."""
    task_name = models.TextField(blank=False, help_text='Enter task name for pomodoro')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, help_text='Unique ID for this particular pomodoro across whole library')

    # Foreign Key used bc pomodoro can only have one category but a category can have multiple pomodoros.
    categoryID = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    day_of_week = models.CharField(max_length=10, help_text='Day of week (i.e. Monday-Sunday)')
    time_of_day = models.DateTimeField(help_text='XX:XX AM or PM')
    minutes = models.IntegerField(default=25)    
 
    def __str__(self):
        """String for representing the Model object."""
        return self.task_name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this pomodoro."""
        return reverse('pomodoro-detail', args=[str(self.id)])
