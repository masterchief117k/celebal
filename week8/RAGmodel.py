from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

# Load your chunks
with open("loan_chunks.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

# Create embeddings using Hugging Face model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Index with FAISS
db = FAISS.from_texts(documents, embedding_model)
print(db)

# ✅ Add your OpenAI API key directly
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key="ssk-proj-qrGXj21wpZ28lu-dljDoxbzHjIvz-VuZGonqMCYSU4d8epb0fIQvWNWHrwt0iNYWiXIA27OmzvT3BlbkFJ50QFBn0Av2qjtGD308D573nBfBqpY7Hm0wT4PA-PRGIYkXfOGoiVKeqJ65JBIz83k6adqmc-sA"  #  Replace with your actual key
)

# Setup memory and QA chain
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 5}),
    memory=memory,
    return_source_documents=True
)

# Chat loop
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    response = qa_chain.invoke({"question": query})
print("Bot:", response["answer"])

