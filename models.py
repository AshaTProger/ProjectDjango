from django.contrib.gis import geos
from django.contrib.gis.db import models


class Bar(models.Model):
    name = models.CharField(max_length=256)
    capacity = models.IntegerField()
    address = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    point = models.PointField(blank=True, null=True)

    class Meta:
        verbose_name = 'Bar'
        verbose_name_plural = 'Bars'

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.point = geos.Point(self.longitude, self.latitude)
        return super(Bar, self).save(*args, **kwargs)
