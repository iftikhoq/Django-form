from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    feedback = models.TextField()
    fdate = models.DateField() 
    type = models.CharField(max_length=255)
    file = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    terms = models.BooleanField()

    def __str__(self):
        return f'{self.name}: {self.type}'
