# Import libraries
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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
#We want to filter the table data based on the fruits a customer will choose, so we'll pre-populate the list to set an example for the customer.
#We'll ask our app to put the list of selected fruits into a variable called fruits_selected. 
#Then, we'll ask our app to use the fruits in our fruits_selected list to pull rows from the full data set (and assign that data to a variable called fruits_to_show). 
#Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page. 

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display it on the page by typing:

streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

# New Text Entry Box and Send the Input to Fruityvice as Part of the API Call
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

# Just writes the data to the screen in JSON
#streamlit.text(fruityvice_response.json())

# Take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# Display it on the page as a Table
streamlit.dataframe(fruityvice_normalized)

# Let's Query Our Trial Account Metadata (commented)
# Let's Query Some Data, Instead
import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_cur.execute("select * from fruit_load_list")
#si no se ejecuta 'banana' cambiar por select * from pc_rivery_db.public.fruit_load_list

my_data_row = my_cur.fetchone()

#streamlit.text("Hello from Snowflake:")

streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)






