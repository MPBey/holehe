from holehe.core import *
from holehe.localuseragent import *

def ello(email):

    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': 'application/json',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://ello.co/join',
        'Content-Type': 'application/json',
        'Origin': 'https://ello.co',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    data = '{"email":"' + email + '"}'
    try:
        response = requests.post('https://ello.co/api/v2/availability',headers=headers,data=data)
        if response.json()["availability"]["email"] == True:
            return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
        else:
            return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
    except:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
