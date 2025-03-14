import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import requests
import datetime
# '''
# # TaxiFareModel front ::)
# '''


chart_data = pd.DataFrame(
    [[40.7830603 , -73.9712488]],
    columns=["lat", "lon"]
)


st.header(" 🗽 Taxi Fare can predict every trip in New York City... and beyond !!  ")

# juste le logo
col01, col02, col03 =  st.columns(3)
with col01:
    st.write("")
with col02:
    st.header("🚕")
with col03:
    st.write("")

base_url = 'https://taxifare.lewagon.ai/predict'

col1, col2, col3,col4 =  st.columns(4)
with col1:

    pick_date = st.date_input('📆 Date input')

    pickup_date = pick_date

    st.write("------------------------")
    pick_long =st.number_input('🌐 Pick up long', value=-73.9712488)
    pick_lat = st.number_input('🌐 Pick up lat', value=40.7830603)
with col2: #  colomne 2
    pick_time = st.time_input('⌚ Time entry ')
    pickup_time = pick_time

        # traitement de la date et l heure
    pickup_datetime = f'{pickup_date} {pickup_time}'

    st.write("------------------------")
    drop_long = st.number_input('📍 Drop of long', value=-73.9715)
    drop_lat = st.number_input('📍 Drop of lat', value=40.78307)
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")

with col3: #   slider passager
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    nb_trav =  st.slider('Number of travellers 👨‍👨‍👧‍👦', min_value=1, max_value=8)
    st.write("                        ")
    st.write("                        ")

    if st.button('Get fare 🏁'):
        params = {"pickup_longitude": pick_long, "pickup_latitude": pick_lat, "dropoff_longitude": drop_long, "dropoff_latitude": drop_lat,"passenger_count": nb_trav, "pickup_datetime" : pickup_datetime}

        response = requests.get(base_url, params=params)
        # st.write('hello 👋')
        # print("Réponse JSON:", response.json())
        # st.json(response.json())
        prediction = response.json()
        pred = prediction['fare']
        st.header(f'Fare amount: ${round(pred, 2)}')

        # if response.status_code == 200:
        #     print("Réponse JSON:", response.json())
        # else:
        #     print("Erreur:", response.status_code)


with col4:  # La CARTE
    st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=40.7830603 , # position de manhatan
            longitude=-73.9712488,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",
                get_radius=200,
            ),
        ],
    )
)


col001, col002, col003 =  st.columns(3)
with col001:
    st.write("")




with col002:  # cela sert juste a aligner a gauche
    st.write("")
with col003:
    st.write("")



# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')
# "add something"
# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''
