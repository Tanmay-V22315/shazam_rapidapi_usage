import os
import json
import base64 
import requests
import sounddevice as sd
import time
from soundfile import write

#Wait before recording, so that you can get ready
for i in range(3,0,-1):
    print("Recording begins in",str(i))
    time.sleep(1)

print("Recording has begun!")

#Recording audio from microphone
x=sd.rec(7*44100,44100, channels=1)
sd.wait()

print("Recording stopped. Sending data...")

#writing it to a temporary file so that it can be loaded later
write("temp.wav", x, 44100)
enc=base64.b64encode(open("temp.wav","rb").read())

#This functions is the main thing. 

url = "https://shazam.p.rapidapi.com/songs/detect"

payload = enc
#You need to add your API key below
headers = {
    'content-type': "text/plain",
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "{YOUR API KEY}"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print("Identified as:",json.loads(response.text)['track']['title'],"by",json.loads(response.text)['track']['subtitle'])



#Cleaning up
os.remove("temp.wav")