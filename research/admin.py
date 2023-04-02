from django.contrib import admin

from . import models

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'keywords', 'description')
    
class PaperAdmin(admin.ModelAdmin):
    list_display = ('get_subject_name','rating', 'title', 'authors', 'summary', 'short_id', 'is_read', 'published_date', 'updated_date')
    
    def get_subject_name(self, obj):
        return obj.subject.name
    get_subject_name.admin_order_field  = 'subject'  #Allows column order sorting
    get_subject_name.short_description = 'Subject Name'  #Renames column head

admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Paper, PaperAdmin)
