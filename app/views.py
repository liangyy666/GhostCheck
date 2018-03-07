# coding:utf-8

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Chapter
import copy

def home(request):

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        ghosts = Chapter.objects.filter(fight_ghost__icontains=q)
        tmp = dict()
        for go in ghosts:
            if tmp.get(go.chapter_name):
                tmp[go.chapter_name].append(go.ghost_name + " ： " + go.fight_ghost.replace(q,'<em style = "color:red">'+q+'</em>'))
            else:
                tmp[go.chapter_name] = []
                tmp[go.chapter_name].append(go.ghost_name + " ： " + go.fight_ghost.replace(q,'<em style = "color:red">'+q+'</em>'))

        # 整理格式，模板中不能使用dict
        li = []
        for k,v in tmp.items():
            tmp_li = []
            tmp_li.append(k)
            for vv in v:
                tmp_li.append(vv)

            li.append(tmp_li)


        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
                'ghosts':li
            })
    else:
        return render(            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
                'ghosts':None
            })

    

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
