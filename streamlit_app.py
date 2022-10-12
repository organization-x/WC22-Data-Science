#importing general objects
import pandas as pd
import plotly.express as px
import numpy as np
import streamlit as st

#TODO: reading in the dataset


#Some basic commands in streamlit -- you can find an amazing cheat sheet here: https://docs.streamlit.io/library/cheatsheet
st.title('Data Science Example EDA')
st.write('You should add your plots and code to this page, using the code we have as inspiration to get started. I created a sample dataset below using numpy and pandas to show you how to display tables and graphs.')
st.markdown("""---""")
#generate random data for my example dataframe -- howto: https://stackoverflow.com/questions/32752292/how-to-create-a-dataframe-of-random-integers-with-pandas
example_data = pd.DataFrame(np.random.randint(0,100,size=(150, 4)), columns=list('ABCD'))

#show off a bit of your data. 
st.header('The Data')
col1, col2 = st.columns(2) #here is how you can use columns in streamlit. 
col1.dataframe(example_data.head())
col2.markdown("\n") #add a line of empty space.
col2.markdown('This is an example _dataframe_ I made up. You can put your teams dataframe here if you want!') #you can add multiple items to each column.
col2.markdown('- **It is pretty cool that you can use multiple columns in streamlit** (and *markdown* too)!')
st.markdown("""---""")

st.header('Some Plots')
st.plotly_chart(px.histogram(example_data, x="C"))
st.plotly_chart(px.scatter(example_data, x="A", y="B"))
st.markdown("This is an example set of charts I made up. You can put your team's charts here if you want!")
st.markdown("""---""")

#Always good to section out your code for readability.
st.header('Conclusions')
st.markdown('- **Data Science is Fun!**')
st.markdown('- **The [Streamlit Cheatsheet](https://docs.streamlit.io/library/cheatsheet) is really useful.**')
