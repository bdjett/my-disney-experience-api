#MyDisneyExperience API

JSON API for MyDisneyExperience written using Python and the django framework with BeautifulSoup.

##Contributions

Contributions are always appreciated. Feel free to fork.

##Example Use

###Itinerary for Day

	http://localhost:8000/date/{yyyy}/{mm}/{dd}/

Returns:

	{
		"content": {
			"resort": {
				"confNumber": "6UM04XXX",
				"name": "Disney's Yacht Club Resort"
			}, "destinations": [
				{
					"name": "Magic Kingdom\u00ae Park",
					"plans": [
					{
						"fastPass": true,
						"name": "Big Thunder Mountain Railroad\u00ae",
						"time": "12:35 PM"
					}, {
						"fastPass": true,
						"name": "Buzz Lightyear's Space Ranger Spin\u00ae",
						"time": "2:30 PM"
					}, {
						"fastPass": true,
						"name": "Space Mountain\u00ae",
						"time": "3:30 PM"
					}, {
						"fastPass": false,
						"name": "Tony's Town Square Restaurant",
						"time": "6:00 PM"
					}]
				}]
			},
		"result": "success"
	}

###Park Hours

	http://localhost:8000/hours/{yyyy}/{mm}/{dd}/

Returns:

	{
		"content": {
			"parks": [
				{
					"hours": {
						"extraMagicHours": "8:00 AM to 9:00 AM \u2013 Extra Magic Hours",
						"operating": "9:00 AM to 1:00 AM",
						"closed": false
					},
					"park": "Magic Kingdom\u00ae Park"
				}, {
					"hours": {
						"extraMagicHours": false,
						"operating": "9:00 AM to 9:00 PM",
						"closed": false
					},
					"park": "Epcot\u00ae"
				}, {
					"hours": {
						"extraMagicHours": false,
						"operating": "9:00 AM to 9:30 PM",
						"closed": false
					},
					"park": "Disney's Hollywood Studios\u00ae"
				}, {
					"hours": {
						"extraMagicHours": false,
						"operating": "8:00 AM to 8:00 PM",
						"closed": false
					},
					"park": "Disney's Animal Kingdom\u00ae Theme Park"
				}, {
					"hours": {
						"extraMagicHours": false,
						"operating": "10:00 AM to 5:00 PM",
						"closed": false
					},
					"park": "Disney's Typhoon Lagoon Water Park"
				}, {
					"hours": {
						"extraMagicHours": false,
						"operating": "10:00 AM to 5:00 PM",
						"closed": false
					},
					"park": "Disney's Blizzard Beach Water Park"
				}]
			},
		"result": "success"
	}

##Future Plans
* More API Endpoints
* More information about each itinerary item
