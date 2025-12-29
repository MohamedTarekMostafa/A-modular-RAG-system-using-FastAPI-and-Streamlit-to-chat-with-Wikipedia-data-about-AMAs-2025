import os
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import processor as poc

load_dotenv(".env")

def rag_chain():
    persist_dir = './chroma_db'
    embeddings = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')
    
    if os.path.exists(persist_dir):
        vector_store = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    else:
        print("Creating new Vector Store...")
        split = poc.get_split()
        vector_store = Chroma.from_documents(
            documents=split, 
            embedding=embeddings, 
            persist_directory=persist_dir
        )

    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    
    llm = ChatGroq(model='llama-3.3-70b-versatile', max_tokens=512, temperature=0)

    template = """ 
    Answer using ONLY the context:
    Context :{Context}
    Question : {Question}
    """
    prompt = PromptTemplate.from_template(template)
    
    def format_docs(docs):
        return "\n".join(doc.page_content for doc in docs)

    chain = (
        {"Context": retriever | format_docs, "Question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain