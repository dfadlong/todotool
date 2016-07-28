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
  done = request.GET.get('done', '')
  if done != '':
    itemDone = Item.objects.get(id=done)
    itemDone.isFinished = True
    itemDone.finished = datetime.date.today()
    itemDone.save()

  items = Item.objects.filter(isFinished=False)

  template = loader.get_template(
  	'interface/itemlist.html')
  output = template.render({'items': items, 'isArchive': False})
  return HttpResponse(output)

def show_archive(request):
  items = Item.objects.filter(isFinished=True)

  template = loader.get_template(
    'interface/itemlist.html')
  output = template.render({'items': items, 'isArchive': True})
  return HttpResponse(output)
