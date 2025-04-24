import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("weather_data.csv")
data["tarih"]=pd.to_datetime(data["tarih"])
data=data.sort_values("tarih")

plt.figure(figsize=(10,6))
plt.plot(data["tarih"],data["sicaklik"],marker="o",linestyle="-", color="orange")
plt.title("Günlük Sıcaklık Değişimi")
plt.xlabel("Tarih")
plt.ylabel("Sıcaklık (°C)")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("sicaklik_degisimi.png")
plt.show()

min_temp=data["sicaklik"].min()
max_temp=data["sicaklik"].max()
mean_temp=data["sicaklik"].mean()

print(f"En düşük sıcaklık: {min_temp}°C")
print(f"En yüksek sıcaklık: {max_temp}°C")
print(f"Ortalama sıcaklık: {mean_temp:.2f}°C")

# Histogram (dağılım grafiği)
plt.figure(figsize=(8, 4))
plt.hist(data["sicaklik"], bins=10, color="skyblue", edgecolor="black")
plt.title("Sıcaklık Dağılımı")
plt.xlabel("Sıcaklık (°C)")
plt.ylabel("Frekans")
plt.tight_layout()
plt.savefig("sicaklik_histogram.png")
plt.show()