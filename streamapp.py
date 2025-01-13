import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
# here we are importing the neccessary libraries required for the streamlit model

st.sidebar.title("Here we hare making a model for predicting the fitnesss score of the person ")

st.sidebar.markdown("by entering the age and the miles run the score can be calculated")
#st.image("/Users/Lenovo/Desktop/house pic.jpeg" ,use_container_width=True)

# // if selected_page == "Home":
    # st.title("Welcome to the Home Page")
    # st.write("This is the main page of your app.")
# elif selected_page == "predection model":
st.title("enter the values")
st.write("Learn more about our app and its purpose.")
 # we have also created a sidebar which will be use
df = pd.read_csv("cardio_cleaned_dataset.csv")
st.title("This is the dataset which we have")
st.write(df.head(6))

st.subheader("we have a dataset which has the age and the fitnesss score of a certain group of people ")

plt.figure(figsize=(5,5), dpi = 200)
sns.histplot(df['Age'],bins = 11 , kde = True, color = 'red')
plt.title('DISTRIBUTION OF AGE IN CARDIO CSV FILE')
p=10
plt.xlabel('Age' ,fontsize= p)
plt.ylabel('Frequency' , fontsize= p)

st.pyplot(plt)
# here we have displayed a plot for making the age and the frequency of the

st.write(df.describe())
# this describes the data 

# now we are going to make dataset with having to select the coloumns and the unqiue values

st.subheader("chose the value of the coloumns")
columns_select = df.columns.tolist()
selected_columns = st.radio("select the desired coloumns" , columns_select)
unique_values = df[selected_columns].unique()
selected_values = st.selectbox("selectd cloumns values" , unique_values)


# we are now going to make a 

filter_df = df[df[selected_columns]== selected_values]
st.write(filter_df)

# this gives us the filtered data and dynamically changes upon clicking the selectbox
# filtering this we get how we can get the values unique and the


