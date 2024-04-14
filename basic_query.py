from colorama import Fore, Back, Style, init
import textwrap

from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    load_index_from_storage,
    StorageContext,
    Settings,
)
import llama_index.core

style = Style.BRIGHT + Fore.GREEN

# Debug
# llama_index.core.set_global_handler("simple")

# Set the LLM, embedding model, node parser, and other settings
Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.3, max_tokens=312)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.node_parser = SentenceSplitter(chunk_size=500, chunk_overlap=3)
Settings.context_window = 1800

# Load the documents from the "books" directory
documents = SimpleDirectoryReader("books").load_data()


# Create the Semantic index and persist it to disk
index = VectorStoreIndex.from_documents(documents, show_progress=True)
index.storage_context.persist()

# Load Context
storage_context = StorageContext.from_defaults(persist_dir="storage")

# Recreate index from storage_context
index = load_index_from_storage(storage_context=storage_context)

query_engine = index.as_query_engine()

pirate_style = "Answer like a pirate in funny accent about the book he wrote"
# response = query_engine.query("Who is the author of Alice in Wonderland?" + pirate_style)
response = query_engine.query("Who is Alexandru Zahar?" + pirate_style)
# response = query_engine.query("I thought the original author from Alice in Wonderland is someone else?" + pirate_style)
wrapped_text = textwrap.fill(response.response, 100)
print(style + wrapped_text)
print(response.source_nodes)
