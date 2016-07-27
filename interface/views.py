from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import Context, loader

from interface.models import Item

import datetime

def show_itemlist(request):
  text = request.GET.get('text', '')
  if text != '':
    Item.objects.create(text=text,
     created=datetime.date.today(),
     isFinished=False,
     finished=datetime.date.today())

  items = Item.objects.all()

  template = loader.get_template(
  	'interface/itemlist.html')
  output = template.render({'items': items})
  return HttpResponse(output)
