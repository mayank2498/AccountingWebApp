from __future__ import unicode_literals

from django.db import models

class OtpData(models.Model):
    mobile = models.CharField(max_length=240, blank=False, null=False)
    otp = models.IntegerField(default=0)
    flag = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

