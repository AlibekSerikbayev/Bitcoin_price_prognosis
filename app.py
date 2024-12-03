# #api kodi 
# import streamlit as st
# import pandas as pd
# import joblib
# import requests

# # Modelni yuklash
# model = joblib.load('bitcoin_model.pkl')

# # CoinCap API orqali ma'lumot olish funksiyasi
# def get_bitcoin_data(api_key):
#     url = "https://api.coincap.io/v2/assets/bitcoin"
#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.json()["data"]
#     else:
#         return None

# # Interfeys
# st.title("Bitcoin Narxi Bashorati")
# st.write("Kelajakdagi Bitcoin narxini bashorat qiling")

# # API kalitni kiritish
# api_key = "6f820eae-b4d5-4577-8a25-c88d5e7244f3"  # API kalitini to'g'ridan-to'g'ri kodga kiritish

# # Foydalanuvchi kiritishi uchun form
# open_price = st.number_input("Open narxi:", min_value=0.0)
# high_price = st.number_input("High narxi:", min_value=0.0)
# low_price = st.number_input("Low narxi:", min_value=0.0)
# close_price = st.number_input("Close narxi:", min_value=0.0)
# volume = st.number_input("Volume:", min_value=0.0)

# # CoinCap API orqali ma'lumot olish
# bitcoin_data = get_bitcoin_data(api_key)

# if bitcoin_data:
#     # Ma'lumotlarni jadvalda ko'rsatish
#     data = {
#         "Parameter": ["Joriy narx (priceUsd)", "Narx (priceQuote)", "Oxirgi 24 soatlik hajm (volumeUsd24Hr)", 
#                       "Bozor ulushi o'zgarishi (percentExchangeVolume)", "24 soatlik savdo soni (tradesCount24Hr)", "Oxirgi yangilanish (updated)"],
#         "Value": [
#             f"${float(bitcoin_data['priceUsd']):,.2f}",
#             f"${float(bitcoin_data['priceQuote']):,.2f}",
#             f"${float(bitcoin_data['volumeUsd24Hr']):,.2f}",
#             f"{float(bitcoin_data['percentExchangeVolume']):,.2f}%",
#             bitcoin_data['tradesCount24Hr'],
#             bitcoin_data['updated']
#         ]
#     }

#     # Jadval ko'rinishida chiqarish
#     df = pd.DataFrame(data)
#     st.write(df)  # Jadvalda ko'rsatish
# else:
#     st.error("API orqali ma'lumotlarni olishda xatolik yuz berdi.")

# # Bashorat qilish
# if st.button("Bashorat qilish"):
#     input_data = pd.DataFrame({
#         'Open': [open_price],
#         'High': [high_price],
#         'Low': [low_price],
#         'Close': [close_price],
#         'Volume': [volume]
#     })
#     prediction = model.predict(input_data)[0]
#     st.write(f"Kelajakdagi narx: ${prediction:.2f}")

#     # Joriy narxni chiqarish
#     st.write(f"Joriy narx: {float(bitcoin_data['priceUsd']):,.2f}")




# import streamlit as st
# import pandas as pd
# import requests
# import joblib

# # API ma'lumotlarini olish
# def get_bitcoin_data():
#     url = "https://api.coincap.io/v2/assets/bitcoin"
#     headers = {"Authorization": "Bearer YOUR_API_KEY_HERE"}  # API kalitni shu yerga qo'shing
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()["data"]
#         return {
#             "volumeUsd24Hr": float(data["volumeUsd24Hr"]),
#             "priceUsd": float(data["priceUsd"])
#         }
#     else:
#         st.error("API ma'lumotlarini olishda xatolik yuz berdi!")
#         return None

# # Modelni yuklash
# model = joblib.load('bitcoin_model.pkl')

# # Interfeys
# st.title("Bitcoin Narxi Bashorati")
# st.write("Kelajakdagi Bitcoin narxini bashorat qiling")

# # API orqali ma'lumotlarni olish
# api_data = get_bitcoin_data()

# # Foydalanuvchi kiritishi uchun form
# open_price = st.number_input("Open narxi:", min_value=0.0)
# high_price = st.number_input("High narxi:", min_value=0.0)
# low_price = st.number_input("Low narxi:", min_value=0.0)
# close_price = st.number_input("Close narxi:", min_value=0.0)
# volume = st.number_input("Volume:", min_value=0.0, value=api_data["volumeUsd24Hr"] if api_data else 0.0)

# # Bashorat qilish
# if st.button("Bashorat qilish"):
#     input_data = pd.DataFrame({
#         'Open': [open_price],
#         'High': [high_price],
#         'Low': [low_price],
#         'Close': [close_price],
#         'Volume': [volume]
#     })
#     prediction = model.predict(input_data)[0]
#     st.write(f"Kelajakdagi narx: ${prediction:.2f}")

#     # Joriy narxni ko'rsatish
#     if api_data:
#         st.write(f"Joriy narx (priceUsd): ${api_data['priceUsd']:.2f}")




# import streamlit as st
# import pandas as pd
# import requests
# import joblib

# # CoinCap API'dan ma'lumot olish
# def get_bitcoin_data():
#     url = "https://api.coincap.io/v2/assets/bitcoin"
#     headers = {"Authorization": "6f820eae-b4d5-4577-8a25-c88d5e7244f3"}  # API kalitni shu yerga qo'shing
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()["data"]
#         return {
#             "open_price": float(data["priceUsd"]),
#             "low_price": float(data["low24Hr"]),
#             "close_price": float(data["priceUsd"]),
#             "volume": float(data["volumeUsd24Hr"])
#         }
#     else:
#         st.error("API ma'lumotlarini olishda xatolik yuz berdi!")
#         return None

# # Modelni yuklash
# model = joblib.load('bitcoin_model.pkl')

# # Interfeys
# st.title("Bitcoin Narxi Bashorati")
# st.write("Kelajakdagi Bitcoin narxini bashorat qiling")

# # API orqali ma'lumotlarni olish
# api_data = get_bitcoin_data()

# # Foydalanuvchi kiritishi uchun form
# open_price = st.number_input("Open narxi:", min_value=0.0, value=api_data["open_price"] if api_data else 0.0)
# high_price = st.number_input("High narxi:", min_value=0.0)
# low_price = st.number_input("Low narxi:", min_value=0.0, value=api_data["low_price"] if api_data else 0.0)
# close_price = st.number_input("Close narxi:", min_value=0.0, value=api_data["close_price"] if api_data else 0.0)
# volume = st.number_input("Volume:", min_value=0.0, value=api_data["volume"] if api_data else 0.0)

# # Bashorat qilish
# if st.button("Bashorat qilish"):
#     input_data = pd.DataFrame({
#         'Open': [open_price],
#         'High': [high_price],
#         'Low': [low_price],
#         'Close': [close_price],
#         'Volume': [volume]
#     })
#     prediction = model.predict(input_data)[0]
#     st.write(f"Kelajakdagi narx: ${prediction:.2f}")


# import streamlit as st
# import pandas as pd
# import requests
# import joblib
# import toml

# # API kalitini yuklash
# config = toml.load("secret.toml")
# api_key = config["api"]["key"]

# # CoinCap API'dan ma'lumot olish
# def get_bitcoin_data():
#     url = "https://api.coincap.io/v2/assets/bitcoin"
#     headers = {"Authorization": f"Bearer {api_key}"}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()["data"]
#         return {
#             "open_price": float(data["priceUsd"]),
#             "high_price": float(data["high24Hr"]),
#             "low_price": float(data["low24Hr"]),
#             "close_price": float(data["priceUsd"]),
#             "volume": float(data["volumeUsd24Hr"])
#         }
#     else:
#         st.error("API ma'lumotlarini olishda xatolik yuz berdi!")
#         return None

# # Modelni yuklash
# model = joblib.load('bitcoin_model.pkl')

# # Interfeys
# st.title("Bitcoin Narxi Bashorati")
# st.write("Kelajakdagi Bitcoin narxini bashorat qiling")

# # API orqali ma'lumotlarni olish
# api_data = get_bitcoin_data()

# # Foydalanuvchi kiritishi uchun form
# open_price = st.number_input("Open narxi:", min_value=0.0, value=api_data["open_price"] if api_data else 0.0)
# high_price = st.number_input("High narxi:", min_value=0.0, value=api_data["high_price"] if api_data else 0.0)
# low_price = st.number_input("Low narxi:", min_value=0.0, value=api_data["low_price"] if api_data else 0.0)
# close_price = st.number_input("Close narxi:", min_value=0.0, value=api_data["close_price"] if api_data else 0.0)
# volume = st.number_input("Volume:", min_value=0.0, value=api_data["volume"] if api_data else 0.0)

# # Bashorat qilish
# if st.button("Bashorat qilish"):
#     input_data = pd.DataFrame({
#         'Open': [open_price],
#         'High': [high_price],
#         'Low': [low_price],
#         'Close': [close_price],
#         'Volume': [volume]
#     })
#     prediction = model.predict(input_data)[0]
#     st.write(f"Kelajakdagi narx: ${prediction:.2f}")



# ishlaydigan kod


import streamlit as st
import pandas as pd
import joblib

# Modelni yuklash
model = joblib.load('bitcoin_model2.pkl')

# Interfeys
st.title("Bitcoin Narxi Bashorati")
st.write("Kelajakdagi Bitcoin narxini bashorat qiling")

# Foydalanuvchi kiritishi uchun form
open_price = st.number_input("Open narxi:", min_value=0.0)
high_price = st.number_input("High narxi:", min_value=0.0)
low_price = st.number_input("Low narxi:", min_value=0.0)
close_price = st.number_input("Close narxi:", min_value=0.0)
volume = st.number_input("Volume:", min_value=0.0)

# Bashorat qilish
if st.button("Bashorat qilish"):
    input_data = pd.DataFrame({
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Close': [close_price],
        'Volume': [volume]
    })
    prediction = model.predict(input_data)[0]
    st.write(f"Kelajakdagi narx: ${prediction:.2f}")
