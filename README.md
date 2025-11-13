```
	Assessment 1 
```
    Build backend endpoints that simulate scheduling logic for a medical clinic.

	End Point 1: GET /api/calendly/availability (Eg : http://127.0.0.1:8000/api/calendly/availability?date=2024-01-16&appointment_type=consultation)
    End Point 2: POST /api/calendly/book (Eg : http://127.0.0.1:8000/api/calendly/book)

```
   	Assessment 2 
```
    Build a conversational FAQ agent that answers clinic-related queries using Retrieval-Augmented Generation.

	End Point 1: 
    ```
    curl -X GET http://0.0.0.0:8000/api/ask-faq `
     -H "Content-Type: application/json" `
     -d '{"query" : "availability of docker Meena"}'
     ```
