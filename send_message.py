import requests

# TODO: Replace the following with your instance ID, Premium Client ID and Secret:
instanceId = "YOUR_INSTANCE_ID_HERE"
clientId = "YOUR_CLIENT_ID_HERE"
clientSecret = "YOUR_SECRET_HERE"

jsonBody = {
    'number': '12025550108',  # Specify the recipient's number (NOT the gateway number) here.
    'message': 'Have a nice day! Loving you:)'  # FIXME
}

headers = {
    'X-WM-CLIENT-ID': clientId, 
    'X-WM-CLIENT-SECRET': clientSecret
}

r = requests.post('http://api.whatsmate.net/v1/telegram/single/message/' + instanceId,
    headers=headers,
    json=jsonBody)

print("Status code: " + str(r.status_code))
print("RESPONSE : " + str(r.content))
