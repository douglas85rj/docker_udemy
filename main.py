from fastapi import FastAPI


App = FastAPI()


@app.get("/")

def read_root():
    return {"message": "Hello from a Dockerized FastAPI app"}
	
