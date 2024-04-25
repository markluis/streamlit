import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

if st.session_state.get("logged_in", True):
    if st.button("Log Out", type="secondary"):
        st.session_state.logged_in = False
        st.switch_page("./login.py")
else:
    st.switch_page("./login.py")

st.set_option('deprecation.showPyplotGlobalUse', False)

#region [ CSV Data Sources ]

def load_lyrics_fearless_data():
    lyrics = pd.read_csv('./data/swift_fearless_taylors_version.csv')["lyric"]
    lyrics_series = ', '.join(str(i) for i in lyrics)
    return lyrics_series

def load_lyrics_1989_data():
    lyrics = pd.read_csv('./data/swift_1989_deluxe.csv')["lyric"]
    lyrics_series = ', '.join(str(i) for i in lyrics)
    return lyrics_series

def load_lyrics_folklore_data():
    lyrics = pd.read_csv('./data/swift_folklore.csv')["lyric"]
    lyrics_series = ', '.join(str(i) for i in lyrics)
    return lyrics_series

def load_all_lyrics():
    return load_lyrics_fearless_data() + load_lyrics_1989_data() + load_lyrics_folklore_data()

#endregion

selectbox_album = st.selectbox("Taylor Swift's Album", ['Fearless', '1989', 'Folklore'], index=None, placeholder="Select an album")

if selectbox_album == None:
    # select all albums
    plt.clf()
    st.info("Displaying all albums!")
    wordcloudall = WordCloud().generate(load_all_lyrics())
    plt.imshow(wordcloudall, interpolation='antialiased')
    plt.axis("off")
    plt.show()
    st.pyplot()
else:
    # load selected album
    # st.write("Album: ", selectbox_album)
    sb_str = "Most common word in the album: " + selectbox_album
    st.info(sb_str)
    if selectbox_album == 'Fearless':
        plt.clf()
        wordcloud = WordCloud().generate(load_lyrics_fearless_data())
        plt.imshow(wordcloud, interpolation='antialiased')
        plt.axis("off")
        plt.show()
        st.pyplot()
    elif selectbox_album == '1989':
        plt.clf()
        wordcloud89 = WordCloud().generate(load_lyrics_1989_data())
        plt.imshow(wordcloud89, interpolation='antialiased')
        plt.axis("off")
        plt.show()
        st.pyplot()
    elif selectbox_album == 'Folklore':
        plt.clf()
        wordcloudfolklore = WordCloud().generate(load_lyrics_folklore_data())
        plt.imshow(wordcloudfolklore, interpolation='antialiased')
        plt.axis("off")
        plt.show()
        st.pyplot()
