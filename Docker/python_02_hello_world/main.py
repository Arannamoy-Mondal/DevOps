from fastapi import FastAPI
import uvicorn
app=FastAPI()

@app.get("/")
def home():
    return "This is home page"


if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",reload=True,port=8000)
