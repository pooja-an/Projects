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

msg = ''' Ae Dukkr, Bhul gya na tu mujhe ? yad hai kitna chat krte the isse !
Aaj ka special message, Good Morning Mots :) ! Happy Weekend ! 
'''

response = create_request(URL,'4TDFVJGMCR4J72SU9R6R1QB42B60HFE0','DCSS0EJV5UMAW8HT','stage','9028316525','pythonCode',msg)
print(response.text)
