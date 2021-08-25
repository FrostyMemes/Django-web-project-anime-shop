
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

from PIL import Image
'''
class DakimakuraAdminForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:13px;"> Загружайте изображения с минимальным разрешением {}x{}</span>'.format(
                *Product.MIN_RESOLUTION
            )
        )
    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Загруженное изображение меньше минимального разрешения!')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Загруженное изображение больше максимально разрешения!')
        return image
'''
class DakimakuraAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return  ModelChoiceField(Category.objects.filter(slug='dakimakuras'))
        return  super().formfield_for_foreignkey(self, db_field, request, **kwargs)


class FigurinesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return  ModelChoiceField(Category.objects.filter(slug='figurines'))
        return  super().formfield_for_foreignkey(self, db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Dakimakuras, DakimakuraAdmin)
admin.site.register(Figurines, FigurinesAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)

