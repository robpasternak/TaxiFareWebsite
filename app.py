import streamlit as st
from datetime import datetime
import requests

'''
# Taxi Fare Estimator!

Enter the information for your taxi trip below, and we will give
you our best estimate for how much your trip will cost. We make
no guarantees about the accuracy of our predictions.

In the future we intend to add map functionality to make
inputting pickup and dropoff locations easier; in the meantime
these have to be put in manually.
'''

date = st.date_input('Day of Trip:')
time = st.time_input('Time of Trip (ET):')
date = date.strftime('%Y-%m-%d')
time = time.strftime('%H:%M:%S')
pickup_datetime = ' '.join([date, time])

pickup_longitude = st.text_input('Pickup Longitude:')
pickup_latitude = st.text_input('Pickup Latitude:')

dropoff_longitude = st.text_input('Dropoff Longitude:')
dropoff_latitude = st.text_input('Dropoff Latitude:')

passenger_count = st.text_input('Number of Passengers:')


url = 'https://taxifare.lewagon.ai/predict'

params = {
    'pickup_datetime' : pickup_datetime,
    'pickup_longitude' : float(pickup_longitude),
    'pickup_latitude' : float(pickup_latitude),
    'dropoff_longitude' : float(dropoff_longitude),
    'dropoff_latitude' : float(dropoff_latitude),
    'passenger_count' : int(passenger_count),
}

fare = requests.get(url, params = params).json()['fare']

st.markdown(f'## Predicted Fare: ${round(fare,2)}')
