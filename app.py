import requests
import json

URL = 'https://www.way2sms.com/api/v1/sendCampaign'

def create_request(reqUrl,apiKey,secretKey,useType,phoneNo,senderId,textMsg):
    reqParam = {'apikey':apiKey,
                'secret':secretKey,
                'usetype':useType,
                'phone':phoneNo,
                'message':textMsg,
                'senderid':senderId
                }
    return requests.post(reqUrl,reqParam)

msg =  'Hi There !'

response = create_request(URL,'','','stage','','pythonCode',msg)
print(response.text)
