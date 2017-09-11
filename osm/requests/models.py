from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Item(models.Model):
	itemName = models.CharField(max_length=200)
	req_date = models.DateTimeField('date requested')
	quantity = models.IntegerField(default=1)
	url = models.URLField(max_length=200)
	requester = models.CharField(max_length=200)
	def __str__(self):
		return self.itemName
