from django_elasticsearch_dsl import Document, fields,Index
from django_elasticsearch_dsl.registries import registry
from .models import CompensationData

PUBLISHER_INDEX=Index('compensation_data_salary_survey-1')

PUBLISHER_INDEX.settings(
   number_of_shards=1,
   number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class CompensationDataDocument(Document):
    class Index:
        name = 'compensation_data_salary_survey-1'

    Timestamp = fields.DateField()
    Age = fields.KeywordField()
    Industry = fields.Text()  
    JobTitle = fields.Text() 
    Salary = fields.FloatField()
    Currency = fields.KeywordField()
    Location = fields.KeywordField()
    Experience = fields.KeywordField()
    AdditionalInformation = fields.Text()  
    Other = fields.Text() 

    class Django:
        model = CompensationData
