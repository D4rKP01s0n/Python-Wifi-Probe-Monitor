#    Uncomment the section for the service that you are using

######################  Pushover  ######################
#pushover_app_token = '' #    Add in your Pushover Application Token
#pushover_user_key = ''
#import httplib, urllib
######################  Telegram Bot  ######################

######################  Code  ######################
def notify(type, importance, message):
    if pushover_app_token and pushover_user_key:
        c = httplib.HTTPSConnection("api.pushover.net:443")
        c.request("POST", "/1/messages.json",
          urllib.urlencode({
              "token": pushover_app_token,
              "user": pushover_user_key,
              "message": message,
          }), { "Content-type": "application/x-www-form-urlencoded" })
        return c.getresponse()
