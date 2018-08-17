from django.contrib import admin
from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _
from django.utils.text import force_text
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . import models


class StorageInline(admin.StackedInline):
    model = models.storage_locations
    extra = 1
    fields = ["edit_location", "location"]
    readonly_fields = ["edit_location"]

    def edit_location(self, obj=None):
        if obj.pk:
            url = urlresolvers.reverse("""
                                       admin:%s_%s_change
                                       """ % (obj._meta.app_label,
                                              obj._meta.model_name),
                                       args=[force_text(obj.pk)])
            return """
                   <a href="{url}">{text}</a>
                   """.format(
                            url=url,
                            text=_("""
                                   Edit this %s separately
                                   """) % (obj._meta.verbose_name))
        return _("(save and continue editing to create a link)")

    edit_location.short_description = _("Edit link")
    edit_location.allow_tags = True


@admin.register(models.departments)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ['department']
    inlines = [StorageInline]


class CountDivisionInline(admin.StackedInline):
    model = models.count_division
    extra = 1
    fields = ["item_name", "item_count"]


@admin.register(models.storage_locations)
class LocationAdmin(admin.ModelAdmin):
    fields = ["location", "department"]
    inlines = [CountDivisionInline]


class InventoryResources(resources.ModelResource):

    class Meta:
        model = models.inventory


class InventoryTotal(ImportExportModelAdmin):
    list_display = ('__str__', 'item', 'item_total_count', 'item_department')
    search_fields = ('item',)
    resource_class = InventoryResources


admin.site.register(models.inventory, InventoryTotal)
# admin.site.register(models.issue_application)
