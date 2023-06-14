from django.db import models

# Create your models here.

class Email(models.Model):
    email_pk = models.AutoField(primary_key=True)
    email_id = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    composedEmail = models.CharField(max_length=5000)

    def __str__(self):
        return self.email_id
