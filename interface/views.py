from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import Context, loader

def greeting(request):
  template = loader.get_template(
  	'interface/itemlist.html')
  output = template.render()
  return HttpResponse(output)
