from fastapi import FastAPI,Response
from api import endpoints 
import json
app = FastAPI()

app.include_router(endpoints.router, prefix="/api", tags=["Version 1"], responses={404: {"description": "Not found"}}, )

@app.get('/')
def root_endpoint():
    response_data={'data':[1,2,3,4,5,7]}
    return Response(content=json.dumps(response_data), status_code=200, media_type="application/json")
if __name__=='__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=1000, reload=True)
