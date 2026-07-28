from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from Jenkins + Docker + SonarQube!"}

@app.get("/health")
def health():
    return {"status": "Application is running"}
