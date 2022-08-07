import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

col1, col2, col3 = st.columns(3)
col2.image(Image.open('sJyjnYUx_400x400.png'))

st.header('Arpit Dutt Dixit, CS.')

st.info('Senior At Sir MVIT , Competitive Programmer, Developer and full time Machine Learning Enthusiast')

icon_size = 20


st_button('github', 'https://github.com/dungeonmastae', 'Github', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/arpit-dutt-dixit-59b631121/', 'LinkedIn', icon_size)
st_button('leetcode', 'https://leetcode.com/arpitdixitc23/', 'Leetcode Profile', icon_size)
st_button('codeforces', 'https://codeforces.com/profile/ashwathamaa', 'Codeforces Profile', icon_size)
st_button('codechef', 'https://www.codechef.com/users/arpit121', 'Codechef Profile', icon_size)
