import requests
import builtins
from PIL import Image
import streamlit as slt
from streamlit_lottie import st_lottie
slt.set_page_config(page_title="Code Web",page_icon=":fish:",layout='wide')
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

def local_css(file_name):
    with open(file_name) as f:
        slt.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

slt.markdown(hide_style,unsafe_allow_html=True)
def load(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding1  = load("https://assets4.lottiefiles.com/private_files/lf30_wqypnpu5.json")
lottie_coding2 = load("https://assets4.lottiefiles.com/private_files/lf30_b8oxhxr5.json")

img1 = Image.open(('/home/harsh/Documents/Python Codes/one.jpeg'))
img2 = Image.open(('/home/harsh/Documents/Python Codes/two.png'))
slt.subheader('Hi! I am Harsh :wave:')
slt.title('A Python Web Developer')
slt.write("I'm passionate finding the ways to use python streamlit and website applications")
slt.write("[Follow my github and learn lot of codes > ](https://www.github.com/hvs1234)")
with slt.container():
    slt.write('---')
    left_column , right_column = slt.columns(2)
    with left_column:
        slt.header('What I do')
        slt.write('##')
        slt.write(
            """
            I'm currently studying in graphic era hill university. I learned lot of structures in python:
            - Know about GUI tkinter module.
            - Know about data visualization using pyplot which contains graph structures.
            - Know some other languages like C, C++, Java.
            - I Know advanced modules in Python to create a GUI and web design rather than other languages.

            If you guys want to get the questions and their codes of languages [C, C++, Java, Python], so please follow me
            in the github. My Github link is mentioned above.
            """
        )
    with right_column:
        st_lottie(lottie_coding1,height=400,key="Coding")

with slt.container():
    slt.write('---')
    slt.text('Learn about turlte graphics GUI python')
    slt.write('[Go to this link ...](https://github.com/hvs1234/GitDemo/tree/main/Learn%20GUI)')
    slt.write('---')
    slt.header('My Projects')
    image_column , text_column = slt.columns((1,2))
    with image_column:
        slt.image(img1,width=250)
    with text_column:
        slt.subheader("Build an *'Text Editor App'* using python module")
        slt.write("[Learn how to create text editor app >]"
            "(https://github.com/hvs1234/project/blob/master/Python%20Project/Text%20Editor%20By%20HVS.py)")
        slt.write('---')
        slt.text('This project contains GUI module and text module to built an cool app design.')

with slt.container():
    slt.write('---'); slt.write(' '); 
    image_column , text_column = slt.columns((1,2))
    with image_column:
        slt.image(img2,width=250)
    with text_column:
        slt.subheader("Build an *'Login System'* using python module")
        slt.write('[Learn how to create login system >]'
        '(https://github.com/hvs1234/project/blob/master/Python%20Project/Login.py)')
        slt.write('---')
        slt.text('This project contains GUI module and show label username and password to access it.')
slt.write('---')

with slt.container():
    slt.write('Get Touch With Me! :thought_balloon:'); slt.write("##")
    contact_form = """
    <form action="https://formsubmit.co/3469harshsharma@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    """
    left_column,right_column = slt.columns(2)
    with left_column:
        slt.markdown(contact_form,unsafe_allow_html=True)
        local_css("style/style.css")
    with right_column:
        st_lottie(lottie_coding2,height=350,key="Join Us")
slt.write('---')
slt.write('If you guys ask me something design a web, so send me your details above. Thanks!!!')
