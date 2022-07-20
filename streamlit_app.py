import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('dp.png'))

st.header('Arpit Dutt Dixit, CS.')

st.info('Senior At Sir MVIT , Competitive Programmer, Developer and full time Data Enthusiast')

icon_size = 20

st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
st_button('twitter', 'https://twitter.com/thedataprof/', 'Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/arpit-dutt-dixit-59b631121/', 'LinkedIn', icon_size)
st_button('leetcode', 'https://leetcode.com/arpitdixitc23/', 'Leetcode Profile', icon_size)
