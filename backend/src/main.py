from typing import Union

from fastapi import FastAPI

from routes import auth

from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/sitemap")
def sitemap():
    routes = []

    for route in app.routes:
        path = route.__getattribute__("path")
        display_route = {
            "path": path, 
            "route": {
                "name": route.__getattribute__("name"),
                "methods": list(route.__getattribute__("methods"))
            }
        }
        routes.append(display_route)
        
    import json

    json_str = json.dumps(routes, indent=4, default=str)
    return Response(content=json_str, media_type='application/json')


app.include_router(router=auth.router)
