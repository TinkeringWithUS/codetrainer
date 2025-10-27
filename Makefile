# Run backend
brun:
	cd backend && cd src && ../venv/bin/fastapi dev main.py

# Run frontend
frun:
	cd frontend && npm run dev

