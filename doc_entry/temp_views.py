from django.shortcuts import render, redirect
from .models import Language, Programmer
from django.forms import modelformset_factory, inlineformset_factory


def index(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    # language_formset = modelformset_factory(Language, fields=('name', 'number', 'price', 'total'))
    language_formset = inlineformset_factory(Programmer, Language, fields=('name', 'number', 'price'),
                                             can_delete=False)
    if request.method == 'POST':
        # formset = language_formset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = language_formset(request.POST, instance=programmer)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.programmer_id = programmer.id
                instance.total = instance.number * instance.price
                instance.save()
            return redirect('index', programmer_id=programmer.id)

    # formset = language_formset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = language_formset(instance=programmer)
    return render(request, 'website/index.html', {'formset': formset})
