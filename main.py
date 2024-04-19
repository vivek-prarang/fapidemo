from fastapi import FastAPI,Response
from api import endpoints  

app = FastAPI()

app.include_router(endpoints.router, prefix="/api", tags=["Version 1"], responses={404: {"description": "Not found"}}, )
# app.include_router(endpoints.router, prefix="/api", tags=["Version 1"], responses={404: {"description": "Not found"}}, )
@app.get('/')
def root_endpoint():
    return 2
if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=1000, reload=True)