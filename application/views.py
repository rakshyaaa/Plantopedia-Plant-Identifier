from django.shortcuts import render
from .predictPlant import plantPredict
from .information import info

p = plantPredict()
i = info()
def application(request):
    if request.method == "POST":
        img = request.FILES.get('image')
        result,predClass = p.prediction(img)
        info = i.getinfo(predClass)
        return render(request, 'index.html', {"result": result, "info": info})
    else:
        return render(request, 'index.html', {})


