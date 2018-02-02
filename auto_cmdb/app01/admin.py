# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# _*_coding:utf-8_*_
from django.contrib import admin
import models

from daterange_filter.filter import DateRangeFilter
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ServerResource(resources.ModelResource):
    class Meta:
        model = models.Server


class AssetResource(resources.ModelResource):
    class Meta:
        model = models.Asset


# Register your models here.

class AssetAdmin(ImportExportModelAdmin):
    resource_class = AssetResource
    list_display = ('id', 'device_type', 'name', 'hostname', 'business_unit', 'admin', 'idc', 'cabinet_num', 'status')
    list_filter = ('idc', 'business_unit', 'status', 'device_type')
    search_fields = ['hostname', 'id']
    # raw_id_fields = ("server_device","network_device")


class ServerAdmin(ImportExportModelAdmin):
    resource_class = ServerResource
    readonly_fields = ('update_at',)
    # list_display=('asset','from_idc','sn','cpu_count','cpu_model','ram_size','manufactory','model','update_at')
    list_display = (
    'asset', 'sn', 'from_idc', 'cpu_count', 'cpu_model', 'ram_size', 'manufactory', 'model', 'update_time', 'update_at')
    search_fields = ['sn', 'asset__hostname']
    # list_filter = ('manufactory','update_at','asset__idc')
    list_filter = ('manufactory', ('update_at', DateRangeFilter), 'asset__idc')
    filter_horizontal = ('nic', 'physical_disk_driver', 'ram', 'raid_adaptor', 'software')

    # date_hierarchy = 'update_at'
    def from_idc(self, obj):
        return '%s' % obj.asset.idc

    from_idc.short_description = 'IDC'

    def update_time(self, obj):
        return obj.update_at.strftime('%Y-%m-%d %H:%M:%S')

    update_time.short_description = u'更新时间'


class NICAdmin(admin.ModelAdmin):
    search_fields = ['parent_sn', 'mac']
    list_display = ('sn', 'model', 'name', 'ipaddr', 'mac')


class RAMAdmin(admin.ModelAdmin):
    list_display = ('sn', 'model', 'slot', 'manufactory')


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('sn', 'manufactory', 'model', 'firmware', 'port_num', 'device_detail')


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('version', 'types')


class ContractAdmin(admin.ModelAdmin):
    list_display = ('sn', 'name', 'cost', 'start_date', 'end_date', 'license_num')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'department', 'email', 'phone', 'mobile', 'backup_name', 'leader')


class MaintainenceAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'maintain_type', 'device_sn', 'description', 'applicant', 'event_start', 'event_end', 'performer')
    list_filter = ('name', 'maintain_type', 'applicant', 'event_start')
    # date_hierarchy = 'event_start'
    search_fields = ('device_sn',)


class RaidAdaptorAdmin(admin.ModelAdmin):
    list_display = ('name', 'sn', 'parent_sn', 'model', 'memo')


class DiskAdmin(admin.ModelAdmin):
    search_fields = ['parent_sn']
    list_display = ('slot', 'sn', 'parent_sn', 'model', 'iface_type')


class CPUAdmin(admin.ModelAdmin):
    search_fields = ['parent_sn']
    list_display = ('sn', 'parent_sn', 'model')


class EventLogAdmin(admin.ModelAdmin):
    search_fields = ['uuid', 'detail', 'post_data']
    list_display = ('id', 'uuid', 'detail', 'create_at')
    list_filter = ('create_at',)
    # date_hierarchy = 'create_at'


class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'os_installed', 'puppet_installed', 'zabbix_configured', 'auditing_configured', 'approved')


class ApiAuthAdmin(admin.ModelAdmin):
    list_display = ('url', 'method_type', 'description')


admin.site.register(models.ApiAuth, ApiAuthAdmin)
admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.Configuration, ConfigurationAdmin)
admin.site.register(models.Server, ServerAdmin)
admin.site.register(models.NetworkDevice, NetworkAdmin)
admin.site.register(models.Software, SoftwareAdmin)
admin.site.register(models.Disk, DiskAdmin)
admin.site.register(models.CPU, CPUAdmin)
admin.site.register(models.NIC, NICAdmin)
admin.site.register(models.Contract, ContractAdmin)
admin.site.register(models.Manufactory)
admin.site.register(models.ProductVersion)
admin.site.register(models.BusinessUnit)
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Maintainence, MaintainenceAdmin)
admin.site.register(models.IDC)
admin.site.register(models.Memory, RAMAdmin)
admin.site.register(models.Monitor)
admin.site.register(models.RaidAdaptor, RaidAdaptorAdmin)
admin.site.register(models.EventLog, EventLogAdmin)
