from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse,Http404
from quicklinks.models import QuickLinkGroup, QuickLink
#from django.core import serializers
from django.template import Context, loader
import simplejson as json
from .lib.flexible_json import json_response_from
from django.template import Context, Template


def indexAlt(request):

    listed_groups = QuickLinkGroup.objects.all().order_by('id')#.values('title', 'group__title', 'group__url')
    listed_links = QuickLink.objects.all().select_related('quicklinkgroup_id')
    #template = loader.get_template("index.html")

    context = {

        "listed_groups": listed_groups,
        "listed_links": listed_links
    }

    return render(request, 'index.html', context)


def home(request):
    return render_to_response(u'default.html')


def links(request):
    link_groups = QuickLinkGroup.objects.all().select_related('group_set').order_by('id')#gets list of objects
    response = link_groups
    return json_response_from(response, related=['group'], ignored = ['quicklinkgroup', 'quicklinkgroup_id'])
