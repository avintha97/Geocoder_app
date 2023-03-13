from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Searchs
from .forms import SearchForm
import folium
import geocoder

# Create your views here.
def index(request):

    if request.method =='POST':
        form =SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()


    #create map object
    address = Searchs.objects.all().last()
    location =geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country =location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('your adress input is invalid')
    map = folium.Map(location=[ 7.96584,80.3568],zoom_start=2)
    marker = folium.Marker([ lat,lng],tooltip='click for more',popup=country)  
    marker.add_to(map)  
    map =map._repr_html_()
    context ={
        'm':map,
         'form':form,
    }
    return render(request,'index.html',context)

# def calculate_distance_view(request):
#     obj=get_list_or_404(Mesurements, id =1)

#     context ={
#         'distance':obj
#     }

#     return render(request,'index.html',context)



