from app import create_app

# Preferred way of running FastAPI app:
# uvicorn main:app --reload

app = create_app()

if __name__ == "__main__":
    # Debug server
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
