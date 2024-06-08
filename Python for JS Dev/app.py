from fastapi import FastAPI,UploadFile
import uvicorn

app = FastAPI()
# ye jo @ hai isko decorators kehtay hain
@app.get("/")
def home():
    return {"data": "Welcome to the home page."}
    
@app.get("/contact")
def contact():
    return {"data": "Welcome to the contact page."}

@app.post("/upload")
def upload(file:list[UploadFile]):
    print(file)
    return {'status': 'got the file'}

uvicorn.run(app)
