from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from quicklinks.models import QuickLinkGroup
from quicklinks.models import QuickLink

from adminsortable.admin import SortableAdmin
from adminsortable.admin import SortableTabularInline

#admin.site.register(QuickLinkGroup)
#admin.site.unregister(User)
#admin.site.unregister(Group)


#class QuickLinkInline(admin.TabularInline):
class QuickLinkInline(SortableTabularInline):
    model = QuickLink
    fk_name = 'quicklinkgroup'


#class QuickLinkGroupInline(admin.ModelAdmin):
class QuickLinkGroupInline(SortableAdmin):
    model = QuickLinkGroup
    inlines = (QuickLinkInline,)

admin.site.register(QuickLinkGroup,QuickLinkGroupInline)
#admin.site.register(User)
#admin.site.register(Group)
