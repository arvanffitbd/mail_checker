from django.db import models

class Form(models.Model):
    email = models.EmailField(max_length=123, default=None)
    
    def __str__(self):
        return self.email