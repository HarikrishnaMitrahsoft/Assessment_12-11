from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM, OllamaEmbeddings
import logging

embedding_function = OllamaEmbeddings(model="nomic-embed-text")
llmModel = OllamaLLM(model="deepseek-r1:1.5b")

logger = logging.getLogger(__name__)

def query_rag(query_text: str):
	# Load vector DB
	db = Chroma(persist_directory='./db', embedding_function=embedding_function)

	# Search top 3 results
	results = db.similarity_search_with_score(query_text, k=3)
	if not results:
		return "I couldn't find relevant clinic information."

	# Join context
	context_text = "\n---\n".join([doc.page_content for doc, _ in results])

	prompt = f"""
	You are a helpful medical assistant. Use the following clinic data to answer the user's question.

	Clinic Data:
	{context_text}

	User Question:
	{query_text}

	Answer clearly and concisely.
	"""

	# Prepare prompt
	prompt_template = ChatPromptTemplate.from_template(prompt)
	prompt = prompt_template.format(context=context_text, question=query_text)

	logger.info("\n🔹 Sending prompt to LLM...")
	response_text = llmModel.invoke(prompt)
	logger.info("Bot:", response_text)

	return response_text
