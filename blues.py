import requests
import random
from bs4 import BeautifulSoup

def blues(realname=None):

    if not realname:
        realname = str(random.randint(1,99999))

    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    url = "http://www.mess.be/inickgenbluesmalename.php"
    data = 'realname=%s&Submit=blues+me' % realname

    res = requests.post(url, headers=headers, data=data)


    soup = BeautifulSoup(res.content)
    soup = soup.find_all('center')[1].span
    name = " ".join(soup.getText().split())

    return name

if __name__ == '__main__':
    print blues()

