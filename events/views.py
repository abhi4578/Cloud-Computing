from django.shortcuts import render, redirect
from predicthq import Client
from django.http import HttpResponse
import requests

# Create your views here.

def index(request):

	url = "https://api.predicthq.com/v1/events/"
	ACCESS_TOKEN = "h8jTYSTHTta2o84n9WfahbIO2eRC9S"
	payload={
	'sort':'rank',
	'count':'50',
	'category' : 'disasters',
	'labels' : ['disaster','fire']
	}
	headers={
	'Accept': 'application/json',
	'Authorization': "Bearer " + ACCESS_TOKEN
	}
	r = requests.get(url, params=payload,headers=headers)
	# phq = Client(access_token=ACCESS_TOKEN)
	results = r.json()['results']
	#print(results)
	count = 0
	for i in results:
		
		
		if 'vehicle-accident' in i['labels']:
			results.pop(count)

		
		count = count + 1

	for i in results:
		print(i)
		print("*"*100)	
	# for event in phq.events.search(category="disasters",state="active"):
	#     print(event.description, event.category, event.title, event.start.strftime('%Y-%m-%d'))
	return render(request,'listOfEvents.html',{'events':results})

def eventDetail(request,eventId):
	url = "https://api.predicthq.com/v1/events/"
	ACCESS_TOKEN = "h8jTYSTHTta2o84n9WfahbIO2eRC9S"
	payload={
	'id' : eventId
	}
	headers={
	'Accept': 'application/json',
	'Authorization': "Bearer " + ACCESS_TOKEN
	}
	r = requests.get(url, params=payload,headers=headers)
	#print(eventId)
	results = r.json()['results']
	print(results)
	results = results[0]

	return render(request,'eventDetail.html',{'event':results})



