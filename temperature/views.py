from __future__ import unicode_literals
from .models import Weather,Weather1         # Here we are importing module Weather
from django.shortcuts import render     # Importing render module
# Create your views here.
from django.http import HttpResponse    # Importing Httpresponse module
# Defining a function index
def index(request):
	received_data=Weather.objects.all()[len(Weather.objects.all())-1] # Retriving last values of sensors in database
	temp_data=str(received_data.tem_value)  # Retriving Weather value
	hum_data=str(received_data.hum_value)   # Retriving humidity value
	soil_data=str(received_data.soil_value) # Retriving soil moisture value
	context={'tem':temp_data,'hum':hum_data,'soil':soil_data} # Assigning sensor values to respective word 
	return render(request,'index.html',context)  # returning values to index.html page 
# Defining a function getdata	
def getdata(request):
 if request.method=='GET' :          # If request metod is get method following values are retrived
  tem_value=request.GET['temperature']  # retriving Weather value from get method
  hum_value=request.GET['humidity']     # retriving humidity value from get method
  soil_value=request.GET['soil_moisture1']   # retriving soil moisture value from get method
  rain_value=request.GET['rain_info_1']     #retriving rain status from get method
  water_value=request.GET['water_lev']      #retriving water_level value from get method
  t_obj=Weather()                # Weather object is assigned to t_obj
  t_obj.tem_value=tem_value         # tem_value obtained above is assigned to t_obj.tem_value
  t_obj.hum_value=hum_value         # hum_value obtained above is assigned to t_obj.hum_value
  t_obj.soil_value=soil_value       # soil_value obtained above is assigned to t_obj.soil_value
  t_obj.rain_value=rain_value       # rain status obtained above is assigned to t_obj.rain_value
  t_obj.water_value=water_value     # water_value obtained above is assigned to t_obj.water_value 
  t_obj.save()
  tem_value=request.GET['temperature']  # retriving Weather value from get method
  hum_value=request.GET['humidity']     # retriving humidity value from get method
  soil_value=request.GET['soil_moisture2']   # retriving soil moisture value from get method
  rain_value=request.GET['rain_info_1']     #retriving rain status from get method
  water_value=request.GET['water_lev']      #retriving water_level value from get method
  t_obj1=Weather1()                # Weather object is assigned to t_obj
  t_obj1.tem_value1=tem_value         # tem_value obtained above is assigned to t_obj.tem_value
  t_obj1.hum_value1=hum_value         # hum_value obtained above is assigned to t_obj.hum_value
  t_obj1.soil_value1=soil_value       # soil_value obtained above is assigned to t_obj.soil_value
  t_obj1.rain_value1=rain_value      # rain status obtained above is assigned to t_obj.rain_value
  t_obj.water_value1=water_value   # water_value obtained above is assigned to t_obj.water_value 
  t_obj.save()
  return HttpResponse("data saved in db")
 else:
  return HttpResponse("error")
# Defining a function temp
received_data=[]
temp_data=[]
hum_data=[]
def temp(request):
 for i in range(1,9):
  received_data.append(Weather.objects.all()[len(Weather.objects.all())-i])
 for i in range(0,8):
  temp_data.append(str(received_data[i].tem_value)) # Retriving Weather value
  hum_data.append(str(received_data[i].hum_value))  # Retriving humidity value
 soil_data=str(received_data[0].soil_value) # Retriving soil moisture value
 moisture=soil_data[:len(soil_data)-1]
 rain_data=str(received_data[0].rain_value) # Retriving rain status
 water_data=str(received_data[0].water_value) # Retriving water_level value
 
 context={'tem':temp_data[0],'hum':hum_data[0],'tem1':temp_data[1],'hum1':hum_data[1],'tem2':temp_data[2],'hum2':hum_data[2],'tem3':temp_data[3],'hum3':hum_data[3],'tem4':temp_data[4],'hum4':hum_data[4],'tem5':temp_data[5],'hum5':hum_data[5],'tem6':temp_data[6],'hum6':hum_data[6],'tem7':temp_data[7],'hum7':hum_data[7],'soil':moisture,'mois':soil_data,'rain':rain_data,'water':water_data} # Assigning sensor values to respective word 
 return render(request,'temp.html',context)  # returning values to temp.html page  

