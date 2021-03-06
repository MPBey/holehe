from holehe.core import *
from holehe.localuseragent import *


def babeshows(email):
    s=requests.session()
    headers = {
        'User-Agent': random.choice(ua["browsers"]["chrome"]),
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://www.babeshows.co.uk/member.php',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.babeshows.co.uk',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    r=s.get("https://www.babeshows.co.uk/member.php",headers=headers)
    if "Your request was blocked" in r.text or r.status_code!=200:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    headers['X-Requested-With']= 'XMLHttpRequest'


    params = (
        ('action', 'email_availability'),
    )
    try:
        data = {
          'email': email,
          'my_post_key':r.text.split('var my_post_key = "')[1].split('"')[0]
        }
    except:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    response = s.post('https://www.babeshows.co.uk/xmlhttp.php', headers=headers, params=params, data=data)
    if "Your request was blocked" not in response.text and response.status_code==200:
        if "email address that is already in use by another member." in response.text:
            return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
        else:
            return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
