import requests
import bs4
from twocaptcha import TwoCaptcha
from dotenv import load_dotenv
import os

load_dotenv()
TwoCaptcha_api_key = os.getenv("TwoCaptcha_api_key")
renew_url = os.getenv("renew_url")
renew_session = requests.session()
renew_request = renew_session.get(renew_url)
renew_content = renew_request._content
renew_soup = bs4.BeautifulSoup(renew_content, 'lxml')
# sitekey
renew_sitekey = renew_soup.find('div', {"class":"g-recaptcha"})['data-sitekey']
# _token needed for the post request
renew_token = renew_soup.find('input', {"name":"_token"})['value']
solve = TwoCaptcha(TwoCaptcha_api_key)
result = solve.recaptcha(
    sitekey=renew_sitekey,
    url=renew_url)
#g-recaptcha-response
recaptcha_response = result['code']
postdata = {"username": "AAAAAAA", "g-recaptcha-response": f"{recaptcha_response}", "_token": f"{renew_token}" }
renew_post = renew_session.post(renew_url, data=postdata)
print(renew_post)