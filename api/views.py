from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import os
from bs4 import BeautifulSoup

'''
API for My Disney Experience

Created by: Brian Jett
Email: bdjett@me.com
Website: http://logicalpixels.com
'''

@csrf_exempt
def parkHours(request, year, month, date):

	username = request.POST['username']
	password = request.POST['password']

	response_data = {}

	# Payload for login information
	payload = {
		'username': username,
		'password': password
	}

	# Attempt to login
	with requests.Session() as s:
		r = s.post('https://disneyworld.disney.go.com/login/', data=payload)

		r = s.get('https://disneyworld.disney.go.com/plan/itinerary/' + year + '-' + month + '-' + date + '/')
		soup = BeautifulSoup(r.content)

		park_hours = soup.find("ul", {"class": "parkHoursList"}).find_all("li")

		print park_hours

		response_data['result'] = 'success'
		response_data['content'] = {}
		response_data['content']['parks'] = []

		for li in park_hours:
			park_data = {}
			park_data['hours'] = {}

			park = li.find("div", {"class":"pkTitle"}).string
			hours = li.find("div", {"class":"operating"})
			emHours = li.find("div", {"class":"extraMagicHours"})
			closed = li.find("div", {"class":"closed"})

			park_data['park'] = park.string

			if hours:
				park_data['hours']['operating'] = hours.string
			else:
				park_data['hours']['operating'] = False

			if emHours:
				park_data['hours']['extraMagicHours'] = emHours.string
			else:
				park_data['hours']['extraMagicHours'] = False

			if closed:
				park_data['hours']['closed'] = True
			else:
				park_data['hours']['closed'] = False

			response_data['content']['parks'].append(park_data)

		return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def itineraryForDate(request, year, month, date):

	username = request.POST['username']
	password = request.POST['password']

	response_data = {}

	# Payload for login information
	payload = {
		'username': username,
		'password': password
	}

	# Attempt to login
	with requests.Session() as s:
		r = s.post('https://disneyworld.disney.go.com/login/', data=payload)

		r = s.get('https://disneyworld.disney.go.com/plan/itinerary/' + year + '-' + month + '-' + date + '/')
		soup = BeautifulSoup(r.content)

		destinations = soup.find_all("article", {"class":"destinationBlock"})

		if not destinations:
			response_data['result'] = 'fail'
			response_data['content'] = 'Request failed'

			return HttpResponse(json.dumps(response_data), content_type="application/json")

		response_data['result'] = 'success'
		response_data['content'] = {}
		response_data['content']['destinations'] = []

		for destination in destinations:
			resort = destination.find("div", {"class":"resort"})
			if resort:
				# got a resort
				name = resort.string
				confNum = destination.find("div", {"class":"confirmationNumber"}).contents[1].string.strip(' ')
				response_data['content']['resort'] = {}
				response_data['content']['resort']['name'] = name
				response_data['content']['resort']['confNumber'] = confNum
			else:
				destination_data = {}
				name = destination.find("h1", {"class":"name"})
				if name:
					destination_data['name'] = name.string
				else:
					destination_data['name'] = destination.find("div", {"class":"name"}).string

				destination_data['plans'] = []

				plans = destination.find_all("div", {"class":"planListItem"})

				for plan in plans:
					plan_data = {}
					time = plan.find("time")
					hours = time.contents[0].string
					ampm = time.contents[1].contents[0].string
					time = hours + ampm

					name = plan.find("h2", {"class":"name"}).string

					if u'fastPassPlus' in plan['class']:
						isFastPass = True
					else:
						isFastPass = False

					plan_data['time'] = time
					plan_data['name'] = name
					plan_data['fastPass'] = isFastPass

					destination_data['plans'].append(plan_data)

				response_data['content']['destinations'].append(destination_data)


		return HttpResponse(json.dumps(response_data), content_type="application/json")
