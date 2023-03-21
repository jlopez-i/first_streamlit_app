import streamlit
import pandas

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# We want pandas to read our CSV file from that S3 bucket so we use a pandas function
#called read_csv  to pull the data into a dataframe we'll call my_fruit_list. 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#After pulling the data into a pandas dataframe called my_fruit_list, 
#we will ask the streamlit library to display it on the page by typing:

streamlit.dataframe(my_fruit_list)
