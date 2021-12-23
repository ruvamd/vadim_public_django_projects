from django.db import models

class Meal(models.Model):
    """The weekly planned meals."""
    
    text = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.text
