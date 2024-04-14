from colorama import Fore, Back, Style, init
import textwrap
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    Settings,
)

style = Style.BRIGHT + Fore.GREEN

# import llama_index.core
# Debug
# llama_index.core.set_global_handler("simple")


# Set the LLM, embedding model, node parser, and other settings
Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, max_tokens=112)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
Settings.context_window = 1800

documents = SimpleDirectoryReader("./books").load_data() # Load the documents from the "books" directory
db = chromadb.PersistentClient(path="./chroma_db") # initialize client, setting path to save data
chroma_collection = db.get_or_create_collection("alice_in_wonderland") # create collection

# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# # CREATE INDEX
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    show_progress=True
)

# LOAD INDEX from stored vectors
index = VectorStoreIndex.from_vector_store(
    vector_store,
    storage_context=storage_context
)


# =========== CHAT MODE ===========
pirate_style = "Answer like a pirate in funny accent about the book he wrote"
chat_engine = index.as_chat_engine(chat_mode="best", verbose=True)

response = chat_engine.chat("Who is Alexandru Zahar?" + pirate_style)
# response = chat_engine.chat("I thought the original author from Alice in Wonderland is someone else?" + pirate_style)


wrapped_text = textwrap.fill(response.response, 100)
print(style + wrapped_text)