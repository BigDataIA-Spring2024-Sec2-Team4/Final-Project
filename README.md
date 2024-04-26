# BINGEWATCH

**One Stop Recommendation System** personalised recommendations for OTT Content. In an era saturated with entertainment options across numerous streaming platforms, finding the perfect show or movie can feel like searching for a needle in a haystack.

This is where we have a need for a consolidated movie recommendation system like BingeWatch. Our groundbreaking project designed to revolutionise how viewers discover and engage with content. 

With a focus on genre and mood-based filtering, as well as occasion-specific recommendations, the system promises to deliver personalised viewing suggestions tailored to individual preferences


## 🚀 Live Application

Experience the power of personalized content discovery:

[![Application](https://img.shields.io/badge/Application-008000?style=for-the-badge&&logoColor=white)](http://34.16.229.123:8501/)
[![Codelabs Tutorial](https://img.shields.io/badge/Codelabs_Tutorial-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1z-pGIA6HOZregKgnnslvBE-ZZRUS_rhmiQvnVc8Xoww#0)
[![Demo Video](https://img.shields.io/badge/Demo_Video-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/link-to-your-demo-video)


## 📜 Problem Statement

Users face decision fatigue due to an overwhelming amount of content across multiple streaming platforms. Existing recommendation systems operate in silos, failing to leverage cross-platform data for personalized recommendations. 

The Unified Streaming Content Recommendation System aims to solve this by:

1. Aggregating data from various streaming services for cross-platform content discovery.
2. Implementing advanced machine learning to analyze multi-dimensional user data (preferences, histories, contexts) for personalized recommendations.
3. Providing a user-friendly interface to streamline content discovery and reduce decision fatigue.
4. Continuously adapting recommendations through learning capabilities.
5. Offering valuable insights to streaming providers for targeted marketing and subscriber acquisition.

It will revolutionize the streaming experience with personalized, contextually relevant recommendations, enhancing user engagement while driving growth for providers.

## 🎯 Project Goals

Our mission is to:

- Enhance the user experience through genre, mood, and occasion-based recommendations.
- Increase user engagement and reduce decision-making time.
- Provide cross-platform insights for content strategies.

## 🏛️ Architecture 

Below is the architectural diagram showcasing the data flow and interaction between different components of BingeWatch:

![Architecture Diagram](https://github.com/BigDataIA-Spring2024-Sec2-Team4/Final-Project/assets/144851281/968f52ed-12c5-4e44-be70-6cdefc6f4721)

## 🔧 Technologies Used

Our solution leverages the following technologies:

[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com)
[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pinecone](https://img.shields.io/badge/Pinecone-FF6F00?style=for-the-badge&logo=pinecone&logoColor=white)](https://www.pinecone.io)
[![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![The Movie Database](https://img.shields.io/badge/TMDB-01D277?style=for-the-badge&logo=themoviedatabase&logoColor=white)](https://www.themoviedb.org)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com)
[![Apache Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)](https://airflow.apache.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)

## 📊 Data Sources

Our enriched dataset is compiled from diverse sources, ensuring a rich selection for recommendation:

- **Kaggle**: Curated datasets from a broad range of streaming content.
- **TMDb API**: Real-time data access to movies and TV shows metadata.

## 🛠 Pre-requisites

To get started with our system, you will need:

- Basic understanding of Python and data processing.
- Access to services such as GCP, Snowflake, and PostgreSQL.
- Familiarity with Docker for container management.

## 🗂 Project Structure

Organized and structured for scalability and ease of navigation:

``` 
.github
   |-- workflows
   |   |-- ci.yml
.gitignore
Dockerfile
README.md
airflow_rec
   |-- dags
   |   |-- __init__.py
   |   |-- data_extraction.py
   |-- src
   |   |-- __init__.py
   |   |-- data_cleaning.py
   |   |-- rag_implementation.py
   |   |-- similarity_search.py
   |   |-- snowflake_upload.py
   |   |-- trailer_extract.py
bingewatch.py
contentapi.py
db_module
   |-- __init__.py
   |-- db.py
   |-- user_handler.py
docker-compose.yaml
main.py
models
   |-- __init__.py
   |-- pydantic_validators.py
   |-- user_model.py
requirements.txt
unit_testing.py
utils.py
```

## 🖥 How to Run Application Locally

To embark on your BingeWatch journey:

1. Clone the repo.
2. Install the dependencies.
```
pip install -r requirements.txt
```
3. Run the Dockerfile to generate the image and run the Docker compose file to bring up the instances.
```
docker build -t <image_name> .
```
```
docker compose up -d
```
This is create an airflow instance, postgresDB, streamlit for frontend and fastapi for backend.

## 📚 References & Dataset

Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows/data

For detailed insights into our approach and methodology, visit:
- RAG - https://www.pinecone.io/learn/retrieval-augmented-generation/
- Speech Input - https://blog.futuresmart.ai/building-a-conversational-voice-chatbot-integrating-openais-speech-to-text-text-to-speech
- Recommendation systems - https://medium.com/dailymotion/reinvent-your-recommender-system-using-vector-database-and-opinion-mining-a4fadf97d020

## ✅ Learning Outcomes

The development of BingeWatch has enriched our team with knowledge in:

- Advanced machine learning model integration.
- Full-stack development and cloud-native application deployment.
- Creating a data-driven user interface with Streamlit.

## 👥 Team Information and Contribution

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

| Name     | Contribution % | Key Contributions                        |
|----------|----------------|------------------------------------------|
| Nidhi Kulkarni | 50%             | Airflow, Frontend, Backend, Data processing, Cloud Deployment           |
| Riya Singh | 50%             | RAG Implementation, Vector Database, LangChain, Airflow    |







