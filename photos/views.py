from django.shortcuts import render

# Create your views here.
def photos(request):
    photos = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'photos.html',{'photos':photos,'locations':locations})
