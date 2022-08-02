import streamlit as st
from pytube import YouTube
import os

def get_yt_obj(url):
	try:
		obj = YouTube(url)
		return obj
	except:
        #st.write('Insert a valid URL')
		return False

st.write("""
# YouTube Downloader
The easiest way to download Audio or Video from YouTube video
""")

yt_url = st.text_input('The URL link')
yt = get_yt_obj(yt_url)

if yt:
    st.video(yt_url)

    audios = yt.streams.filter(only_audio=True, mime_type="audio/mp4")

    st.write(f'Title: {yt.title}')
    st.write(f'Author: {yt.author}')

    # options = range(len(audios))
    # kbps = st.radio(
    #      "Options",
    #      (f' [ {j+1} ]  {i.abr}' for i,j in zip(audios, options))
    #      )

    options = [f'{i.abr}' for i in audios]
    st.subheader('Download')
    index = st.selectbox("selectbox", range(len(options)), format_func=lambda x: options[x])

    # st.write("option:", options[index])
    # st.write("index:", index)

    if st.button('Download'):
        audio = yt.streams.filter(only_audio=True, mime_type="audio/mp4")[int(index)]

        out_file = audio.download(output_path='/dev/null')

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
