```
	poetry install
```

```
	poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

If face any issue with ollama,
	stop all ollama service and start

	Then use below command to run app with one worker,
		```
			poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
		```
