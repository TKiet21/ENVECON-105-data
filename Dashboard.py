#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import altair as alt


# In[3]:


st.set_page_config(
    page_title="Key Outputs From the Individual and the Group Projects",
    layout="wide",
    initial_sidebar_state="expanded")

st.title("Individual and Group Projects Key Plots - Kiet Hoa")

st.markdown(
    """ 
    This dashboard displays the key plots from the Individual and Group Projects from ENVECON 105 

    Please use the sidebar to select the country that you want to view plots from. 
    """
)

with st.sidebar:
    st.title("Please select a country")
    country_list = ["United States of America", "Vietnam", "World"]
    selected_country = st.selectbox('Select a country', country_list)

if selected_country == "United States of America":
    st.write("**Plots for the USA**")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/US%20plots/emissions_per_yr_indiv.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/US%20plots/dist_indiv.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/US%20plots/CO2_temp_US.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/US%20plots/US_emissions_temp.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/US%20plots/CO2_temp_US_scaled.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/US%20plots/summary_plot_indiv.png?raw=true")

elif selected_country == "Vietnam":
    st.write("**Plots for Vietnam**")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/VN%20plots/emissions_per_yr_group.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/VN%20plots/dist_group.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/VN%20plots/CO2_temp_VN.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/VN%20plots/VN_emissions_temp.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/VN%20plots/CO2_temp_VN_scaled.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/VN%20plots/summary_plot_group.png?raw=true")

else:
    st.write("**Plots for the World**")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/World%20plots/CO2_world.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/World%20plots/CO2_per_capita_world.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/World%20plots/top_10_line_indiv.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/World%20plots/top_10_line_groupnew.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/World%20plots/top_10_tile_indiv.png?raw=true")
    st.image("https://github.com/TKiet21/ENVECON-105-data/blob/main/World%20plots/top_10_tile_groupnew.png?raw=true")


# In[ ]:




