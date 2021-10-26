import requests

def CheckFormat():
    response = requests.get('https://app.citadel.one/api/webhooks/mixpanel/track/?verbose=1&ip=1&_=1635233727838')
    return ((response.headers['Content-Type']))


