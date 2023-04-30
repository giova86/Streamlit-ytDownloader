import streamlit as st
import yt_dlp
import os
from io import BytesIO
from PIL import Image

def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        "ignoreerrors": True,
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        filename = str(ydl.extract_info(video_url)["title"]) + ".mp3"
    return filename


base_path = os.path.dirname(os.path.realpath(__file__)).replace("p\\", "/") + '/'

# Impostiamo alcune opzioni predefinite per yt_dlp
ytdl_options = {
    "format": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
    "merge_output_format": "mkv",
    "ignoreerrors": True
}

# Impostiamo un'opzione per lo stile della pagina Streamlit
st.set_page_config(page_title="Audio & Video Downloader")


image = Image.open('cover.jpg')

st.image(image)


# Aggiungiamo una descrizione della funzione dell'app
# st.header("Scarica video da YouTube con yt_dlp")


# Aggiungiamo un campo di input per l'URL del video YouTube
url = st.text_input("Inserisci l'URL del video YouTube")

# Se è stato inserito un URL valido, procediamo con lo scaricamento
if url:


    st.video(url)

    tab1, tab2 = st.tabs(['Video', 'Audio'])

    with tab1:

        if st.button('Download Video', use_container_width=True):

            with st.spinner('Wait for it...'):
                try:
                    # Utilizziamo la libreria yt_dlp per scaricare il video
                    with yt_dlp.YoutubeDL(ytdl_options) as ydl:
                        # st.write(ydl)
                        filename = ydl.download([url])
                        st.write(filename)
                    # with open(filename, 'rb') as f:
                    #     file_bytes = BytesIO(f.read())
                    #     btn_down = st.download_button(label='Scarica Video', data=file_bytes, file_name=filename, mime='audio/mp3', use_container_width=True)
                    #     if btn_down:
                    #         os.remove(f"{base_path}{filename}")

                       # Mostraimo un messaggio di successo
                    st.success("Download completato!")
                except Exception as e:
                    # Mostraimo un messaggio di errore se si verifica un problema con lo scaricamento
                    st.error(f"Si è verificato un errore: {str(e)}")


    with tab2:
        if st.button("Estrai Traccia Audio", use_container_width=True):

            with st.spinner('Wait for it...'):
                filename = download_audio(url)
                st.success("Download completato!")
            # with open(filename, 'rb') as f:
            #     file_bytes = BytesIO(f.read())
            #     btn_down = st.download_button(label='Scarica Traccia Audio', data=file_bytes, file_name=filename, mime='audio/mp3', use_container_width=True)
            #     if btn_down:
            #         os.remove(f"{base_path}{filename}")


