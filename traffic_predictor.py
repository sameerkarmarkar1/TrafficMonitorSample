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
TIMEFRAME = "Timeframe"
DATE = "Date"
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
        timeframes = data[TIMEFRAME]
        dates = data[DATE]

        vehiclesFrom8To11 = 0
        vehiclesFrom11To16 = 0
        vehiclesFrom16To19 = 0
        vehiclesFrom19To22 = 0


        vehiclesFrom8To11_0101 = 0
        vehiclesFrom11To16_0101 = 0
        vehiclesFrom16To19_0101 = 0
        vehiclesFrom19To22_0101 = 0

        vehiclesFrom8To11_0102 = 0
        vehiclesFrom11To16_0102 = 0
        vehiclesFrom16To19_0102 = 0
        vehiclesFrom19To22_0102 = 0

        vehiclesFrom8To11_0103 = 0
        vehiclesFrom11To16_0103 = 0
        vehiclesFrom16To19_0103 = 0
        vehiclesFrom19To22_0103 = 0

        vehiclesFrom8To11_0104 = 0
        vehiclesFrom11To16_0104 = 0
        vehiclesFrom16To19_0104 = 0
        vehiclesFrom19To22_0104 = 0

        vehiclesFrom8To11_0105 = 0
        vehiclesFrom11To16_0105 = 0
        vehiclesFrom16To19_0105 = 0
        vehiclesFrom19To22_0105 = 0

        vehiclesFrom8To11_0106 = 0
        vehiclesFrom11To16_0106 = 0
        vehiclesFrom16To19_0106 = 0
        vehiclesFrom19To22_0106 = 0

        vehiclesFrom8To11_0107 = 0
        vehiclesFrom11To16_0107 = 0
        vehiclesFrom16To19_0107 = 0
        vehiclesFrom19To22_0107 = 0

        numberOfVehicles = []
        index = 0

        for currentCity in cities:
            if currentCity == city:
                currentArea = areas[index]

                if currentArea == area:
                    currentTimeFrame = timeframes[index]
                    if currentTimeFrame == '8 to 11':
                        vehiclesFrom8To11 = vehiclesFrom8To11 + vehicleCounts[index]
                        if dates[index] == '01.01.22':
                            vehiclesFrom8To11_0101 = vehiclesFrom8To11_0101 + vehicleCounts[index]
                        elif dates[index] == '02.01.22':
                            vehiclesFrom8To11_0102 = vehiclesFrom8To11_0102 + vehicleCounts[index]
                        elif dates[index] == '03.01.22':
                            vehiclesFrom8To11_0103 = vehiclesFrom8To11_0103 + vehicleCounts[index]
                        elif dates[index] == '04.01.22':
                            vehiclesFrom8To11_0104 = vehiclesFrom8To11_0104 + vehicleCounts[index]
                        elif dates[index] == '05.01.22':
                            vehiclesFrom8To11_0105 = vehiclesFrom8To11_0105 + vehicleCounts[index]
                        elif dates[index] == '06.01.22':
                            vehiclesFrom8To11_0106 = vehiclesFrom8To11_0106 + vehicleCounts[index]
                        elif dates[index] == '07.01.22':
                            vehiclesFrom8To11_0107 = vehiclesFrom8To11_0107 + vehicleCounts[index]

                    elif currentTimeFrame == '11 to 16':
                        vehiclesFrom11To16 = vehiclesFrom11To16 + vehicleCounts[index]
                        if dates[index] == '01.01.22':
                            vehiclesFrom11To16_0101 = vehiclesFrom11To16_0101 + vehicleCounts[index]
                        elif dates[index] == '02.01.22':
                            vehiclesFrom11To16_0102 = vehiclesFrom11To16_0102 + vehicleCounts[index]
                        elif dates[index] == '03.01.22':
                            vehiclesFrom11To16_0103 = vehiclesFrom11To16_0103 + vehicleCounts[index]
                        elif dates[index] == '04.01.22':
                            vehiclesFrom11To16_0104 = vehiclesFrom11To16_0104 + vehicleCounts[index]
                        elif dates[index] == '05.01.22':
                            vehiclesFrom11To16_0105 = vehiclesFrom11To16_0105 + vehicleCounts[index]
                        elif dates[index] == '06.01.22':
                            vehiclesFrom11To16_0106 = vehiclesFrom11To16_0106 + vehicleCounts[index]
                        elif dates[index] == '07.01.22':
                            vehiclesFrom11To16_0107 = vehiclesFrom11To16_0107 + vehicleCounts[index]

                    elif currentTimeFrame == '16 to 19':
                        vehiclesFrom16To19 = vehiclesFrom16To19 + vehicleCounts[index]
                        if dates[index] == '01.01.22':
                            vehiclesFrom16To19_0101 = vehiclesFrom16To19_0101 + vehicleCounts[index]
                        elif dates[index] == '02.01.22':
                            vehiclesFrom16To19_0102 = vehiclesFrom16To19_0102 + vehicleCounts[index]
                        elif dates[index] == '03.01.22':
                            vehiclesFrom16To19_0103 = vehiclesFrom16To19_0103 + vehicleCounts[index]
                        elif dates[index] == '04.01.22':
                            vehiclesFrom16To19_0104 = vehiclesFrom16To19_0104 + vehicleCounts[index]
                        elif dates[index] == '05.01.22':
                            vehiclesFrom16To19_0105 = vehiclesFrom16To19_0105 + vehicleCounts[index]
                        elif dates[index] == '06.01.22':
                            vehiclesFrom16To19_0106 = vehiclesFrom16To19_0106 + vehicleCounts[index]
                        elif dates[index] == '07.01.22':
                            vehiclesFrom16To19_0107 = vehiclesFrom16To19_0107 + vehicleCounts[index]

                    elif currentTimeFrame == '19 to 22':
                        vehiclesFrom19To22 = vehiclesFrom19To22 + vehicleCounts[index]
                        if dates[index] == '01.01.22':
                            vehiclesFrom19To22_0101 = vehiclesFrom19To22_0101 + vehicleCounts[index]
                        elif dates[index] == '02.01.22':
                            vehiclesFrom19To22_0102 = vehiclesFrom19To22_0102 + vehicleCounts[index]
                        elif dates[index] == '03.01.22':
                            vehiclesFrom19To22_0103 = vehiclesFrom19To22_0103 + vehicleCounts[index]
                        elif dates[index] == '04.01.22':
                            vehiclesFrom19To22_0104 = vehiclesFrom19To22_0104 + vehicleCounts[index]
                        elif dates[index] == '05.01.22':
                            vehiclesFrom19To22_0105 = vehiclesFrom19To22_0105 + vehicleCounts[index]
                        elif dates[index] == '06.01.22':
                            vehiclesFrom19To22_0106 = vehiclesFrom19To22_0106 + vehicleCounts[index]
                        elif dates[index] == '07.01.22':
                            vehiclesFrom19To22_0107 = vehiclesFrom19To22_0107 + vehicleCounts[index]

            index = index + 1

        numberOfVehicles.append(vehiclesFrom8To11)
        numberOfVehicles.append(vehiclesFrom11To16)
        numberOfVehicles.append(vehiclesFrom16To19)
        numberOfVehicles.append(vehiclesFrom19To22)

        data = pd.DataFrame([[vehiclesFrom8To11, 'Total', '08 am to 11 pm'],
        [vehiclesFrom8To11_0101, '01 Jan', '08 am to 11 pm'],
        [vehiclesFrom8To11_0102, '02 Jan', '08 am to 11 pm'],
        [vehiclesFrom8To11_0103, '03 Jan', '08 am to 11 pm'],
        [vehiclesFrom8To11_0104, '04 Jan', '08 am to 11 pm'],
        [vehiclesFrom8To11_0105, '05 Jan', '08 am to 11 pm'],
        [vehiclesFrom8To11_0106, '06 Jan', '08 am to 11 pm'],
        [vehiclesFrom8To11_0107, '07 Jan', '08 am to 11 pm'],
        [vehiclesFrom11To16, 'Total', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0101, '01 Jan', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0102, '02 Jan', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0103, '03 Jan', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0104, '04 Jan', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0105, '05 Jan', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0106, '06 Jan', '11 pm to 16 pm'],
        [vehiclesFrom11To16_0107, '07 Jan', '11 pm to 16 pm'],
        [vehiclesFrom16To19, 'Total', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0101, '01 Jan', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0102, '02 Jan', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0103, '03 Jan', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0104, '04 Jan', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0105, '05 Jan', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0106, '06 Jan', '16 pm to 19 pm'],
        [vehiclesFrom16To19_0107, '07 Jan', '16 pm to 19 pm'],
        [vehiclesFrom19To22, 'Total', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0101, '01 Jan', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0102, '02 Jan', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0103, '03 Jan', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0104, '04 Jan', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0105, '05 Jan', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0106, '06 Jan', '19 pm to 22 pm'],
        [vehiclesFrom19To22_0107, '07 Jan', '19 pm to 22 pm']],
        columns = ['Vehicle count', 'Date', 'Timeframe'])

        gp_chart = alt.Chart(data).mark_bar().encode(
          alt.Column('Timeframe'), alt.X('Date'),
          alt.Y('Vehicle count', axis=alt.Axis(grid=False)),
          alt.Color('Date'))

        st.altair_chart(gp_chart, use_container_width=False)




