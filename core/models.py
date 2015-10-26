from django.db import models
VISIBILITY_CHOICES = (
(0, 'Dr.'),
(1, 'Mr.'),
(2, 'Mrs.'),
(3, 'Miss'),
)
# Create your models here.
class Contact(models.Model):
  title = models.IntegerField(choices=VISIBILITY_CHOICES, default=0)
  first_Name = models.CharField(max_length=300, default="")
  last_Name = models.CharField(max_length=300, default="")
  email_Address = models.CharField(max_length=300, default="")
  message = models.TextField(max_length=300, default="")
  created_at = models.DateTimeField(auto_now_add=True)

class About(models.Model):

  def __unicode__(self):
    return self.first_Name