import requests
import json
from arlo import Arlo

USERNAME = ''
PASSWORD = ''

print('Api is listening\n')

try:

    arlo = Arlo(USERNAME, PASSWORD)

    basestations = arlo.GetDevices('basestation')

    def callback(arlo, event):

        print("Motion has been Detected")

        body = json.dumps({
            "notification": "Motion has been Detected",
            "accessCode": ""
        })
        requests.post(
            url="https://api.notifymyecho.com/v1/NotifyMe", data=body)
    arlo.SubscribeToMotionEvents(basestations[0], callback)

except Exception as e:
    print(e)
