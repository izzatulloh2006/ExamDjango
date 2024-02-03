from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    actions = ['export_csv']

    def export_csv(modeladmin, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contacts.csv"'

        writer = csv.writer(response)
        writer.writerow(['First Name', 'Last Name', 'Email'])

        for contact in queryset:
            writer.writerow([contact.first_name, contact.last_name, contact.email])

        return response

    export_csv.short_description = "Export selected contacts to CSV"


# admin.site.register(Contact)