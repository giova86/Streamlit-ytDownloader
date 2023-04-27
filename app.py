import streamlit as st
import yt_dlp

# Impostiamo alcune opzioni predefinite per yt_dlp
ytdl_options = {
    "format": "bestvideo[height<=2160]+bestaudio/best[height<=2160]",
    "merge_output_format": "mkv",
}

# Impostiamo un'opzione per lo stile della pagina Streamlit
st.set_page_config(page_title="Scarica video da YouTube con yt_dlp")

# Aggiungiamo una descrizione della funzione dell'app
st.header("Scarica video da YouTube con yt_dlp")
st.write(
    "Quest'applicazione ti consente di scaricare un video da YouTube utilizzando la libreria yt_dlp."
)

# Aggiungiamo un campo di input per l'URL del video YouTube
url = st.text_input("Inserisci l'URL del video YouTube")

# Se è stato inserito un URL valido, procediamo con lo scaricamento
if url:

    st.video(url)

    if st.button('Download Video'):

        with st.spinner(text="Download in corso..."):
            try:
		        # Utilizziamo la libreria yt_dlp per scaricare il video
                with yt_dlp.YoutubeDL(ytdl_options) as ydl:
                    ydl.download([url])

		        # Mostraimo un messaggio di successo
                st.success("Download completato!")
            except Exception as e:
		        # Mostraimo un messaggio di errore se si verifica un problema con lo scaricamento
                st.error(f"Si è verificato un errore: {str(e)}")
