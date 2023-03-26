from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'country', 'city')
    list_editable = ('city',)
    list_filter = ('country', 'city')

    #def link_provider(self, obj):
    #    '''ссылка на объект Provider в
    #    модели продукта'''
    #    link = reverse("admin:link_model_provider_change", args=[obj.provider_id])
    #    return format_html('<a href="{}"> {}</a>', link, obj.provider.name)
#
    #link_provider.short_description = 'Поставщик'

admin.site.register(Contact, ContactAdmin)
