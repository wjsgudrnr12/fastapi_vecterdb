import os
import csv
from openai import OpenAI

import numpy as np
from pprint import pprint

from models import ReuestFile
from dotenv import load_dotenv

load_dotenv()

faq_db = []
api_key = os.getenv('OPENAI_API_KEY')
openAIclient = OpenAI(api_key=api_key)

class CustomdbInterface: 
    def custom_load(self, file):

        # print(file.path)
        with open(file.path, 'r', encoding='utf-8') as fp:
            cr = csv.reader(fp)
            next(cr)

            for row in cr:
                # row: id,question,answer
                text = "Question: " + row[1] + "\nAnswer: " + row[2] + "\n"
                vector = self.get_embedding(text)
                doc = {'id': row[0], 'vector': vector,
                    'question': row[1], 'answer': row[2]}
                faq_db.append(doc)

        return faq_db


    def get_embedding(self, content, model='text-embedding-ada-002'):
        response = openAIclient.embeddings.create(input=content, model=model)
        vector = response.data[0].embedding
        return vector


    def similarity(self, v1, v2):  # return dot product of two vectors
        return np.dot(v1, v2)


    # def custom_query(self, vector, db):
    def custom_query(self, query):

        results = []
        vector = self.get_embedding(query.query)
        # print(vector)
        
        for doc in faq_db:
            # print(doc)
            score = self.similarity(vector, doc['vector'])
            results.append(
                {'id': doc['id'], 'score': score, 'question': doc['question'], 'answer': doc['answer']})

        results = sorted(results, key=lambda e: e['score'], reverse=True)
        # print("data\n\n")
        # print(results)

        return results


if __name__ == '__main__':
    db = CustomdbInterface()
    file = ReuestFile(db_type='customdb', path='prompt-faq.csv')

    faq_db = db.custom_load(file)
    # print(faq_db)
    # print(faq_db)

    question = "ReAct가 뭔가요?"
    vector = db.get_embedding(question)
    # print(question, vector)

    result = db.custom_query(vector, faq_db)
    pprint(result)
