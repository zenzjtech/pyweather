# pyweather
Pyweather is a quick python program for crawling current and predicting future weather condition.

Input anything without having to worry about the format and pyweather will do the rest for
you!

Pyweather is currently available in python 2. only.
## Installation

Cloning git repo:
	
	$ git clone https://github.com/fluteguitar/pyweather.git

Install requirements:

	$ pip install requirements.txt

## Usage

Help:
	$ python pyweather.py -h
or,
	$ python pyweather.py -help

Input with data from arguments:
	
	$ python pyweather.py "New york" "NewDelhi" "NewYork" "^^+{}:^"
	New york
		Weather: Partly Cloudy
		Humidity: 88%
		Wind Speed: 10km/h
		Temperature: 17^C
		UV: 0/10 Low

	NewDelhi
		Weather: Haze
		Humidity: 37%
		Wind Speed: 21km/h
		Temperature: 34^C
		UV: 5/10 Moderate

	NewYork
		Weather: Partly Cloudy
		Humidity: 88%
		Wind Speed: 10km/h
		Temperature: 17^C
		UV: 0/10 Low

	^^+{}:^
		Unavailable Location

Input with data from text file:
	$ python weather.py -i sample_location.txt
	NewYork

		Weather: Partly Cloudy
		Humidity: 88%
		Wind Speed: 10km/h
		Temperature: 17^C
		UV: 0/10 Low

	New York

		Weather: Partly Cloudy
		Humidity: 88%
		Wind Speed: 10km/h
		Temperature: 17^C
		UV: 0/10 Low

	Long Xuyên, An Giang VN-44

		Weather: Rain Shower
		Humidity: 82%
		Wind Speed: 21km/h
		Temperature: 28^C
		UV: 2/10 Low

	Vũng Tàu, Bà Rịa– Vũng Tàu VN-43

		Weather: Rain
		Humidity: 80%
		Wind Speed: 14km/h
		Temperature: 28^C
		UV: 2/10 Low
