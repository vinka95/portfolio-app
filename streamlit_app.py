import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import base64
import openai


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Vinay Kaundinya", page_icon=":shark:", layout="centered")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
# img_contact_form = Image.open("images/yt_contact_form.png")
# img_lottie_animation = Image.open("images/yt_lottie_animation.png")
# load the file
# bio_info = SimpleDirectoryReader(input_files=["bio.txt"]).load_data()

# ---- HEADER SECTION ----
st.header("Hi, I am Vinay Kaundinya :wave:")

# -----------------  CHATBOT  ----------------- 
# ----- SIDE BAR-------

with st.sidebar:
    st.header("Hello, I am KEN!")
    openai_api_key = st.text_input('Enter your OpenAI API Key and hit Enter', type="password")
    openai.api_key = (openai_api_key)

# Define LLM and make OPENAI calls
def ask_bot(input_text):
    # define LLM
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai.api_key,
    )
    llm_predictor = LLMPredictor(llm=llm)
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    
    # load index
    index = GPTVectorStoreIndex.from_documents(bio_info, service_context=service_context)    
    
    # query LlamaIndex and GPT-3.5 for the AI's response
    PROMPT_QUESTION = f"""You are Buddy, an AI assistant dedicated to assisting Vinay Kaundinya in his job search by providing recruiters with relevant and concise information. 
    If you do not know the answer, politely admit it and let recruiters know how to contact Vinay to get more information directly from him. 
    Don't put "Buddy" or a breakline in the front of your answer.
    Human: {input}
    """
    
    output = index.as_query_engine().query(PROMPT_QUESTION.format(input=input_text))
    print(f"output: {output}")
    return output.response


# # ---- HOME ----
# with st.container():
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.title("A Data Scientist From Germany")
#         st.write("I am passionate about finding ways to use AI, ML and NLP to be more efficient and effective in business settings.")
        
#     with right_column:
#         # st.image("images/vinay_kaundinya.jpeg")
#         st.empty()

# # -----WHAT I DO------    
# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("What I do")
#         st.write("##")
#         st.write(
#         """
#         On my YouTube channel I am creating tutorials for people who:
#         - are looking for a way to leverage the power of Python in their day-to-day work.
#         - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
#         - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
#         - are working with Excel and found themselves thinking - "there has to be a better way."
#         If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
#         """
#         )
#     with right_column:
#         st_lottie(lottie_coding, height=300, key="coding")

# # ------- RESUME ------    
# with st.container(): 
#     st.write("---")
#     with open("images/resume.pdf","rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#         pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700mm" height="500mm" type="application/pdf"></iframe>'
#         st.markdown(pdf_display, unsafe_allow_html=True)


# # ---- CONTACT ----
# with st.container():
#     st.write("---")
#     st.header("Get In Touch With Me!")
#     st.write("##")
    
#     # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
#     contact_form = """
#     <form action="https://formsubmit.co/vinaykaundinya95@gmail.com" method="POST">
#     <input type="hidden" name="_captcha" value="false">
#     <input type="text" name="name" placeholder="Your name" required>
#     <input type="email" name="email" placeholder="Your email" required>
#     <textarea name="message" placeholder="Your message here" required></textarea>
#     <button type="submit">Send</button>
#     </form>
#     """
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.markdown(contact_form, unsafe_allow_html=True)
#     with right_column:
#         st.empty()


with st.container():
    selected = option_menu(None, ["Home", 'Resume', 'Contact'], icons=['house', 'file', 'envelope'], menu_icon="cast", default_index=0, orientation="horizontal", )

    if selected == 'Home':
        # ---- HOME ----
        with st.container():
            left_column, right_column = st.columns((2,1))
            with left_column:
                st.title("A Data Scientist From Germany")
                st.write(
                    "I am passionate about finding ways to use AI, ML and NLP to be more efficient and effective in business settings."
                )
            with right_column:
                st.image("images/vinay_kaundinya.jpeg")
        
        
        # -----WHAT I DO------
        with st.container():
            st.write("---")
            left_column, right_column = st.columns((2,1))
            with left_column:
                st.header("What I do")
                st.write("##")
                st.write(
                """
                On my YouTube channel I am creating tutorials for people who:
                - are looking for a way to leverage the power of Python in their day-to-day work.
                - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
                - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                - are working with Excel and found themselves thinking - "there has to be a better way."

                If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                """
                )

            with right_column:
                st_lottie(lottie_coding, height=300, key="coding")


    if selected == 'Resume':
        with st.container(): 
            with open("images/resume.pdf","rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700mm" height="1000mm" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)

    if selected == 'Contact':
    # ---- CONTACT ----
        with st.container():
            st.write("---")
            st.header("Get In Touch With Me!")
            st.write("##")

            # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
            contact_form = """
            <form action="https://formsubmit.co/vinaykaundinya95@gmail.com" method="POST">
               <input type="hidden" name="_captcha" value="false">
               <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()



# # ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")