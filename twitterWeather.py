#twitter
from turtle import pos
import twitter

#meteo
from bs4 import BeautifulSoup
import requests

#key/token twitter
api = twitter.Api(consumer_key='RSxgI2nOWzpcX2pe38SCHLlyZ',
                consumer_secret='o7vIawwlWpm7S9J86xb3leT1lhFAk3V02FSACUtMo1pdjbRYXu',
                access_token_key='1564255133835399169-u83V2ZYA2UVWhkmrerWjyifBarTOTB',
                access_token_secret='Ge8OofmmlX5xXg12s184xnrs0O2dfpvz5OGlBgfpwZt2B')

listeDeVille = ['Vierzon', 'Reuilly', 'Angers', 'Nohant-en-Goût', 'Coulandon', 'Dijon', 'Moulins', 'Sainte-Verge ']
meteoVille = []
#ecrire un tweet
#def postStatus(location,info,weather):
    #status = api.PostUpdate(location+'\n'+info+'\n'+weather)
    #print(status.text)

def postStatus(chaine):
    status = api.PostUpdate(chaine)
    print(status.text)

#requete pour meteo
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/58.0.3029.110 Safari/537.3'}

#recup de la meteo pour une ville donnée
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(f'https://google.com/search?q={city}\
        &oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=\
        chrome&ie=UTF-8', headers=headers)
    #print('Searching.....\n')
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    #return(location, info, weather+" C°")
    return(location, info, weather)

for i in range(len(listeDeVille)):
    t = weather(listeDeVille[i]+' weather')
    location, info, Vweather = t
    #Vweather = int(Vweather)
    #ça caille
    if int(Vweather) <= 5:
        meteoVille.append(location+' '+info+' '+Vweather+" C° ❄️")
    #froid mais ok
    elif int(Vweather) <= 15:
        meteoVille.append(location+' '+info+' '+Vweather+" C° 🥶")
    #c'est cool
    elif int(Vweather) <= 25:
        meteoVille.append(location+' '+info+' '+Vweather+" C° 🌡️")
    #chaud
    elif int(Vweather) <= 32:
        meteoVille.append(location+' '+info+' '+Vweather+" C° 🥵")
    #trés chaud pas cool
    else:
        meteoVille.append(location+' '+info+' '+Vweather+" C° 🔥")
    #s = "\n".join(meteoVille)

#for i in range(len(meteoVille)):
 #   print(meteoVille[i])

s = "\n".join(meteoVille)
print(s)
#postStatus(s)
#postStatus(location, info, Vweather) 