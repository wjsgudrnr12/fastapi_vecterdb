import os
from PyPDF2 import PdfReader
from fastapi import FastAPI
from datastore import Datastore
from models import Query, File, ChromdbQuery, CustomddbQuery
from chromadbinterface import ChromadbInterface
from customdbinterface import CustomdbInterface

cdb_interface = ChromadbInterface()
cudb_interface = CustomdbInterface()


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

