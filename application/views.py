from django.shortcuts import render
from .predictPlant import plantPredict
from .models import Image
from .form import ImageForm


def application(request):
    return render(request, 'index.html', {})



def predictImage(request):
    if request.method == "POST":
        print("post method")
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            obj=form.instance
            print(obj)

            # p = plantPredict()
            # p.prediction(obj.image.url)

            return render(request, "index.html", {'obj': obj})



        else:
            print('invalid')
    else:
        print("Get method")
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html", {'form':form, 'img':img})

