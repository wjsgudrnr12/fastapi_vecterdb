import os
from PyPDF2 import PdfReader
from fastapi import FastAPI
from datastore import Datastore
from models import *
from chromadbinterface import ChromadbInterface
from customdbinterface import CustomdbInterface
from milvusdbinterface import MilvusdbInterface

cdb_interface = ChromadbInterface()
cudb_interface = CustomdbInterface()
mdb_interface = MilvusdbInterface()


app = FastAPI()

@app.post("/chromadb/load")
async def load(file: File):
    return cdb_interface.chromadb_load(file)


@app.post("/customdb/load")
async def load(file: File):
    return cudb_interface.custom_load(file)


@app.post("/chromadb/query")
async def query(query: ChromdbQuery):
    return cdb_interface.chromadb_query(query)


@app.post("/customdb/query")
async def query(query: CustomddbQuery):
    return cudb_interface.custom_query(query) 

@app.post("/milvusdb/load")
async def load(file: File):
    return mdb_interface.milvusdb_load(file)

@app.get("/milvusdb/query")
async def query(query: MilvusdbQuery):
    return mdb_interface.milvusdb_query(query) 

@app.get("/milvusdb/problem/{id}")
async def query(problem_id: str):
    return 

@app.get("/milvusdb/solution/{id}")
async def query(solution: Solution):
    return 

