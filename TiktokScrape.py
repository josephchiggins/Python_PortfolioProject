from http import cookies
from os import link
from selenium import webdriver
import time 
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def downloadVideo(link, id):
    cookies = {
    '__cflb': '02DiuEcwseaiqqyPC5qr2kcTPpjPMVimukZUgKbo77aXd',
    '_ga': 'GA1.2.1733591920.1673897727',
    '_gid': 'GA1.2.1248322213.1673897727',
    '__gads': 'ID=b475569f9d1d5cbd-223d900586da00d0:T=1673897727:RT=1673897727:S=ALNI_MbKTJYMdhzwcuF00263lWrmQVhwhQ',
    '__gpi': 'UID=000009399e1e67cd:T=1673897727:RT=1673897727:S=ALNI_MaRd4JQ15tV0BUp0nkgNfH7wBksZQ',
    '_gat_UA-3524196-6': '1',
}

headers = {
    'authority': 'ssstik.io',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__cflb=02DiuEcwseaiqqyPC5qr2kcTPpjPMVimukZUgKbo77aXd; _ga=GA1.2.1733591920.1673897727; _gid=GA1.2.1248322213.1673897727; __gads=ID=b475569f9d1d5cbd-223d900586da00d0:T=1673897727:RT=1673897727:S=ALNI_MbKTJYMdhzwcuF00263lWrmQVhwhQ; __gpi=UID=000009399e1e67cd:T=1673897727:RT=1673897727:S=ALNI_MaRd4JQ15tV0BUp0nkgNfH7wBksZQ; _gat_UA-3524196-6=1',
    'hx-current-url': 'https://ssstik.io/en',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'referer': 'https://ssstik.io/en',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36',
}

params = {
    'url': 'dl',
}

data = {
    'id':link,
    'locale': 'en',
    'tt': 'S2FWOHpm',
}

response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)

downloadSoup = BeautifulSoup(response.text, "html.parser")

downloadLink = downloadSoup.a["href"]

mp4File = urlopen(downloadLink)
with open(f"videos/{id}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break


driver= webdriver.Chrome()
driver.get("https://www.tiktok.com/@lessworkmoresmart")

time.sleep(1)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1

while True:
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break 

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})


print(len(videos))

for index, videos in enumerate(videos):
    downloadVideo(videos.a["href"], index)

time.sleep(10) 

