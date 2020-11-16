from django.contrib import admin

from import_export.admin import ImportExportActionModelAdmin

from .models import Medication

# Register your models here.


class MedicationAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(Medication, MedicationAdmin)
