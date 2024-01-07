from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from elasticsearch_dsl import Search
import os

from compensation_logs.documents import CompensationDataDocument


    
class CompensationDataViewSetByFields(APIView):
    def get_authenticated_elasticsearch_client(self,username, password):
        return Elasticsearch(
            ['localhost:9200'],
            http_auth=(username, password),
            scheme="http", 
        )
    def get(self, request, *args, **kwargs):
       
        fields = request.GET.get('fields')

        if not fields:
            return Response({"status":"error","error": "fields parameter is not present"}, status=status.HTTP_400_BAD_REQUEST)

        es_username = os.environ.get('ELASTICSEARCH_USERNAME', 'elastic')
        es_password = os.environ.get('ELASTICSEARCH_PASSWORD', 'Anurag')

        es_client = self.get_authenticated_elasticsearch_client(es_username,es_password)
        
        fields_to_include = fields.split(',')

        search = Search(using=es_client, index=CompensationDataDocument.Index.name).extra(size=10000)

        response = search.execute()

        if response.hits.total.value == 0:
            return Response({"status":"error","error": "No records found containing these fields"}, status=status.HTTP_400_BAD_REQUEST)

        serialized_data = []
        for hit in response.hits:
            record = {}
            for field in fields_to_include:
                if field in hit:
                    record[field] = hit[field]
            serialized_data.append(record)

        return Response({"status":"success","data":serialized_data},status=status.HTTP_200_OK)
        

        