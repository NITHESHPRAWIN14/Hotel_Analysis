import streamlit as st 
from data import hotel_info



if __name__ == '__main__':
    st.header("Customer Status Predictor")
    
    
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
        print('working...')
        return hotel_info[city][category]
    if True:
        st.session_state.opts = get_hotels(category=category,city=city)
    print(st.session_state.opts)
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
    
    no_guest = st.number_input('Number of Guests',value=0)
    
    days_stay = st.number_input('Days Staying',value=0)

    st.button('Book Now')



