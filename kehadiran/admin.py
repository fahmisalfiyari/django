# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from kehadiran.models import Kehadiran, Izin

# Register your models here.
class KehadiranAdmin (admin.ModelAdmin):
	list_display = ['karyawan', 'jenis_kehadiran', 'waktu']
	list_filter = ('jenis_kehadiran',)
	search_fields = []
	list_per_page = 25

admin.site.register(Kehadiran, KehadiranAdmin)

class IzinAdmin(admin.ModelAdmin):
	list_display = ['karyawan','jenis_kehadiran','waktu_mulai','waktu_berhenti','disetujui']
	list_filter = ('jenis_kehadiran','disetujui')
	search_fields = ['alasan']
	list_per_page = 25

admin.site.register(Izin, IzinAdmin)