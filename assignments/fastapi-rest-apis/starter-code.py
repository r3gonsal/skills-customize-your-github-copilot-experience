from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="My FastAPI App", description="A simple REST API built with FastAPI")

class Item(BaseModel):
    name: str
    description: Optional[str] = None

# TODO: Add your endpoints here

@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI application!"}</content>
<parameter name="filePath">/workspaces/skills-customize-your-github-copilot-experience/assignments/fastapi-rest-apis/starter-code.py