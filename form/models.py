from django.db import models

class Form(models.Model):
    email = models.EmailField(max_length=123, default=None)
    
    def __str__(self):
        return self.email


class ip(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address