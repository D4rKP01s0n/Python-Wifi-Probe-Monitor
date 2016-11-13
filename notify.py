#    Uncomment the section for the service that you are using

######################  Pushover  ######################
#pushover_app_token = '' #    Add in your Pushover Application Token
#pushover_user_key = ''
#import httplib, urllib
######################  Telegram Bot  ######################
#    This requires the installation of "telepot" via "pip install telepot"
#import telepot
#t_botkey = '' #     This is the token/key of your bot, which can be obtained by messaging @BotFather
######################  Code  ######################
def notify(message, importance, thetype):
    if pushover_app_token and pushover_user_key:
        c = httplib.HTTPSConnection("api.pushover.net:443")
        c.request("POST", "/1/messages.json",
          urllib.urlencode({
              "token": pushover_app_token,
              "user": pushover_user_key,
              "message": message,
          }), { "Content-type": "application/x-www-form-urlencoded" })
        return c.getresponse()
    #if t_botkey:
        #t_bot = telepot.Bot(t_botkey)
        
