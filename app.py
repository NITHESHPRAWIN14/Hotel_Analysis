import streamlit as st 

if 'key' not in st.session_state:
    st.session_state['cities'] = []
    st.session_state['hotels'] =[]

from data import hotel_info



if __name__ == '__main__':
    st.markdown("<h1> Customer Status Predictor </h1>",unsafe_allow_html=True)
    category = st.selectbox(
            label="Hotel Category (Luxury/Business)",
            options=('Luxury','Business')
        )

    
    st.session_state.cities = list(hotel_info['city'].keys())
    city = st.selectbox(
        label='City',
        options= st.session_state.cities
    )
    
    st.session_state.hotels = list(hotel_info['city'][city][category])
    hotel = st.selectbox(
        label='Hotel',
        options=st.session_state.hotels
    )
    
    check_in_date = st.date_input('Check In Date')
    no_guest = st.number_input('Number of Guests',value=0)
    days_stay = st.number_input('Days Staying',value=0)