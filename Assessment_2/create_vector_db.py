import json
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
import os
import logging

logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Define paths
DATA_PATH = "data/clinic_info.json"
CHROMA_PATH = "./db"

def create_vector_db():
	# Load your clinic data
	with open(DATA_PATH, "r", encoding="utf-8") as f:
		clinic_data = json.load(f)

	# Convert JSON into readable text chunks
	documents = []

	def json_to_text(data, parent_key=""):
		"""Recursively flatten JSON into text"""
		text_blocks = []
		if isinstance(data, dict):
			for key, value in data.items():
				new_key = f"{parent_key} {key}".strip()
				text_blocks.extend(json_to_text(value, new_key))
		elif isinstance(data, list):
			for i, item in enumerate(data):
				new_key = f"{parent_key} item{i}".strip()
				text_blocks.extend(json_to_text(item, new_key))
		else:
			text_blocks.append(f"{parent_key}: {data}")
		return text_blocks

	flat_text = "\n".join(json_to_text(clinic_data))
	documents.append(Document(page_content=flat_text, metadata={"source": "data/clinic_info.json"}))

	# Initialize Ollama embeddings (local)
	embedding_fn = OllamaEmbeddings(model="nomic-embed-text")

	# Create or overwrite vector store
	if os.path.exists(CHROMA_PATH):
		import shutil
		shutil.rmtree(CHROMA_PATH)

	db = Chroma.from_documents(documents, embedding_fn, persist_directory=CHROMA_PATH)
	db.persist()
	print(f"✅ Vector database created successfully at: {CHROMA_PATH}")

if __name__ == "__main__":
	create_vector_db()