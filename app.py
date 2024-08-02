import os
import streamlit as st
from yt_dlp import YoutubeDL
import logging

# Configurazione del logging
logging.basicConfig(filename='download_errors.log', level=logging.ERROR)

def download_youtube_playlist_as_mp3(playlist_url, download_path='downloads'):
    # Crea la cartella di download se non esiste
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,  # Impostiamo a False per scaricare tutta la playlist
        'ignoreerrors': True,  # Ignora gli errori dei singoli video
        'logger': logging.getLogger(),  # Registra gli errori nel file di log
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=True)
        print(info_dict)
        if 'entries' in info_dict:
            for entry in info_dict['entries']:
                if entry:
                    try:
                        st.write(f"Ho scaricato: {entry['title']}")
                        ydl.process_ie_result(entry, download=True)
                    except Exception as e:
                        logging.error(f"Errore nel download/conversione di {entry['webpage_url']}: {e}")
                        st.write(f"Errore nel download/conversione di {entry['webpage_url']}: {e}")
        else:
            st.write(f"Scaricando: {info_dict['title']}")


    st.success("Download completato. Controlla download_errors.log per eventuali errori.")

# Interfaccia Streamlit
st.title("Downloader di Canzoni/Playlist di YouTube in formato MP3")
st.write("Inserisci l'URL della playlist di YouTube per scaricare le tracce audio in formato MP3.")

playlist_url = st.text_input("URL della Playlist di YouTube")
download_path = st.text_input("Percorso di Download", value='downloads')

if st.button("Scarica Playlist"):
    if playlist_url:
        with st.spinner("Download in corso..."):
            download_youtube_playlist_as_mp3(playlist_url, download_path)
            st.info("Download completato.")
    else:
        st.error("Per favore, inserisci un URL valido della playlist di YouTube.")
