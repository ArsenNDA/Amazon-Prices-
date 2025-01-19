from bs4 import BeautifulSoup
import requests
import smtplib
import dotenv

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


# site = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers).text # github example
# site = requests.get("https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M", headers=headers).text # real amazon
# site = requests.get("https://www.amazon.com/I16-PRO-MAX-Unlocked-Smartphone/dp/B0DK5X3R21/ref=sr_1_4?crid=32BPVGJFOGJ06&dib=eyJ2IjoiMSJ9.J-2nNUkqW9mvcwB_GitpwcR2qoxOpX3B7xSc_Zjd0j9iGej8dtBUF_iMyx10tfwaIkfmAWgv5kkDfK8Q0rjJPnlL7X3zJBLz0dSaF-1gj3XU4vl13L-m2I7F9U63xTmj2aZEZ0TG6Xjj5w7iy0hwl9b-fkU409nyhDj4V_I6Z2Nv3X9oib0rl6wJuP-lssIfYtSxcjVvKVSJzHGS_PHx759bPRJ_Jq5m6a09c9jHAoE.OJdn9Rhszm5FV-Vcp8pZ11zzecb6HR35i770gkMs0zg&dib_tag=se&keywords=iphone+16&qid=1735310468&sprefix=iphone+16+pro+max%2Caps%2C604&sr=8-4", headers=headers).text # real amazon
# site = requests.get("https://www.amazon.com/SAMSUNG-Smartphone-Unlocked-Processor-SM-S921UZKAXAA/dp/B0CMDRCZBJ/ref=sr_1_12_sspa?crid=3IC50C72ILWFE&dib=eyJ2IjoiMSJ9.ChKsxY4JYyc5LtS0xhiwvj0G9YvisqwsxnYtYZ5-qBC-38dOz-_RAmDyt6-6gdZQMtQ7ACLCPIt0nrzhCEv4jYGx98Y8RRPkni2h_1nZp-9uwnupttZYtLzq54hMNNrbmo_F2hLGFD2Hzsn9w4EDp8CVOUF42V3MbHXC61H4xwYW4m38b-ZgJz0CuYjB73F4Y4vjzJTB6E3OuDmccNtmUMenL79moiSNBioic6hi_E0.Bs0KlmpDTcAqSHNcaiz73-U5HiwA0XEIoov7MkcHPo4&dib_tag=se&keywords=samsung&qid=1735310612&sprefix=samsun%2Caps%2C296&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1", headers=headers).text # real amazon
site = requests.get("https://appbrewery.github.io/instant_pot/", headers=headers).text # github example

soup = BeautifulSoup(site, "html.parser")

price = float(soup.find("span", class_="a-price-whole").text)
price_cents = float((soup.find("span", class_="a-price-fraction").text))
price_cents = price_cents / 100
print(price)
print(price_cents)
final_price = price + price_cents
print(final_price)

my_email = dotenv.get_key(".env", "MY_EMAIL")
password = dotenv.get_key(".env", "PASSWORD")
smtp_adress = dotenv.get_key(".env", "SMTP_ADDRESS")

if final_price < 100.00:
    connection = smtplib.SMTP(host=smtp_adress, port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject:Price Drop!\n\nThe price dropped down to ${final_price}!"
    )
    print("Email sent!")
    connection.close()