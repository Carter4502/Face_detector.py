
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json

subscription_key = ‘YOURSUBSCRIPTIONKEY’

uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = {
    'returnFaceAttributes': 'glasses',
}

body = {'url': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'}

try:
    response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers= headers, params=params)
    parsed = json.loads(response.text)
    info = (json.dumps(parsed, sort_keys=True, indent=2))
    glasses = parsed[0]['faceAttributes']['glasses']
    print(glasses)

except Exception as e:
    print('Error:')
    print(e)
