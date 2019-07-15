from django.contrib import admin
from cms.models import Rsvp, Code
from cms.actions import export_as_csv_action

# Register your models here.

class RsvpList(admin.ModelAdmin):
    search_fields = ['name', 'email', 'phone', 'guest', 'attending', 'message']
    list_display = ('name', 'email', 'phone', 'guest', 'attending', 'message')

    def get_queryset(self, request):
        queryset = super(RsvpList, self).get_queryset(request)
        queryset = queryset.order_by('attending')
        return queryset

    actions = [export_as_csv_action("CSV Export", fields=['name', 'email', 'phone', 'guest', 'attending', 'message'])]

class CodeList(admin.ModelAdmin):
    model = Code

admin.site.register(Rsvp, RsvpList)
admin.site.register(Code, CodeList)
admin.site.site_header = 'LoviSatya RSVP'
