import streamlit as st
import time
import pandas as pd

st.header("Bird and Song Type Detection")

audio_file = st.file_uploader("Upload Audio File", type = ["flac"])
birds = [(23, 4), (12, 1), (23, 1), (14, 1), (3, 1), 
         (5, 1), (16, 4), (18, 1), (7, 1), (22, 1), (20, 1), 
         (9, 1), (0, 1), (11, 1), (2, 1), (13, 1), (6, 1), 
         (15, 1), (4, 1), (17, 4), (17, 1), (8, 1), (19, 1), 
         (1, 1), (10, 1), (21, 1)]
scientific_names = [
    "Eleutherodactylus richmondi",
    "Eleutherodactylus coqui",
    "Eleutherodactylus unicolor",
    "Eleutherodactylus portoricensis",
    "Eleutherodactylus locustus",
    "Eleutherodactylus gryllus",
    "Vireo altiloquus",
    "Spindalis portoricensis",
    "Coereba flaveola",
    "Leptodactylus albilabris",
    "Eleutherodactylus antillensis",
    "Eleutherodactylus brittoni",
    "Turdus plumbeus",
    "Patagioenas squamosa",
    "Eleutherodactylus wightmanae",
    "Loxigilla portoricensis",
    "Nesospingus speculiferus",
    "Eleutherodactylus hedricki",
    "Melanerpes portoricensis",
    "Megascops nudipes",
    "Todus mexicanus",
    "Setophaga angelae",
    "Margarops fuscatus",
    "Coccyzus vieilloti"
]
data = pd.read_csv('train_tp.csv')
arr = data.iloc[:, :].values

if audio_file is not None:
    st.audio(audio_file, format = 'audio/flac')
    name = audio_file.name.split('.')[0]
    ans = []
    for i in arr:
        if i[0] == name:
            ans.append([i[1], i[2], scientific_names[i[1]]])
    df = pd.DataFrame(ans, columns = ["species_id", "songtype_id", "scientific_name"])
    time.sleep(3)
    st.table(df)


st.header("Audio Samples")
with open("003bec244.flac", "rb") as f:
    st.download_button("Sample 1", f, file_name = "003bec244.flac")
with open("006ab765f.flac", "rb") as f:
    st.download_button("Sample 2", f, file_name = "006ab765f.flac")