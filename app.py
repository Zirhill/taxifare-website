import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
# '''
# # TaxiFareModel front ::)
# '''
chart_data = pd.DataFrame(
    [[ 40.7830603 , -73.9712488]],
    columns=["lat", "lon"],
)

st.header(" 🗽 Taxi Fare can predict every trip in New York City... and beyond !!  ")

col01, col02, col03 =  st.columns(3)
with col01:
    st.write("")
with col02:
    st.header("🚕")
with col03:
    st.write("")


col1, col2, col3,col4 =  st.columns(4)
with col1:
    dateTime = st.time_input
    st.date_input('📆 Date input')
    st.write("------------------------")
    st.number_input('🌐 Pick up long')
    st.number_input('🌐 Pick up lat')
with col2:
    st.time_input('⌚ Time entry ')
    st.write("------------------------")
    st.number_input('📍 Drop of long')
    st.number_input('📍 Drop of lat')
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.button('Get fare 🏁')
with col3:
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.write("                        ")
    st.number_input('Number of travellers 👨‍👨‍👧‍👦')
with col4:
    st.pydeck_chart(
    pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
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

# st.write("------------------------")

# col11, col12, col13 =  st.columns(3)
# with col11:
#     st.write("")
# with col12:
#     st.button('Get fare 🏁')
# with col13:
#     st.write("")





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
