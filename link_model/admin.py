from django.contrib import admin
from django.db.models import QuerySet

from link_model.models import Provider
from django.urls import reverse
from django.utils.html import format_html





class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'provider', 'arrears', 'time_create', 'link_contact')
    list_display_links = ('id',)
    search_fields = ('type', 'name')
    list_editable = ('name',)
    list_filter = ('type', 'name')

    actions = ['delete_arrears']

    def link_contact(self, obj):
        '''ссылка на объект Provider в
        модели продукта'''
        link = reverse("admin:contacts_contact_change", args=[obj.contacts_id])
        return format_html('<a href="{}"> {}</a>', link, obj.contacts.email)

    link_contact.short_description = 'Адрес'

    @admin.action(description='Удалить задолженности')
    def delete_arrears(self, request, queryset: QuerySet):
        '''Обнуление задолженности'''
        queryset.update(arrears=0)


admin.site.register(Provider, ProviderAdmin)
