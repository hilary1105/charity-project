from django.shortcuts import render, redirect
from charityfinder.forms import charityappForm
from charityfinder.models import charityapp


def create(request):
    if request.method == "POST":
        form = charityappForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/all-charity")

    else:
        form = charityappForm()

    return render(request, 'create.html', {'form': form})


def show(request):
    charity = charityapp.objects.all()
    return render(request, "show.html", {'charity': charity})


def delete(request, id):
    charity = charityapp.objects.get(id=id)
    charity.delete()
    return redirect("/all-charity")

def edit(request, id):
    charity = charityapp.objects.get(id = id)
    return render(request, 'edit.html', {"charity": charity})

def update(request, id):
    charity = charityapp.objects.get(id=id)
    print(request.POST)
    form = charityappForm(request.POST, instance = charity)
    print(form.is_valid())
    if form.is_valid():
        charity.save()
        return redirect("/all-charity")

    return render(request, 'edit.html', {"charity": charity})
