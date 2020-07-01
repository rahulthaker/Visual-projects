import plotly.offline as py
import streamlit as st
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.figure_factory import create_table


#Data loading
@st.cache(persist=True)
def load_data():
    gapminder = px.data.gapminder()
    return gapminder


gapminder=load_data()

#Figures


fig_bubble=px.scatter(gapminder,x='gdpPercap',y='lifeExp',color='continent',size='pop',
                      size_max=60,hover_name='country',animation_frame='year',
                      animation_group='country',log_x=True,range_x=[100,100000],range_y=[25,90],
                      labels=dict(pop="Population",gdpPercap="GDP per Capita",lifeExp="Life Expectancy"))



#Streamlit
st.title('World view')
st.markdown('### This webapp is created by  Rahul Thaker play the animations and interact with them  ' \
            " \n \n Check out \n [My Linkedin](https://www.linkedin.com/in/rahul-t-634946141/)")

st.markdown('Hover over the bubble map to get more information')
st.plotly_chart(fig_bubble)


select=st.selectbox('Visualization Type',['orthographic','equirectangular', 'mercator', 'natural earth', 'kavrayskiy7', 'miller', 'robinson', 'eckert4' ])

chloro=px.choropleth(gapminder,locations="iso_alpha",color='lifeExp',hover_name='country',
                     animation_frame="year",color_continuous_scale=px.colors.sequential.Plasma,
                     projection=select)
st.markdown('Rotate  the  globe and hover over the map to get more data')
st.plotly_chart(chloro)
