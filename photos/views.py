from django.shortcuts import render

# Create your views here.
def photos(request):
    photos = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'photos.html',{'photos':photos,'locations':locations})

def locations(request,location):
    locations = Image.filterimageByLocation(location)
    return render(request,'locations.html',{'locations':locations})
