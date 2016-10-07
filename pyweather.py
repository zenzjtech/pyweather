#!/usr/bin/env python
import sys
import getopt
from httplib import HTTPConnection
from json import loads, load
import codecs
from geopy.geocoders import GoogleV3

def gen_weather_api_link(location_name):
	
	site = 'api.weather.com'
	path = '/v2/turbo/vt1precipitation;vt1currentd'\
			'atetime;vt1pollenforecast;vt1dailyForecast;vt1observation?units'\
			'=m&language=en&geocode={},{}&format=json&apiKey=c1ea9f47f6a88b9'\
			'acb43aba7faf389d4'
	geolocator = GoogleV3()			
	location = geolocator.geocode(location_name)
	
	if location is None:
		return None, None

	path = path.format(
		str(location.latitude), 
		str(location.longitude))
	
	return site, path

def process_json_data(json_data):
	"""Return desired weather information from given json source.
	"""
	if json_data is None:
		return "\tUnavailable Location"

	dict = {}
	current_cond = json_data['vt1observation']
	return "\tWeather: {}\n\tHumidity: {}%\n\tWind Speed: {}km/h\n\tTemperature: {}^C" \
			"\n\tUV: {}/10 {}\n".format(
				current_cond['phrase'], current_cond['humidity'],
				current_cond['windSpeed'], current_cond['temperature'],
				current_cond['uvIndex'], current_cond['uvDescription']
				)

def process_http_request(location_name):

	site, path = gen_weather_api_link(location_name)
	if site is None:
		return None
	conn = HTTPConnection(site)
	conn.request("GET", path)
	res = conn.getresponse()
	if res.status != 200:
		return -1

	data = res.read()
	json_data = loads(data)

	return json_data

def get_location_list(file_inp):
	"""Return a list of location from input file.
	"""
	f = open(file_inp, "r")
	location_list = []
	for line in f:
		line.replace("\n", '')
		location_list.append(line)

	return location_list

def parse_argvs(argv):
	
	file_inp = ""
	file_out = ""
	usage_command = 'usage\n' \
			'python pyweather.py -i <inputfile> -o <outputfile>\n' \
			'python pyweather.py <"location 1"> <"location 2> ...'

	try: 
		opts, args = getopt.getopt(argv, "hi:o:", ["help", "ifile=", "ofile="])

	except getopt.GetoptError:
		print usage_command
		sys.exit("Wrong syntax, please try again!")
	
	for opt, arg in opts:
		if opt == 'h':
			print usage_command
			sys.exit()
		elif opt in ('-i', 'ifile'):
			file_inp = arg
		elif opt in ('-o', 'ofile'):
			file_out = arg

	#if input is of the string form of locations
	if opts == []:
		return (args, file_out)

	location_list = get_location_list(file_inp)
	return (location_list, file_out)

if __name__ == '__main__':

	location_list, file_out = parse_argvs(sys.argv[1:])
	if file_out != "":
		f = codecs.open(file_out, "w", "utf-8")
	for location_name in location_list:
		weather = process_json_data(process_http_request(location_name))
		if file_out != "":
			f.write(location_name + ":\n" +  weather)
		else:
			print location_name + "\n" + weather

	if file_out != "":
		f.close()
#print process_json_data(process_http_request("cu chi thanh pho ho chi minh"))
