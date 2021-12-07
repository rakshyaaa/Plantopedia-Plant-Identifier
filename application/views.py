from django.shortcuts import render, redirect
from .predictPlant import plantPredict
from .information import info

p = plantPredict()
i = info()
def application(request):
    if request.method == "POST":
        img = request.FILES.get('image')
        result,predClass = p.prediction(img)
        print(result)
        print(predClass)
        info = i.getinfo(predClass)
        print(info)
        return render(request, 'index.html', {"result": result, "info": info})
    else:
        return render(request, 'index.html', {})


