from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.management.base import BaseCommand
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import json
from traceback import print_exc
from django.db.models import Max
import csv



def current_value(request):
    csv_filename = 'Fixtures.csv'
    data = []

    try:
        with open(csv_filename, 'r') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        data = None

    return render(request, 'welcome.html', {'data': data})





'''def current_value(request):
    # Get the latest data across all grid_sections
    data = SoilData.objects.all().order_by('-id').first()
    
    return render(request,'welcome.html',{'data':data})'''



# Create your views here.
# myapp/views.py

def welcome(request):
    fdata = FIXTURE.objects.all().order_by("-id").first()
    rdata=RESULTS.objects.all().order_by("-id").first()
    idata=ICC_RANKING.objects.all().order_by("-id").first()
    return render(request, 'welcome.html',{'fdata':fdata,'rdata':rdata,'idata':idata})

from .models import *

def fixture_filter(request):
   if request.method == 'POST':
        date = request.POST.get('Date')
        round_number=request.POST.get('Round_number')
        if date:
            data=FIXTURE.objects.all().filter(Date=date)
        elif round_number and not date: 
            data=FIXTURE.objects.all().filter(Round_number=round_number)
        
        csv_filename = 'fixture_writer.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
        # Write a header if the file is empty
            for entry in data:
                csv_writer.writerow([entry.Round_number,entry.Team_1,entry.Team_2,entry.Date,entry.Location,entry.Group])
        return render(request,'fixture.html',{'data':data})
   return redirect('fixture')

def result_filter(request):
   if request.method == 'POST':
        team_1 = request.POST.get('Team_1')
        team_2=request.POST.get('Team_2')
        if team_1:
            data=RESULTS.objects.all().filter(Team_1=team_1)
        elif team_2: 
            data=RESULTS.objects.all().filter(Team_2=team_2)
        
        csv_filename = 'result_filter.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
        # Write a header if the file is empty
            for entry in data:
                csv_writer.writerow([entry.Date,entry.Team_1,entry.Team_2,entry.Winner,entry.Margin,entry.Ground])
        return render(request,'result.html',{'data':data})
   return redirect('result')

def grid_section_detail(request):
    data = FIXTURE.objects.all()
    return render(request, 'npk.html', {'data': data})

from django.http import HttpResponse
import os

def download_csv(request):
    # Path to the CSV file
    csv_file_path = 'fixture_writer.csv'  # Replace with the actual path to your CSV file

    # Open the CSV file
    with open(csv_file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return response

def download_csv1(request):
    # Path to the CSV file
    csv_file_path = 'result.csv'  # Replace with the actual path to your CSV file

    # Open the CSV file
    with open(csv_file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

def download_csv2(request):
    # Path to the CSV file
    csv_file_path = 'ranking_filter.csv'  # Replace with the actual path to your CSV file

    # Open the CSV file
    with open(csv_file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return response

def moisture(request):
    data = RESULTS.objects.all()
    return render(request, 'water.html', {'data': data})

def ranking(request):
    data = ICC_RANKING.objects.all()
    return render(request, 'ranking.html', {'data': data})

def ranking_filter(request):
   if request.method == 'POST':
        team_name = request.POST.get('Team_name')
        team_2=request.POST.get('Team_2')
        if team_name:
            data=ICC_RANKING.objects.all().filter(Team_name=team_name)
        
        csv_filename = 'ranking_filter.csv'
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
        # Write a header if the file is empty
            for entry in data:
                csv_writer.writerow([entry.Team_ranking,entry.Team_name,entry.Rating])
        return render(request,'ranking_filter.html',{'data':data})
   return redirect('ranking_filter')

'''def current_value(request, grid_section):
    data = SoilData.objects
    return render(request, 'welcome.html', {'data': data})'''
    
'''@csrf_exempt
def receive_data_from_rover(request):
    if request.method == 'POST':
        try:

            # Get JSON data from the request
            data_json = json.loads(request.body)

            
            # Extract relevant information from the JSON data
            grid_section = data_json.get('grid_section')
            nitrogen = data_json.get('nitrogen')
            phosphorus = data_json.get('phosphorus')
            potassium = data_json.get('potassium')
            moisture_level = data_json.get('moisture_level')

            # Create a new SoilData instance and save it to the database
            soil_data = SoilData.objects.create(
                grid_section=grid_section,
                nitrogen=nitrogen,
                phosphorus=phosphorus,
                potassium=potassium,
                moisture_level=moisture_level
            )

            return JsonResponse({'message': 'Data received and stored successfully'})
        except Exception as e:
            print_exc()
            return JsonResponse({'error': f'Error: {str(e)}'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)'''

class ReceiveDataFromRoverAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FIXTUREdataserializer(data=request.data)

        if serializer.is_valid():
            csv_filename = 'soil_data.csv'
            with open(csv_filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write a header if the file is empty
                if csvfile.tell() == 0:
                    csv_writer.writerow(serializer.validated_data.keys())
                csv_writer.writerow(serializer.validated_data.values())
            # Save the data to the database
            fixture = FIXTURE.objects.create(**serializer.validated_data)
           

            return JsonResponse({'message': 'Data received and stored successfully'})
            
           
        else:
            print_exc
            return JsonResponse({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
        
class ReceiveDataFromRoverAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = FIXTUREdataserializer(data=request.data)

        if serializer.is_valid():
            csv_filename = 'soil_data.csv'
            with open(csv_filename, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write a header if the file is empty
                if csvfile.tell() == 0:
                    csv_writer.writerow(serializer.validated_data.keys())
                csv_writer.writerow(serializer.validated_data.values())
            # Save the data to the database
            fixture = FIXTURE.objects.create(**serializer.validated_data)
           

            return JsonResponse({'message': 'Data received and stored successfully'})
            
           
        else:
            print_exc
            return JsonResponse({'error': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
