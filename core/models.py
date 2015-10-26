from django.db import models

# Create your models here.
class Contact(models.Model):
  first_Name = models.CharField(max_length=300, default="")
  last_Name = models.CharField(max_length=300, default="")
  email_Address = models.CharField(max_length=300, default="")
  message = models.TextField(max_length=300, default="")
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.first_Name, self.last_Name, self.email_Address, self.message