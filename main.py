import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

df = pd.read_csv('titanic.csv')

#Title and more specific description
st.title("One Week Data Science Example")
st.header("Exploratory Data Analysis Using the Infamous Titanic Dataset")

st.caption(
    "Dataframe for the original dataset. Columns include: Passenger Age, Cabin, Location Embarked, FARE, Passenger Name, # of Parents/Children, PassengerId, Passenger Class, Sex, # of Siblings/Spouses, Survived, Ticket, Title, Family_Size. There are many unneeded columns that could help clean up the dataframe if removed."
)
st.table(df.iloc[0:5])

#Dropping unneeded columns ("Location, Title, Cabin, PassengerId")
df = df.drop(columns=['Location Embarked', 'Title', 'Cabin', 'PassengerId'])

#Moving survived column to the end
df = df.reindex(columns=[col for col in df.columns if col != 'Survived'] +
                ['Survived'])

#Drop null values
df = df.dropna()

st.caption(
    "After removing unneeded columns such as 'Location Embarked', 'Title', 'Cabin', 'PassengerId' and dropping rows with null values, the dataframe becomes much more readable."
)
st.table(df.iloc[0:5])
#Replace female values with 0 and male values with 1 to make them easier to plot
df['Sex'].replace({'FEMALE': 0, 'MALE': 1}, inplace=True)

#Storing charts
fig1 = px.histogram(df, x="Survived", color="Sex")
fig2 = px.box(df, x='Passenger Class', y='Family_Size')
fig3 = px.scatter(df, x='FARE', y='Family_Size', color='Passenger Class')
fig4 = sns.pairplot(data=df)

option = st.selectbox('Select a graph', ['Pairplot', 'Survived Histogram', 'Survived w/ Passenger Class Boxplot','Scatterplot'])

if option == 'Survived Histogram':
    st.plotly_chart(fig1)
    with st.expander("See analysis"):
        st.write(
            "This histogram depicts the number of survivers divided by sex. It shows that a larger proportion of survivers were female (233:83 female ratio compared to 109:470 male ratio)."
        )
elif option == 'Pairplot':
    #st.pyplot(fig4)
    with st.expander("See analysis"):
        st.write(
            "The pairplots show scatterplots between every single variable within the dataframe. Looking at pairplots can help you observe general relationships between variables and determine variables to look further into."
        )
elif option == 'Survived w/ Passenger Class Boxplot':
    st.plotly_chart(fig2)
    with st.expander("See analysis"):
        st.write(
            "Lower class(3) had the largest max value of 10 while the middle class and higher class had the same max value of 5. All box plots are right skewed with the lower class having the most outliers."
        )
elif option == 'Scatterplot':
    st.plotly_chart(fig3)
    with st.expander("See analysis"):
        st.write(
            "There is a negative relationship between passenger class and fare. As fare decreases, the passenger class decreases (lower class to higher class). This makes sense since ticket prices would be greater for higher class passengers. There is a slightly positive relationship between family size and passenger class. Generally, we can observe a larger family size with lower class passengers although there are some outliers within higher class observations."
        )