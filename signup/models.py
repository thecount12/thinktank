from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	editor = models.NullBooleanField(blank=True)
	subscriber = models.NullBooleanField(blank=True)
	# think tank related
	phone = models.CharField(max_length=20, blank=True)
	phone2 = models.CharField(max_length=20, blank=True)
	Address1 = models.CharField(max_length=100, blank=True)
	Address2 = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)  # add choices
	zip_code = models.CharField(max_length=15, blank=True)
	public_profile = models.NullBooleanField(blank=True)
	gender = models.CharField(max_length=7, blank=True)
	howHeard = models.CharField(max_length=100, blank=True)
	industry = models.CharField(max_length=100, blank=True)
	hasKids = models.NullBooleanField(blank=True)
	emergencyName = models.CharField(max_length=100, blank=True)
	emergencyRelation = models.CharField(max_length=100, blank=True)
	emergencyPhone = models.CharField(max_length=20, blank=True)
	emergencyEmail = models.CharField(max_length=100, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()
