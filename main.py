from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World v2.0 from GitHub Codespaces!"}

@app.get("/health")
def health():
    return {"status": "ok"}
