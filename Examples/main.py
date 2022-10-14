import pandas as pd
import numpy as np
import plotly.express as px
import warnings 
import streamlit as st
warnings.filterwarnings("ignore") 

st.title('Data Science Salary EDA')
st.header('Target')
st.write('The target of this EDA is to draw conclusions about the viability of certain positions within the realm of Data Science based on numerous features including but not limited to salary, location, work experience, remote ratio, etc. This will be done through the use of comprehensive charts, tables, and maps that will paint an overall picture of the given dataset.')
# Data Exploration

df = pd.read_csv("./ds_salaries.csv")
st.write(df.head(10))

st.header('List of Features')
st.write(df.columns)

st.header('Value Counts For Each Feature')
st.write(df['work_year'].value_counts())
st.write(df['experience_level'].value_counts())
st.write(df['employment_type'].value_counts())
st.write(df['job_title'].value_counts())
st.write(df['salary_currency'].value_counts())
st.write(df['employee_residence'].value_counts())
st.write(df['remote_ratio'].value_counts())
st.write(df['company_location'].value_counts())
st.write(df['company_size'].value_counts())

st.header('Data Cleaning')
st.write('Here, upon reviewing the value counts and determining how valuable certain features would be compared to others, it was decided that salary and salary_currency would be dropped due to the third similar metric (salary_in_USD) being more workable for exploratory purposes.')

#Make a list of what you want to drop
columns_to_drop = ['salary', 'salary_currency']

#Drop the columns using drop()
df.drop(columns_to_drop, axis=1, inplace = True) #axis = 1 lets pandas know we are dropping columns, not rows.

#Check that they are dropped
st.write(df.head(5))

missing_df = (100*df.isnull().sum()/len(df)).to_frame()
missing_df.columns = ['percentage missing']
missing_df.sort_values(by = 'percentage missing')

st.header('Exploring Correlation')
df_corr = df.corr() # Generate correlation matrix
x = list(df_corr.columns)
y = list(df_corr.index)
z = np.array(df_corr)

fig = ff.create_annotated_heatmap(
    z,
    x = x,
    y = y ,
    annotation_text = np.around(z, decimals=2),
    hoverinfo='z',
    colorscale='Brwnyl',
    showscale=True,
    )
fig.update_xaxes(side="bottom")
fig.update_layout(
    # title_text='Heatmap', 
    title_x=0.5, 
    width=500, 
    height=500,
    yaxis_autorange='reversed',
    template='plotly_white'
)
st.write(' ')
st.write('Correlation Heatmap')
st.plotly_chart(fig)

fig = px.histogram(df, x="salary_in_usd", color='job_title', title = 'Salaries of Varying Job Titles',
                   color_discrete_map = {0:'#B99C6B',1:'#404F24'})
st.plotly_chart(fig)

fig = px.histogram(df, x="remote_ratio", title = 'Salaries of Occupation Location Type and Abundance',
                  color_discrete_map = {0:'#B99C6B',1:'#404F24'})
st.plotly_chart(fig)

st.header('Drawing Conclusions')
st.write('Based on the exploration performed, we can conclude a few things. We can conclude that the salaries for Data Science and Data Analysis positions have a truly broad range, from $40k all the way to $600k with the majority hovering around $100k. We can conclude that fully remote positions generally earn more and are more popular within the industry, nearly twice as popular as both in-office and hybrid positions. An addition thing worth noting is that the majority of instances in this dataset are from the US, and the minority being from nearly every other continent.')
st.write('')
