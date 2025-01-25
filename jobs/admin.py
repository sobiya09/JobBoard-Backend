# from django.contrib import admin
# from .models import Job, CV

# admin.site.register(Job)
# admin.site.register(CV)
from django.contrib import admin
from .models import Job,CV
from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'request_type', 'entity_type', 'created_at')
    list_filter = ('request_type', 'entity_type', 'created_at')
    search_fields = ('name', 'email', 'description')




# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ('title', 'company_name', 'location', 'posted_at')

#  # Override save_model method if you need custom save logic
#     def save_model(self, request, obj, form, change):
#         # Ensure the job is saved
#         obj.save()

admin.site.register(Job)
admin.site.register(CV)




