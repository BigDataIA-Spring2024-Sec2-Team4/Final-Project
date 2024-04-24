import streamlit as st
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from passlib.context import CryptContext  # Import CryptContext
from db_module.user_handler import create_user
import requests
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
from utils import speech_to_text
import os

float_init()


def clear_input():
    """ Clear the input field by resetting the session state variable. """
    st.session_state.input_ids = ''

def clear_input_name():
    """ Clear the input field by resetting the session state variable. """
    st.session_state.movie_name = ''    
# Create empty space on the left to push buttons to the right
def show_main_page():
    st.title('Binge Watch!')
    with st.popover("Pick a Type!"):
        content_type = st.radio("", ["movie", "tv_show"], index=0, on_change=clear_input)

# Allow user to enter a comma-separated list of IDs

    if 'input_ids' not in st.session_state:
        st.session_state.input_ids = ''

    #input_ids = st.text_input('Enter Unique IDs separated by commas:', value=st.session_state.get('input_ids', ''), key="input_ids")

    input1, input2 = st.columns([0.8, 0.2])
    with input2:
        audio_bytes = audio_recorder()

    if audio_bytes:
        with st.spinner("Transcribing..."):
            # Write the audio bytes to a temporary file
            webm_file_path = "temp_audio.mp3"
            with open(webm_file_path, "wb") as f:
                f.write(audio_bytes)

            # Convert the audio to text using the speech_to_text function
            transcript = speech_to_text(webm_file_path)
            if transcript:
                st.session_state.input_ids = transcript.strip()
                os.remove(webm_file_path)

    with input1:
    #    if 'input_ids' not in st.session_state:
    #        st.session_state.input_ids = ''

        input_ids = st.text_input('Enter Unique IDs separated by commas:', value=st.session_state.get('input_ids', ''), key="input_ids")


    if input_ids:
        # Split the input string into a list of IDs
        unique_ids = [id.strip() for id in input_ids.split(',')]
        
        # Send a GET request to the FastAPI endpoint with the list of IDs
        response = requests.get(f'http://fastapi:8001/content', params={'unique_ids': unique_ids, 'content_type': content_type})
        
        if response.status_code == 200:
            movies = response.json()
            
            # Define the number of columns for the grid
            columns_per_row = 4
            row = None
            
            for index, movie in enumerate(movies):
                # Create a new row every 'columns_per_row' movies
                if index % columns_per_row == 0:
                    row = st.columns(columns_per_row)
                
                # Determine the current position in the row
                col = row[index % columns_per_row]
                
                # Display movie details in the corresponding column
                with col:
                    if movie['thumbnail'] and movie['thumbnail'] != "No thumbnail available":
                        st.image(movie['thumbnail'], width=150)
                    else:
                        st.error("Thumbnail not available")
                    #st.image(movie['thumbnail'], width=150)  # Adjust width as needed
                    st.subheader(f"{movie['title']}")
                    st.write(f"Director: {movie['director']}")
                    st.write(f"Cast: {movie['cast_member']}")
                    st.write(f"Release Year: {movie['release_year']}")
                    st.write(f"Duration: {movie['duration']}")
                    st.write(f"Available on: {movie['available_on']}")
                    if movie['trailer'] != "No trailer available":
                        st.video(movie['trailer'], format='video/mp4', start_time=0)
                    else:
                        st.error("Trailer not available")
                    #st.video(movie['trailer'], format='video/mp4', start_time=0)

                    btn_col1, btn_col2 = st.columns(2)
                    with btn_col1:
                        if st.button(f"👍",key=f"like_{movie.get('unique_id', index)}"):
                        # store_feedback(movie['unique_id'], user_id, 'like')
                            st.write('You liked this movie!')
                    with btn_col2:
                        if st.button(f"👎",key=f"dislike_{movie.get('unique_id', index)}"):
                            #store_feedback(movie['unique_id'], user_id, 'dislike')
                            st.write('You disliked this movie!')
        else:
            st.error("Result not found!")
    else:
        st.info("Please enter one or more unique IDs separated by commas.")

    

def show_search_page():
    st.title("Search and Watch!")

    with st.popover("Pick a Type!"):
        content_type = st.radio("", ["movie", "tv_show"], index=0, on_change=clear_input)


    if 'movie_name' not in st.session_state:
        st.session_state.movie_name = ''

    #input_ids = st.text_input('Enter Unique IDs separated by commas:', value=st.session_state.get('input_ids', ''), key="input_ids")

    input1, input2 = st.columns([0.8, 0.2])
    with input2:
        audio_bytes = audio_recorder()

    if audio_bytes:
        with st.spinner("Transcribing..."):
            # Write the audio bytes to a temporary file
            webm_file_path = "temp_audio.mp3"
            with open(webm_file_path, "wb") as f:
                f.write(audio_bytes)

            # Convert the audio to text using the speech_to_text function
            transcript, error = speech_to_text(webm_file_path)
            if transcript:
                st.session_state.movie_name = transcript.strip()
                os.remove(webm_file_path)
            elif error:
                st.warning("Sorry, I couldn't catch that.")   

            else:
                return None     

    with input1:
    #    if 'input_ids' not in st.session_state:
    #        st.session_state.input_ids = ''

        movie_name = st.text_input("Enter movie name to search:", value=st.session_state.get('movie_name', ''), key="movie_name")
    
    
    if st.button("Search"):
        response = requests.get(f"http://fastapi:8001/content", params={"name": movie_name ,'content_type': content_type})
        if response.status_code == 200:
            movies = response.json()
            if movies:  # Check if the movies list is not empty
                columns_per_row = 4
                row = None
                
                for index, movie in enumerate(movies):
                    if index % columns_per_row == 0:
                        row = st.columns(columns_per_row)  # Create a new row every 'columns_per_row' movies
                    
                    col = row[index % columns_per_row]  # Determine the current position in the row
                    
                    with col:
                        # Display movie details in the corresponding column
                        thumbnail = movie.get('thumbnail', "No thumbnail available")
                        if thumbnail != "No thumbnail available":
                            st.image(thumbnail, width=150)
                        else:
                            st.error("Thumbnail not available")

                        st.subheader(f"{movie.get('title', 'Title not available')}")
                        st.write(f"Director: {movie.get('director', 'Director information not available')}")
                        st.write(f"Cast: {movie.get('cast_member', 'Cast information not available')}")
                        st.write(f"Release Year: {movie.get('release_year', 'Release year not available')}")
                        st.write(f"Available on: {movie.get('available_on', 'Availability information not available')}")

                        trailer = movie.get('trailer', "No trailer available")
                        if trailer != "No trailer available":
                            st.video(trailer, format='video/mp4', start_time=0)
                        else:
                            st.error("Trailer not available")
            else:
                st.error("No movies found matching the criteria.")
        else:
            st.error("Failed to fetch movies.")
    
def page_three():
    st.write("Welcome to Page Three!")

pages = {
    "Main Page": show_main_page,
    "Search Page": show_search_page,
    "History Page": page_three
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("",list(pages.keys()))

# Display the selected page with the content in the function
pages[page]()

# Define your User model
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    password = Column(String)

# Database connection
DATABASE_URL = "postgresql://airflow:airflow@postgres/airflow"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize password context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Initialize session state for loggedIn and userCreated flags
if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False
if 'userCreated' not in st.session_state:
    st.session_state['userCreated'] = False

headerSection = st.container()
userSection = st.container()

def verify_user(username, entered_password):
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
        if user and pwd_context.verify(entered_password, user.password):
            return True
        else:
            return False

def LoggedIn_Clicked(username, password):
    if verify_user(username, password):
        st.session_state['loggedIn'] = True
        st.session_state['userCreated'] = False  # Reset userCreated flag if it was set
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid username or password")

def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False

def show_login_page():
    with userSection:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username", placeholder="Enter your username")
        password = st.text_input("Password", key="login_password", placeholder="Enter your password", type="password")
        st.button("Login", on_click=LoggedIn_Clicked, args=(username, password))

def show_create_user_page():
    with userSection:
        st.subheader("Create User")
        # Create a form using the 'with' syntax
        with st.form(key='create_user_form'):
            username = st.text_input("Username", key="create_username", placeholder="Enter your username")
            password = st.text_input("Password", key="create_password", placeholder="Enter your password", type="password")
            # Place the submit button inside the form
            submit_button = st.form_submit_button("Create User")

            if submit_button:
                hashed_password = pwd_context.hash(password)
                user_details = {"username": username, "password": hashed_password}
                result = create_user(user_details, engine)
                if result['status_code'] == 201:
                    st.success("User created successfully. Please login.")
                    st.session_state['userCreated'] = True
                else:
                    st.error(f"Failed to create user: {result['description']}")

with headerSection:
    st.title("User Management")
    #show_main_page()


# Display the appropriate UI elements based on the application state
if not st.session_state['loggedIn']:
    if not st.session_state['userCreated']:
        show_create_user_page()
        show_login_page()
else:
    # If logged in, show logout option or other content
    st.button("Logout", on_click=LoggedOut_Clicked)