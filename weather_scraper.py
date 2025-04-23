import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

url="https://weather.com/tr-TR/weather/today/l/80b7ab0e85646330a87786cb3b580a5c6a7611d99835fa3483339213a7f74071"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.content,"html.parser")
temp_tag=soup.find("span",attrs={"data-testid":"TemperatureValue"})
if temp_tag: 
    temp=temp_tag.text
    now=datetime.now().strftime("½Y-%M-%d %H:%M")
    data=pd.DataFrame([[now,temp]],columns=["Datetime","Temperature"])

 #CSV dosyasını kontrol eder varsa üzerine ekler yoksa oluşturur
    try:
        existing_data=pd.read_csv("weather_data.csv")
        data=pd.concat([existing_data,data],ignore_index=True)
    except FileNotFoundError:
        pass

    data.to_csv("weather_data.csv",index=False)
    print ("Hava durumu verisi kaydedildi.")

else:

    print("Hava durumu verisi alınamadı.")