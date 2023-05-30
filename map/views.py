from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, View


class MarkersMapView(TemplateView):
    template_name = "map.html"


class AddRemember(View):
    def post(self, request, pk):
        print(request.POST)
        return redirect('/')
