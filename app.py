import streamlit as st 
from data import hotel_info
from datetime import datetime,date
import numpy as np
import pickle
import emoji
import warnings #Supressing version related warings
warnings.filterwarnings("ignore")

def predict_status(arr):

    input_arr = np.array(arr).reshape(1,-1)
    prediction = 0
    with open('model.pkl','rb') as f:
        model = pickle.load(f)
        prediction = model.predict(input_arr).reshape(-1)[0]
        
    return prediction



def book_room(category,booking_date,city,hotel,platform,room_class,check_in_date,no_guest,days_stay):

    input_vector = [
        0,0,0,0,0,0
    ]
    
    # number of guests
    input_vector[0] = no_guest,
    input_vector[0] = input_vector[0][0]

    # category
    input_vector[1] = 1 if category == 'Luxury' else 0

    #room_id
    if room_class == 'RT1':
        input_vector[2] = 1
    elif room_class == 'RT2':
        input_vector[2] = 2
    elif room_class == 'RT3':
        input_vector[2] = 3
    else:
        input_vector[2] = 4

    #day type
    if check_in_date.weekday() > 5:
        input_vector[3] = 1
    else :
        input_vector[3] =0
   
    # booking interval
    input_vector[4] = (check_in_date-booking_date).days

    #days stayed
    input_vector[5] = days_stay

    #booking platform
    platform_vector = [0,0,0,0,0,0]

    if platform == 'Direct online':
        platform_vector[0] = 1
    elif platform == 'Journey':
        platform_vector[1] = 1
    elif platform == 'Log trip':
        platform_vector[2] = 1
    elif platform == 'Make your trip':
        platform_vector[3] = 1
    elif platform == 'Others':
        platform_vector[4] = 1
    else:
        platform_vector[5] = 1

    input_vector.extend(platform_vector)

    #hotel name
    property_vector = [0,0,0,0,0,0]
    if hotel == 'Atliq Blu':
        property_vector[0] = 1
    elif hotel == 'Atliq City':
        property_vector[1] = 1
    elif hotel == 'Atliq Exotica':
        property_vector[2] = 1
    elif hotel == 'Atliq Grands':
        property_vector[3] = 1
    elif hotel == 'Atliq Palace':
        property_vector[4] = 1
    else:
        property_vector[5] = 1

    input_vector.extend(property_vector)

    # city
    city_vector = [0,0,0]

    if city == 'Delhi':
        city_vector[0]=1
    elif city == 'Hyderabad':
        city_vector[1]=1
    else:
        city_vector[2]=1

    input_vector.extend(city_vector)


    prediction = predict_status(input_vector)
    return prediction

if __name__ == '__main__':
    st.header("Customer Status Predictor")
    st.write("The accuracy of the model is approximate 63\%-67\%. Most of the time it will predict as checked out.")
    category = st.selectbox(
            label="Hotel Category (Luxury/Business)",
            options=['Luxury','Business']
        )

        
    city = st.selectbox(
        label='City',
        options= ['Delhi','Mumbai','Hyderabad','Bangalore']
    )
    
    @st.cache
    def get_hotels(category,city):
        return hotel_info[city][category]
    if True:
        st.session_state.opts = get_hotels(category=category,city=city)
    hotel = st.selectbox(
        label='Hotel',
        options=st.session_state.opts
    )


    platform = st.selectbox(
        label='Booking Platform',
        options=['Make your trip','Direct online','Direct Offline','Log trip','Journey','Tripster','Other']
    )

    room_class = st.selectbox(
        label='Room Class',
        options=['Standard','Elite','Premium','Presidental']
    )
    
    check_in_date = st.date_input('Check In Date')
    
    no_guest = st.number_input('Number of Guests',value=1,max_value=6,min_value=1)
    
    days_stay = st.number_input('Days Staying',value=1,min_value=1)

    book_now = st.button('Book Now')
    
    if book_now:

        result = book_room(
        category=category,
        city=city,
        hotel=hotel,
        platform=platform,
        room_class=room_class,
        check_in_date=check_in_date,
        booking_date=datetime.now().date(),
        no_guest=no_guest,
        days_stay = days_stay
    )

        if result == 0 or result == 1 :
            st.write("Room Booking was done successfully({}) and Costumer will expected to Check out {}.".format(emoji.emojize(':white_check_mark:'),emoji.emojize(':innocent:')))
        else:
            st.write("Room Booking was done successfully({}) and Costumer will expected to Cancel, Follow Up Required.. {}.".format(emoji.emojize(':white_check_mark:'),emoji.emojize(':disappointed:')))
        



