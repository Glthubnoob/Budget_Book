from django import forms
from django.forms import inlineformset_factory
from .models import Category, Document, Location, Position, Product, Unit
from crispy_forms.helper import FormHelper  # Layout
# from crispy_forms.layout import Row, Column, HTML


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['date_of_purchase', 'location', 'total']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', ]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', ]


class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name', ]


class PositionFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PositionFormHelper, self).__init__(*args, **kwargs)
        self.form_method = 'POST'
        # Following layout won't be used as it has no effect on the table_inline_formset.html
        # which is used to create the table layout
        
        # self.layout = Layout(

        #     Row(
        #         Column('product', css_class='col-md-4 mb-0', style='padding-right: 2px; font-size: 10px;'),
        #         Column('unit', css_class='col-md-2 mb-0', style='padding-right: 2px padding-left: 2px;'),
        #         Column('quantity', css_class='col-md-2 mb-0', style='padding-right: 2px; padding-left: 2px;'),
        #         Column('price', css_class='col-md-2 mb-0', style='padding-right: 2px; padding-left: 2px;'),
        #         Column('total', css_class='col-md-2 mb-0', style='padding-right: 2px; padding-left: 2px; '),
        #     )
        # )
        self.render_required_fields = True


PositionFormset = inlineformset_factory(Document, Position, fields=(
    'id', 'product', 'unit', 'quantity', 'price', 'total'), localized_fields='__all__',  extra=3, can_delete=False)
