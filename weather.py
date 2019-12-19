import pyowm
owm = pyowm.OWM('G097IueS-9xN712E', language = "ru")

place = input("В каком городе/стране: ")

observation = owm.weather_at_place(place)
w = observation.get_weather()

print (w)