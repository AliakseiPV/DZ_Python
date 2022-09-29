from pyowm import *

owm = OWM("4089dcfe307e654c3422c53048f783aa")
place = input("Enter the name of the sity: ")
manager = owm.weather_manager()
observation = manager.weather_at_place(place)
w = observation.weather

t = w.temperature("celsius")
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']

wi = w.wind()['speed']
humid = w.humidity
cloud = w.clouds
pr = w.pressure['press']
ti = w.reference_time('iso')


print(f'In {place}, the t {t1}, feels like {t2}, the max t {t3}, the min t {t4}\n\
Wind speed {wi}, humidity {humid}, cloud cover {cloud}, pressure {pr}\n Time: {ti}')