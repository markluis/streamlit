import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if st.session_state.get("logged_in", True):
    if st.button("Log Out", type="secondary"):
        st.session_state.logged_in = False
        st.switch_page("./login.py")
else:
    st.switch_page("./login.py")

st.title("Taylor Swift's Songs Profile")
def load_swift_data():
    return pd.read_csv('./data/swiftspot.csv')

tswift = load_swift_data()

df_tswift_album = tswift["album"].unique()

# st.write(df_tswift_album)

selectbox_album = st.selectbox("Taylor Swift's Album", df_tswift_album, index=None, placeholder="Select an album")

if selectbox_album != None:
    st.write("Album: ", selectbox_album)    
    tswift = tswift[tswift["album"] == selectbox_album]
else:
    st.info("Showing all album.")

# Scatter Plot - Dancability
st.subheader("Popularity relative to the song's `danceability`")
st.info("Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.")
splot = sns.scatterplot(x="danceability", y="popularity", data=tswift)
st.pyplot(splot.get_figure())

plt.clf()

# Scatter Plot - Valence
st.subheader("Popularity relative to the song's `valence`")
st.info("Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry)")
valence_splot = sns.scatterplot(x="valence", y="popularity", data=tswift)
st.pyplot(valence_splot.get_figure())

plt.clf()

# Scatter Plot - Liveness
st.subheader("Popularity relative to the song's `liveness`")
st.info("Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.")
liveness_plot = sns.scatterplot(data=tswift, x="liveness", y="popularity")
st.pyplot(liveness_plot.get_figure())
