import http.client, urllib

class PushoverSender :
    def __init__(self, user_key, api_key):
        self.user_key = user_key
        self.api_key =  api_key
 
    def send_notification(self, text):
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        post_data = {'user': self.user_key, 'token': self.api_key, 'message': text}
        conn.request("POST", "/1/messages.json",
                     urllib.parse.urlencode(post_data), {"Content-type": "application/x-www-form-urlencoded"})
        # print(conn.getresponse().read())


class Sensors:
    def __init__(self,pushover):
        self.pushover=pushover
       
    def message(self):
        self.pushover.send_notification("amit")
       


#Add keys
#user_key=user kay
#api_key=appi key
pushover=PushoverSender(user_key,api_key)
s=Sensors(pushover)
for i in range (5):
    s.message()
