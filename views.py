# encoding: utf-8
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from test_project.models import Bar
from test_project.serializers import BarSerializer, BarGeoSerializer


def map(request):
    return render(request, 'map.html', {})


def index(request):
    return render(request, 'index.html',{})

def detail(request):
    return render(request, 'detail.html',{})


class BarView(APIView):
    template_name = ''

    def get(self, request, pk=None, format=None):
        if request.is_ajax():
            return Response({'data': 'Ajax response'})
        if pk:
            try:
                bar = Bar.objects.get(pk=pk)
                bar_serializer = BarSerializer(bar)
            except Bar.DoesNotExist:
                return Response({'detail': 'Bar was not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            bar = Bar.objects.all()
            bar_serializer = BarSerializer(bar, many=True)
        data = bar_serializer.data
        return Response({'bars': data})

    def post(self, request):
        serializer = BarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            bar = Bar.objects.all()
            bar_serializer = BarSerializer(bar, many=True)
            data = bar_serializer.data
            return Response({'bars': data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GeoJsonView(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        bar = Bar.objects.all()
        bar_serializer = BarGeoSerializer(bar, many=True)
        data = bar_serializer.data
        return Response({'bars': data})

