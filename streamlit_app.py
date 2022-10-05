#importing general objects
import pandas as pd
import plotly.express as px
#importing streamlit
import streamlit as st

#reading and sorting the dataset
ds_jobs = pd.read_csv("ds_salaries.csv")
ds_jobs.drop(columns=['Unnamed: 0'], inplace=True)

# sorting by categorical colums with less than 20 categories
cat_feature1=[feature for feature in ds_jobs.columns if ds_jobs[feature].dtype=='O' and len(ds_jobs[feature].unique())<20]

#over 20 categories columns
cat_feature2=[feature for feature in ds_jobs.columns if ds_jobs[feature].dtype=='O' and len(ds_jobs[feature].unique())>20]

#discrete & continuous values for numerical columns
dis_feature=[feature for feature in ds_jobs.columns if len(ds_jobs[feature].unique())<20 and ds_jobs[feature].dtype!='O']

cont_feature=[feature for feature in ds_jobs.columns if len(ds_jobs[feature].unique())>20 and ds_jobs[feature].dtype!='O']


st.title('Data Science Jobs EDA')
st.write('Data science is the domain of study that deals with vast volumes of data using modern tools and techniques to find unseen patterns, derive meaningful information, and make business decisions. Data science uses complex machine learning algorithms to build predictive models.The data used for analysis can come from many different sources and presented in various formats. Data science is an essential part of many industries today, given the massive amounts of data that are produced, and is one of the most debated topics in IT circles. Its popularity has grown over the years, and companies have started implementing data science techniques to grow their business and increase customer satisfaction.')

#paiwise correlation of columns
fig=px.imshow(ds_jobs.corr(),text_auto=True,height=600,width=600,template='ggplot2',aspect='auto',title='<b>Paiwise Correlation of Columns</b>')
fig.update_layout(title_x=0.5)
st.plotly_chart(fig, use_container_width = True)

#top ds jobs and salaries
z=ds_jobs['job_title'].value_counts().head(10)
fig=px.bar(z,x=z.index,y=z.values,color=z.index,text=z.values,labels={'index':'job title','y':'count','text':'count'},template='seaborn',title='<b> Top 10 Popular Roles in Data Sceince')
st.plotly_chart(fig, use_container_width = True)
z=ds_jobs.groupby('job_title',as_index=False)['salary_in_usd'].mean().sort_values(by='salary_in_usd',ascending=False)
z['salary_in_usd']=round(z['salary_in_usd'],2)
fig=px.bar(z.head(10),x='job_title',y='salary_in_usd',color='job_title',labels={'job_title':'job title','salary_in_usd':'avg salary in usd'},text='salary_in_usd',template='seaborn',title='<b> Top 10 Roles in Data Science based on Average Pay')
fig.update_traces(textfont_size=8)
st.plotly_chart(fig, use_container_width = True)

st.header('You Can Further Visualize Elements of the Dataset by Selecting an Option Below')

#adding a side bar selection box for convenience
option = st.selectbox(
    'What Data Would You like to Visualize',
    ('Categorical (<20 categories)', 'Categorical (>20)', 'Numerical (Discrete)', 'Numerical (Continuous)', 'Treemap')
    ) 

#plotting with streamlit
if option == 'Categorical (<20 categories)':
  for feature in cat_feature1:
    fig = px.histogram(ds_jobs, x = feature)
    #fig.show()
    st.plotly_chart(fig, use_container_width = True)
elif option == 'Categorical (>20)':
  for feature in cat_feature2:
    fig = px.bar(ds_jobs, y = feature, x = 'salary')
    st.plotly_chart(fig, use_container_width = True)
elif option == 'Numerical (Discrete)':
  for feature in dis_feature:
    fig2 = px.histogram(ds_jobs, x=feature)
    st.plotly_chart(fig2, use_container_width = True)
elif option == 'Numerical (Continuous)':
  for feature in cont_feature:
    fig = px.box(ds_jobs, x = feature)
    st.plotly_chart(fig, use_container_width = True)
  for feature in cont_feature:
    fig1 = px.histogram(ds_jobs, x= feature, color="experience_level",   marginal="box", # can be `box`, `violin`
                         hover_data=ds_jobs.columns)
    st.plotly_chart(fig1, use_container_width = True)
elif option == 'Treemap':
  fig=px.treemap(ds_jobs,path=[px.Constant('Job Roles'),'job_title','company_location','experience_level'],template='ggplot2',hover_name='job_title',title='<b>TreeMap of Different Roles in Data Science with Experience Level')
  fig.update_traces(root_color='lightgrey')
  st.plotly_chart(fig)

st.header('Conclusions')

st.write('The maximum number of employees work as Data scientists across different countries.')
st.write('Mostly employees are senior experience leveled. Very few are expert level. The number of freshers decreased in 2022.')
st.write('Intuitively, more experienced employees achieve the highest salaries. The average salary of experts is at a maximum')
st.write('Data scientists mostly have senior or mid level experience, few are freshers and almost no data scientist has expert level experience. Data scientists from India tend to have mid and entry level experience.')
st.write('98% of empoyees work as full time and they get more payment as compare to contract, half time and freelencers.')
st.write('Most currency is USD based because there are maximum number of companies set up in the US, especially in 2022, the USA set up more companies and there employees get higher average payments.')
st.write('The mean of salary of all professional employees is $112298 approx. In 2022, employees show maximum average salary, but in India, 2021 has the maximum companies and Data scientists and in 2022 both are decreased.')