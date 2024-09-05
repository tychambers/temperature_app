from django.contrib import admin
from .models import Test, Worldcities
from import_export.admin import ImportExportActionModelAdmin

admin.site.register(Test, ImportExportActionModelAdmin)
admin.site.register(Worldcities, ImportExportActionModelAdmin)
# Register your models here.
