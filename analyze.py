import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("weather_data.csv")
data["tarih"]=pd.to_datetime(data["tarih"])
data["sicaklik"]=data["sicaklik"].astype(str).str.replace("°C","").astype(float)

min_temp=data["sicaklik"].min()
max_temp=data["sicaklik"].max()
min_date=data.loc[data["sicaklik"]==min_temp,"tarih"].values[0]
max_date=data.loc[data["sicaklik"]==max_temp,"tarih"].values[0]
plt.figure(figsize=(10,5))
plt.plot(data["tarih"],data["sicaklik"],label="Sıcaklık",marker="o")

plt.scatter(min_date, min_temp, color='blue', label=f'Min: {min_temp}°C')
plt.scatter(max_date, max_temp, color='red', label=f'Max: {max_temp}°C')

plt.title('Günlük Sıcaklık Değişimi')
plt.xlabel('Tarih')
plt.ylabel('Sıcaklık (°C)')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sehirler=data["sehir"].unique()
print ("Şehirler:", sehirler)
data.head()