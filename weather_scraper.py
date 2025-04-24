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
    temp_text = temp_tag.text.strip().replace("°", "")
    try:
        temperature = int(temp_text)
    except ValueError:
        temperature = None
else:
    temperature = None

# Tarihi al
today = datetime.now().strftime("%Y-%m-%d")

# Veriyi hazırla
data = {
    "tarih": [today],
    "sehir": ["İstanbul"],
    "sicaklik": [temperature]
}

# Yeni veriyi DataFrame'e aktar
new_df = pd.DataFrame(data)

# CSV dosyası varsa oku, yoksa yeni oluştur
try:
    df = pd.read_csv("weather_data.csv")
    # Eğer bugünkü veri zaten varsa tekrar eklememesi için kontrol et
    if today not in df["tarih"].values:
        df = pd.concat([df, new_df], ignore_index=True)
        df.to_csv("weather_data.csv", index=False)
        print("Yeni veri eklendi.")
    else:
        print("Bugünün verisi zaten mevcut.")
except FileNotFoundError:
    new_df.to_csv("weather_data.csv", index=False)
    print("Yeni dosya oluşturuldu ve veri kaydedildi.")