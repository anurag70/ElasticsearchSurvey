from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from elasticsearch_dsl import Search,Q
import ast, os

from compensation_logs.documents import CompensationDataDocument

class CompensationDataViewSet(APIView):
    def get_authenticated_elasticsearch_client(self,username, password):
        return Elasticsearch(
            ['localhost:9200'],
            http_auth=(username, password),
            scheme="http",
        )
    def get(self, request, *args, **kwargs):
        filters = {key: value for key, value in request.GET.items() }
        search_fields=['Salary','Timestamp','Age','Industry','Job title','Additional_information','Other','Experience','Location','Currency']
        
        es_username = os.environ.get('ELASTICSEARCH_USERNAME', 'elastic')
        es_password = os.environ.get('ELASTICSEARCH_PASSWORD', 'Anurag')

        es_client = self.get_authenticated_elasticsearch_client(es_username,es_password)
        q_objects = []

        for key, value in filters.items():  
            if key == "Salary":
                q_objects.append(Q("range", **{key: {"gte": value}}))
           
            else:
                q_objects.append(Q("match", **{key: {"query": value, "fuzziness": "auto"}}))
                
        search = Search(using=es_client, index=CompensationDataDocument.Index.name).query("bool", should=q_objects).extra(size=10000)

        sort_params = self.request.query_params.getlist("sort",[])
        sort_params=ast.literal_eval(sort_params[0]) if sort_params else []
        
        if sort_params:
            for sort_field in sort_params:
                
               field, order = sort_field.split(":")
               order = order.lower()  
               search = search.sort({field: {"order": order}})
                    
        response = search.execute()
        serialized_data = []
        
        for hit in response.hits:
            record = {}
            for field in search_fields:
                if field in hit:
                    record[field] = hit[field]
            serialized_data.append(record)

        return Response({"status":"success","data":serialized_data},status=status.HTTP_200_OK)
        
     