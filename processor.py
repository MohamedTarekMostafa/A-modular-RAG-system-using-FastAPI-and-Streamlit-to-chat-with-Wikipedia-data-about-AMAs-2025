import os
from langchain_community.document_loaders import WikipediaLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_split():
    if os.path.exists('./chroma_db'):
        return None 
    
    print("Fetching data from Wikipedia...")
    loader = WikipediaLoader(query='American Music Awards of 2025', lang='en', load_max_docs=1)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
    return splitter.split_documents(docs)