from pydantic import BaseModel


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
