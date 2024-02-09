from django.contrib import admin
from .models import Command, Participant


class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 1


class CommandAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]


admin.site.register(Command, CommandAdmin)
admin.site.register(Participant)
