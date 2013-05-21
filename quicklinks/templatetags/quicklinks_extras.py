from django.core.management import setup_environ
from django import template
#from quicklinks import settings
from django.template import loader, Context
from quicklinks.models import QuickLinkGroup, QuickLink
#from quicklinks.views import index
register = template.Library()



#parse tag
def do_quicklinks(parser,context):
    return QuicklinksNode()

#write the tag
class QuicklinksNode(template.Node):

    def __init__(self):
        pass


    def render(self, context):

        listed_groups = QuickLinkGroup.objects.all().order_by('id')#.values('title', 'group__title', 'group__url')
        listed_links = QuickLink.objects.all().select_related('quicklinkgroup_id')
        html = ''
        if listed_groups:
           html+= '<div id="quicklinks_wrap"><h3>Quick Links</h3><a href="#"> Show Links</a><ul id="first">'
           for group in listed_groups:
            html+= '<ul id="second"><strong>' #+ group.order_int#
            html+=  '&nbsp;' + group.title + '</strong>'
            if listed_links:
             for links in listed_links:
              if links.quicklinkgroup_id == group.id:
                html+= '<li><a href="' + links.url + '">' + links.title + '</a></li>'
            html+= '</ul>'
           html+= '</ul></div>'
        else:
            html+= '<p>No quick links available.</p>'
        return html

#register the tag
register.tag("quicklink_group", do_quicklinks)
