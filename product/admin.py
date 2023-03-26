from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from product.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'data_publicate', 'link_provider')
    list_display_links = ('id', 'name')
    search_fields = ('model', 'name')
    list_filter = ('model', 'name', 'provider', 'provider__contacts__city')

    def link_provider(self, obj):
        '''ссылка на объект Provider в
        модели продукта'''
        link = reverse("admin:link_model_provider_change", args=[obj.provider_id])
        return format_html('<a href="{}"> {}</a>', link, obj.provider.name)

    link_provider.short_description = 'Поставщик'


admin.site.register(Product, ProductAdmin)
