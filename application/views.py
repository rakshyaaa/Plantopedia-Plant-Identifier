from django.shortcuts import render
from .predictPlant import plantPredict
from .models import Image
from .form import ImageForm


def application(request):
    return render(request, 'index.html', {})



def predictImage(request):
    if request.method == "POST":
        print("post method")
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            p = plantPredict()
            p.prediction(obj.image.url)
    else:
        print("Get method")
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html", {})

    return render(request, 'index.html', {})