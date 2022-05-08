# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
from csv import DictReader

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# LOADING DATA
CITY = "City"
AREA = "Area"
VEHICLE_COUNT = "Number_Of_Vehicles"
#DATA_URL = (
#    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
#)

@st.experimental_memo
def load_data():
    data = pd.read_csv("Traffic_Monitor_Source.csv", sep=';')
    return data

data = load_data()

with st.container():
    st.title("Select City")
    city = st.selectbox("City", list(set(data[CITY])))


with st.container():
    cities = data[CITY]
    areas = data[AREA]

    index = 0
    areaList = []
    for currentCity in cities:
        if currentCity == city:
            areaList.append(areas[index])

        index = index + 1

    area = st.selectbox("Area", list(set(areaList)))

with st.container():

    if st.button("Generate graph"):
        cities = data[CITY]
        areas = data[AREA]
        vehicleCounts = data[VEHICLE_COUNT]
    
        numberOfVehicles = []
        index = 0

        for currentCity in cities:
            if currentCity == city:
                currentArea = areas[index]
                if currentArea == area:
                    numberOfVehicles.append(vehicleCounts[index])
            index = index + 1

        chart_data = pd.DataFrame(numberOfVehicles)
        st.bar_chart(chart_data)

