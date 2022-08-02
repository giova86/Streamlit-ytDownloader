import streamlit as st
from pytube import YouTube
import os
import base64
import pytube.exceptions

def get_yt_obj(url):
	try:
		obj = YouTube(str(url))
		return obj
	except:
        #st.write('Insert a valid URL')
		return False

def download_file(stream):
    stream.download(filename=f'{stream.title}.mp3')

    with open(f'{stream.title}.mp3', 'rb') as f:
        bytes = f.read()
        b64 = base64.b64encode(bytes).decode()
        href = f'<a href="data:file/zip;base64,{b64}" download=\'{stream.title}.mp3\'>\
            Here is your link \
        </a>'
        st.markdown(href, unsafe_allow_html=True)

    os.remove(f'{stream.title}.mp3')

st.write("""
# YouTube Downloader
The easiest way to download Audio or Video from YouTube video
""")

yt_url = st.text_input('The URL link')
yt = get_yt_obj(yt_url)

if yt:
    st.video(yt_url)

    audios = yt.streams.filter(only_audio=True)

    st.write(f'Title: {yt.title}')
    st.write(f'Author: {yt.author}')

    # options = range(len(audios))
    # kbps = st.radio(
    #      "Options",
    #      (f' [ {j+1} ]  {i.abr}' for i,j in zip(audios, options))
    #      )

    options = [f'{i.abr}' for i in audios]
    st.subheader('Settings')
    index = st.selectbox("Select audio quality", range(len(options)), format_func=lambda x: options[x])

    # st.write("option:", options[index])
    # st.write("index:", index)
    st.subheader('Download')

    if st.button('Download'):

        audio = yt.streams.filter(only_audio=True)[int(index)]
        download_file(audio)

        # out_file = audio.download()
        #
        # # save the file
        # base, ext = os.path.splitext(out_file)
        # new_file = base + '.mp3'
        # os.rename(out_file, new_file)
