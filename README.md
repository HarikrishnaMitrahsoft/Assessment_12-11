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

