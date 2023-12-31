from src.utils.helper_function import predict
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()

class RequestData(BaseModel):
    text: str

@app.post("/api")
async def getPredict(data: RequestData):
    result = predict(data.text)
    # predict(data)
    return {"message": result}
 





# Entry point for your application

def main():
    print("Starting the server......")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)




if __name__ == "__main__":
    main()
