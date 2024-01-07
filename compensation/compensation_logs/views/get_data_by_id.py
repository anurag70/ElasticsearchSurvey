from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from elasticsearch_dsl import Search,Q
import os

from compensation_logs.documents import CompensationDataDocument


class CompensationDataViewSetById(APIView):
    def get_authenticated_elasticsearch_client(self, username, password):
        return Elasticsearch(
            ['localhost:9200'],
            http_auth=(username, password),
            scheme="http"
        )
    def get(self, request, *args, **kwargs):
       
      record_id = request.GET.get('id')
      if not record_id:
         return Response({"status":"error","error":"Please provide a valid record Id"}, status=status.HTTP_400_BAD_REQUEST)
      
      es_username = os.environ.get('ELASTICSEARCH_USERNAME', 'elastic')
      es_password = os.environ.get('ELASTICSEARCH_PASSWORD', 'Anurag')

      es_client = self.get_authenticated_elasticsearch_client(es_username,es_password)
      search = Search(using=es_client, index=CompensationDataDocument.Index.name).query(Q('term', document_id=record_id)).extra(size=10000)

      response = search.execute()
      if response.hits.total.value == 0:
         return Response({"status":"error","error": "Record not found related to this id"}, status=status.HTTP_400_BAD_REQUEST)

      serialized_data = response.hits[0].to_dict()

      return Response({"sattus":"success","data":serialized_data},status=status.HTTP_200_OK)
      