import requests
from bs4 import BeautifulSoup
import smtplib, ssl

urlList = ["https://www.amazon.es/Apple-Macbook-Pro-Ordenador-portátil/dp/B072K5XTLJ/ref=sr_1_1_sspa?keywords=macbook+pro&qid=1562616392&s=computers&sr=1-1-spons&psc=1", "https://www.amazon.es/Apple-MacBook-Pro-Ordenador-procesador/dp/B0721BNHJL/ref=sr_1_3?keywords=macbook+pro&qid=1562616392&s=computers&sr=1-3", "https://www.amazon.es/Apple-MacBook-pulgadas-núcleos-generación/dp/B07RZWGSHN/ref=sr_1_6?keywords=macbook+pro&qid=1562616392&s=computers&sr=1-6"]


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}

def check_price():    
    i = 0

    while i < len(urlList):
        page = requests.get(urlList[i], headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find(id="productTitle").get_text()
        price = (soup.find(id="priceblock_ourprice").get_text() + "thousand euros")
        converted_price = float(price[0:5])
        print(title.strip())
        print(converted_price)
        i = i + 1
    

def send_mail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "botaccount@mail.com"  # Enter your address
    receiver_email = "testemail@mail.com"  # Enter receiver address
    password = "xxxxxxxxxx"
    message = "Hey chack it out!"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    
check_price()
