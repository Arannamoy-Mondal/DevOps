import fastapi 
import uvicorn

app=fastapi.FastAPI()


@app.get("/")
def home():
    return "Tested successfully."

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=3000)