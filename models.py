from pydantic import BaseModel, Field


class Metadata(BaseModel):
    filename: str
    page: int


class Document(BaseModel):
    id: str
    text: str
    metadata: Metadata

class ReuestFile(BaseModel):
    db_type: str
    path: str


class ChromdbReuestFile(BaseModel):
    db_type: str
    path: str

class File(BaseModel):
    path: str

class ChromdbQuery(BaseModel):
    filename: str
    query: str
    top_k: int

class Query(BaseModel):
    db_type: str
    filename: str
    query: str
    top_k: int

class CustomddbQuery(BaseModel):
    query: str

class MilvusdbQuery(BaseModel):
    collection_name: str = Field(examples=["leetcode"])
    filename: str
    query: str
    top_k: int

class Solution(BaseModel):
    id: str | None = None
    collection: str
    problem_id: str