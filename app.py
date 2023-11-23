import streamlit as st
import requests
import pandas as pd
import datetime
from streamlit_folium import folium_static
import folium

st.markdown("""# NY taxi""")

if st.button('More 🎈🎈🎈 please!'):
    st.balloons()

df = pd.DataFrame({'first column': list(range(1, 9))})

d = st.date_input(
    "date",
    datetime.date(2019, 7, 6))

t = st.time_input('time', datetime.time(8, 45))

pickup_longitude = st.number_input('pickup_longitude',value = -73.989)
pickup_latitude = st.number_input('pickup_latitude',value=40.747)
dropoff_longitude = st.number_input('dropoff_longitude',value=-73.956)
dropoff_latitude = st.number_input('dropoff_latitude',value=40.802)
passenger_count= st.selectbox('Number of passengers', df['first column'],1)


params = {'pickup_datetime':f'{d} {t}',
          'pickup_longitude':pickup_longitude,
          'pickup_latitude':pickup_latitude,
          'dropoff_longitude':dropoff_longitude,
          'dropoff_latitude':dropoff_latitude,
          'passenger_count':passenger_count}


url = 'https://taxifare.lewagon.ai/predict'

if st.button('how much would it cost ?'):
    response = requests.get(url, params=params)
    cost = f"{response.json()['fare']} €"
    st.markdown(f"### {cost}")



# Fonction pour afficher la carte
def display_map(start, stop):

    m = folium.Map(location=start_coordinates, zoom_start=11, control_scale=True)
    m = folium.Map(location=stop_coordinates, zoom_start=11, control_scale=True)

    folium.Marker(start, popup='Start').add_to(m)
    folium.Marker(stop, popup='Stop').add_to(m)

    folium.PolyLine([start, stop], color="blue", weight=2.5, opacity=1).add_to(m)

    folium_static(m)

# Interface utilisateur Streamlit
st.title("Votre course de taxi")

# Coordonnées de départ et d'arrêt (à remplacer par les coordonnées réelles)
start_coordinates = [pickup_latitude, pickup_longitude]
stop_coordinates = [dropoff_latitude, dropoff_longitude]


# Appel de la fonction pour afficher la carte
display_map(start_coordinates, stop_coordinates)
