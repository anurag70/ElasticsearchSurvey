from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from elasticsearch_dsl import Search,Q
import  os, re
import pandas as pd
import csv,os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from elasticsearch import Elasticsearch, helpers


def extract_numeric_salary(salary_str):
    matches = re.findall(r'\b\d[\d,]*\b', salary_str.replace('$', '').replace(',', ''))
    if matches:
        numeric_salary = ''.join(matches)
        return float(numeric_salary)
     
    if 'plus bonus' in salary_str.lower():
        bonus_match = re.search(r'\b\d[\d,]*\b', salary_str.lower())
        if bonus_match:
            return float(bonus_match.group())
         
    if '+' in salary_str:
        parts = salary_str.split('+')
        numeric_values = [extract_numeric_salary(part) for part in parts]
        return sum(filter(None, numeric_values))
     
    return None


def preprocess_salary(row):
   
    row["Salary"] = extract_numeric_salary(row["Salary"])
    return row

def get_mapping_from_csv(file_path):
   with open(file_path, 'r', encoding='utf-8') as f:
      sample_data = pd.read_csv(file_path, nrows=5, na_values=[""])

   # Generate a dynamic mapping based on data types
   mapping = {
   "mappings": {
      "properties": {
      }
   }
}

   for column in sample_data.columns:
      try:
         if column=="Location" or column=="Industry" or column=="Gender" or column=="Job title":
            es_type="keyword"            
         elif column=="Salary" or column=="Total Base Salary in 2018 (in USD)" or column=="Total Bonus in 2018 (cumulative annual value in USD)" or column=="Total Stock Options/Equity in 2018 (cumulative annual value in USD)":
            es_type="float"
         else:
            es_type="text"
       
           
      except Exception as e:
         es_type = "text"

      mapping["mappings"]["properties"][column] = {"type": es_type}

   return mapping

class UploadCompensationDataViewS1(APIView):
    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')

        if not file_obj:
            return Response({"status":"error","error": "No file provided for uploading"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            file_path = default_storage.save('temp/' + file_obj.name, ContentFile(file_obj.read()))
            es_username = os.environ.get('ELASTICSEARCH_USERNAME', 'elastic')
            es_password = os.environ.get('ELASTICSEARCH_PASSWORD', 'Anurag')

            es = Elasticsearch([{'host': 'localhost', 'port': 9200}], 
                            http_auth=(es_username, es_password),timeout=40)

            mapping = get_mapping_from_csv(file_path)

            index_name = 'compensation_data_' + os.path.splitext(file_obj.name)[0]
            

            if es.indices.exists(index=index_name):
                es.indices.delete(index=index_name)
            
            es.indices.create(index=index_name, body=mapping)
            counter=0

            with open(default_storage.path(file_path), encoding='utf-8') as f:
                reader = csv.DictReader(f)
                bulk_data = []
                
                for row in reader:
                    counter += 1
                    row['document_id'] = counter
                    row = preprocess_salary(row)
                    bulk_data.append({
                        "_op_type": "index",
                        "_index": index_name,
                        "_id": counter,
                        "_source": row
                    })

                    if len(bulk_data) % 500 == 0:
                        helpers.bulk(es, bulk_data)
                        bulk_data = []

                if bulk_data:
                    helpers.bulk(es, bulk_data)

            return Response({"status":"success","data": "Data uploaded successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
           
            return Response({"status":"error","error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         


class UploadCompensationDataViewS2(APIView):

    def post(self, request, *args, **kwargs):
        file_obj = request.data.get('file')
        print(file_obj)


        try:
            file_path = default_storage.save('temp/' + file_obj.name, ContentFile(file_obj.read()))
            es_username = os.environ.get('ELASTICSEARCH_USERNAME', 'elastic')
            es_password = os.environ.get('ELASTICSEARCH_PASSWORD', 'Anurag')

            es = Elasticsearch([{'host': 'localhost', 'port': 9200}], 
                            http_auth=(es_username, es_password),timeout=40)

            mapping = get_mapping_from_csv(file_path)


            index_name = 'compensation_data_' + os.path.splitext(file_obj.name)[0]
            

            if es.indices.exists(index=index_name):
                es.indices.delete(index=index_name)
            
            es.indices.create(index=index_name, body=mapping)
            counter=0
            
            with open(default_storage.path(file_path), encoding='utf-8') as f:
                reader = csv.DictReader(f)
                bulk_data = []
                
                for row in reader:
                    counter += 1
                    row['document_id'] = counter
                    bulk_data.append({
                        "_op_type": "index",
                        "_index": index_name,
                        "_id": counter,
                        "_source": row
                    })

                    if len(bulk_data) % 500 == 0:
                        helpers.bulk(es, bulk_data)
                        bulk_data = []

                if bulk_data:
                    helpers.bulk(es, bulk_data)

            return Response({"status":"success","data": "Data uploaded successfully"}, status=status.HTTP_200_OK)

        except Exception as e:
           
            return Response({"status":"error","error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
      

            
