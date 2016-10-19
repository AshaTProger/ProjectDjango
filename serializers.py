# encoding: utf-8
from rest_framework import serializers

from test_project.models import Bar
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class BarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bar


class BarGeoSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Bar
        geo_field = "point"
