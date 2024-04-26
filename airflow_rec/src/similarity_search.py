! pip install -q pandas
! pip install -q sentence-transformers
! pip install pinecone-client
! pip install -qU langchain-openai

import pandas as pd

"""# **Movie Suggestion**"""

# Load the CSV into a DataFrame
df = pd.read_csv('/content/final_movies.csv')

df = df[['sentences','unique_id']]

# Commented out IPython magic to ensure Python compatibility.
! pip install langchainhub
# %pip install --upgrade --quiet  langchain-pinecone langchain-openai langchain

from langchain.vectorstores import Pinecone as pic
from langchain_community.document_loaders import DataFrameLoader
from langchain.embeddings import OpenAIEmbeddings
from pinecone import ServerlessSpec, Pinecone
import os


index_name='bot'


pc = Pinecone(
    api_key='a2ca514b-4690-421b-9191-bf3d49719490'
)

os.environ['PINECONE_API_KEY'] = 'a2ca514b-4690-421b-9191-bf3d49719490'
os.environ["OPENAI_API_KEY"] = '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'
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )

loader = DataFrameLoader(df, page_content_column="sentences") # take pandas dataframe and convert it into langchain document
data = loader.load()

embeddings = OpenAIEmbeddings() #specifies which embeddings we are using, text into vectors -- langchain
vectorstore =  pic.from_documents( data, embeddings, index_name=index_name, namespace = 'movies') #convert and upsert the data

import pandas as pd

"""#Similarly for TV Shows"""

df = pd.read_csv('/content/final_tv_shows.csv')
df = df[['sentences','unique_id']]

loader = DataFrameLoader(df, page_content_column="sentences")
data = loader.load()

embeddings = OpenAIEmbeddings()
vectorstore =  pic.from_documents( data, embeddings, index_name=index_name, namespace = 'tv shows')

query = "Can you suggest a action movie or show?"

"""#Similarity Search"""

from langchain_pinecone import PineconeVectorStore

vector_store = PineconeVectorStore(
    pic.get_pinecone_index("bot"),
    embedding=embeddings,
    namespace="movies"
)

results = vector_store.similarity_search(query, k=16)

ids = ''
for result in results:
  ids += result.metadata['unique_id']
  if result != results[-1]:
    ids += ','
print(ids)