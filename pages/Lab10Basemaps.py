import streamlit as st 
import leafmap.foliumap as leafmap

st.set_page_config(layout = "wide")

col1, col2 = st.columns([4,1])

with col2:
    dropdown = st.selectbox("Basemap", ["Hybrid" , "Roadmap", "Terrain", "Satellite"])

    url = st.text_input("Enter URL")

m = leafmap.Map()
m.add_basemap(dropdown)

if url:
    m.add_tile_layer(url, name = "Tile Layer", attribution= " ")

with col1:
    m.to_streamlit()