from django.db import models
from adminsortable.models import Sortable



# Create your models here.
#class QuickLinkGroup(models.Model):
class QuickLinkGroup(Sortable):

    class Meta(Sortable.Meta):
        pass

    title = models.CharField(max_length=150)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    order_int = models.IntegerField()

    def groups_list(self):
        group_list = QuickLinkGroup.objects.all().select_related('group_set').order_by('id').values('title', 'group__title', 'group__url')
        return group_list



#class QuickLink(models.Model):
class QuickLink(Sortable):

    class Meta(Sortable.Meta):
        pass

    quicklinkgroup = models.ForeignKey(QuickLinkGroup, related_name="group")
    title = models.CharField(max_length=150)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    url = models.CharField(max_length=250)



