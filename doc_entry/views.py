from django.shortcuts import render, redirect
from .models import Category, Document, Location, Product, Unit  # Position
# from django.forms import inlineformset_factory
from .forms import PositionFormset, PositionFormHelper, CategoryForm, DocumentForm, LocationForm, ProductForm, UnitForm  # FormHelper 
from crispy_forms.layout import Submit
from django.views.generic import CreateView, ListView


class DocumentListView(ListView):
    model = Document
    template_name = 'doc_entry/home.html'
    # ordering = ['-date_of_purchase']
    context_object_name = 'documents'
    queryset = Document.objects.all().order_by('-date_of_purchase')  # [:5]


class DocumentCreateView(CreateView):
    model = Document
    # fields = ('date_of_purchase', 'total')
    template_name = 'doc_entry/document_create.html'
    form_class = DocumentForm
    # success_url = reverse_lazy('book_list')


def home(request):
    return render(request, 'doc_entry/home.html')


def index(request, doc_id):
    document = Document.objects.get(pk=doc_id)
    print(document.date_of_purchase)
    helper = PositionFormHelper()
    helper.add_input(Submit('submit', 'Save'))
    helper.form_show_labels = False
    helper.template = 'doc_entry/table_inline_formset.html'
    if request.method == 'POST':
        formset = PositionFormset(request.POST, instance=document)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.doc_id = document.id
                instance.total = instance.quantity * instance.price
                instance.save()
            return redirect('index', doc_id=document.id)

    formset = PositionFormset(instance=document)

    return render(request, 'doc_entry/index.html', {'formset': formset, 'helper': helper, 'document': document})


class LocationCreateView(CreateView):
    model = Location
    template_name = 'doc_entry/document_create.html'
    form_class = LocationForm
    success_url = '/'
    # queryset = Location.objects.order_by('name')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Create Location'
        data['locations'] = Location.objects.order_by('name')
        return data


class ProductCreateView(CreateView):
    model = Product
    template_name = 'doc_entry/document_create.html'
    form_class = ProductForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Create Product'
        return data


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'doc_entry/document_create.html'
    form_class = CategoryForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Create Category'
        return data


class UnitCreateView(CreateView):
    model = Unit
    template_name = 'doc_entry/document_create.html'
    form_class = UnitForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['page_title'] = 'Unit Category'
        return data
