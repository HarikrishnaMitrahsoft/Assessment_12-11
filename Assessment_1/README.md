```
	python -m venv venv
```
    venv\Scripts\activate
```
	pip install -r reurements.txxt
```
    uvicorn app.main:app --reload
```
    # (only first time)
    alembic init alembic
```
    # whenever models change
    alembic revision --autogenerate -m "Describe your change"
```
    # then apply those changes
    alembic upgrade head


```
    Build backend endpoints that simulate scheduling logic for a medical clinic.

	End Point 1: GET /api/calendly/availability (Eg : http://127.0.0.1:8000/api/calendly/availability?date=2024-01-16&appointment_type=consultation)
    End Point 2: POST /api/calendly/book (Eg : http://127.0.0.1:8000/api/calendly/book)

```

