from src.chatbot import query_rag

query = "Where is the clinic located?"
response = query_rag(query)
print("response", response)