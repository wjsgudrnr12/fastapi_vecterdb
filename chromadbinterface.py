import os
from PyPDF2 import PdfReader
from datastore import Datastore
from models import Document, ChromdbQuery, File

db = Datastore("chromadb")

class ChromadbInterface:
    def __init__(self):
        pass

    def some_method(self):
        pass


    def chromadb_load(self, file: File):
        filename = os.path.basename(file.path)
        fulltext = ""

        with open(file.path, "rb") as f:
            pdf = PdfReader(f)

            for page in pdf.pages:
                text = page.extract_text()
                chunks = [text[i:i+1000] for i in range(0, len(text), 900)]
                pageNum = pdf.get_page_number(page)
                fulltext += text

                for i, chunk in enumerate(chunks):
                    doc = Document(
                        id=f"{filename}-p{pageNum}-{i}",
                        text=chunk,
                        metadata={"filename": filename, "page": pageNum}
                    )
                    print("Upserting: ", doc.id)
                    db.upsert(doc)

        
        return {
            "filename": filename,
            "total_pages": len(pdf.pages),
            "data": "chromadb load ok"
        }
    
    def chromadb_query(self, query: ChromdbQuery) -> list[Document]:
        result = db.query(query.filename, query.query, query.top_k)

        print(result)
        return result
    

if __name__ == '__main__':

    chromadb = ChromadbInterface()
    file = File(path="sample.pdf")
    file.path = "sample.pdf"
    chromadb.chromadb_load(file)

    query = ChromdbQuery(filename="sample.pdf", query="이 논문의 내용은 어떤 내용이에요?", top_k=1)
    query.query ="이 논문의 내용은 어떤 내용이에요?"
    print(chromadb.chromadb_query(query))

    print(query)







    