import streamlit as st
import pandas as pd
import math
import datetime


if st.session_state.get("logged_in", False):
    if st.button("Log Out", type="secondary"):
        st.session_state.logged_in = False
        st.switch_page("./login.py")
    
    #region [main logic]
    # test data storage
    st.title("Collection Profile")

    st.info("This dashboard displays the daily test data collection count and storage used.")

    def load_test_data():
        return pd.read_csv('./data/data.csv').sort_values(by=['date'], ascending=False)

    # store data in var test_data
    test_data = load_test_data()

    slider_size_threshold = st.slider("Select minimum file size (in MB)", 
                                    min_value=0.00, 
                                    max_value=pd.DataFrame(test_data, columns=["date", "filesize_mb"]).filesize_mb.max(), 
                                    step=50.00, 
                                    help="Minimum file size to be selected (in MB)")

    filter_size_data = test_data[test_data["filesize_mb"] >= slider_size_threshold]

    # bar chart
    st.subheader("Daily Total Size")
    st.bar_chart(pd.DataFrame(filter_size_data).groupby(['date'], as_index=False).sum().tail(14), x="date", y="filesize_mb", width=600) 

    # area chart - total count per tester
    st.subheader("Daily Total Count")
    area_series = test_data.groupby(['date'], as_index=False).count().tail(14)

    # area chart
    st.area_chart(area_series, x='date', y='hostname')

    # display data in table
    st.subheader("Details")
    st.write(test_data)

    #endregion

else:
    st.switch_page("./login.py")

