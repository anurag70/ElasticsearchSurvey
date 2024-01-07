![Screenshot 2024-01-08 000350](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/3f571372-7397-4530-ba92-9071098efa32)
![Screenshot 2024-01-08 000339](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/e1b232ef-ec10-4608-a172-4dbded5f47b0)
## to run the project first have to install requirements.txt file(pip3 install -r requiresmennt.txt --legacy-resolver=deprecated)
## also have to install elasticsearch and kibana and have to setup locally 
   1) for elasticsearch  (http://localhost:9200/)
   2) for kibana  (http://localhost:5601/app/dev_tools#/console)


# for uploading the survey dataset 

## exposed endpoint  (/compensation/upload/)
     curl --location --request POST 'localhost:8000/compensation/upload/' \
        --form 'file=@"/C:/Users/anura/Downloads/salary_survey-1.csv"'


#  for querying the exposed endpoints are
   ## 1) fetch using filters ( along with sorting)
      curl --location -g --request GET 'localhost:8000/compensation/compensation_data/?Salary=75000&Industry=Government&Currency=USD&Age=35-44&Job%20title=Data%20Scientist&sort=[%22Timestamp:desc%22,%20%22Salary:asc%22]' \
            --header 'Content-Type: application/json' \
            --data-raw '{
              "level": "INFO",
              "message": "User login successful",
              "resourceId": "eeecf5f2-e05a-41ec-bcc8-6f51e8e11d13",
              "timestamp": "2023-07-15T14:20:10",
              "traceId": "0a35c195-4897-4e5b-8564-bdfb67d05f47",
              "spanId": "d0c0d98d-58a1-4b26-84b3-891b7b937f4f",
              "commit": "46d0b3189dbf534b55f70a654892af06c783b7a0fc422f071a397b0b2a05f17d",
              "metadata": {
                "field1": "value1",
                "field2": 456,
                "field3": false
              }
            }'
            
   ## 2) fetch using fields (also to fetch sparse record)
       curl --location --request GET 'localhost:8000/compensation/compensation_data/get_data_by_fields?fields=Timestamp,Salary,Job%20title,Industry'

   ## 3) fetch using key( single record)
       curl --location --request GET 'localhost:8000/compensation/compensation_data/get_data_by_id?id=11321'


# Screenshots for the query, mapping, exposed rest api endpoints for querying

![Screenshot 2024-01-07 202604](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/5fb59da0-af74-4562-a30d-2c70ae2b8e79)
![Screenshot 2024-01-07 202555](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/765b3953-aa6d-418d-9a2e-1f4ad47b2ca3)
![Screenshot 2024-01-07 202548](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/8d42c6d2-a8c4-4dc4-8b49-1ecb899da12a)
![Screenshot 2024-01-07 202535](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/93ece6f6-6db2-4599-a567-15d83f086b49)
![Screenshot 2024-01-07 202508](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/8cdbd839-3e97-4f7d-9cb5-821e7733a730)
![Screenshot 2024-01-07 202441](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/e76bfaea-f9f2-4fe2-aef3-23ea4ad5c2be)
![Screenshot 2024-01-07 202017](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/a002b383-9ef2-48bd-a637-3d8e0e3f654e)
![Screenshot 2024-01-07 201941](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/13df8c38-c68d-409d-88e2-5a82e83deb8c)
![Screenshot 2024-01-07 201915](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/6be415d0-cbb2-422f-9d90-04bdde550078)
![Screenshot 2024-01-07 201904](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/1cd4b4fe-4fc0-4b48-8c86-aaca6e19e9ff)
![Screenshot 2024-01-07 201852](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/e82a7deb-2131-47b0-8945-14115304a6e5)
![Screenshot 2024-01-07 201839](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/118b5db4-b108-4c6d-9bb2-74acdd2a6ab6)
![Screenshot 2024-01-07 201802](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/10b37cc2-a84b-4288-9e0c-bd1d80946fcf)
![Screenshot 2024-01-07 201746](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/0ea8f425-362d-4c52-8fb6-6e2a75a4c781)
![Screenshot 2024-01-07 201728](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/734f04c9-846b-41e4-aca0-76865e08566b)
![Screenshot 2024-01-07 201713](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/f841bac1-ac02-44ff-87f8-dc7e84a9d814)
![Screenshot 2024-01-07 195522](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/22171c0f-e2fb-4c93-b8d1-7befafe99357)
![Screenshot 2024-01-07 195501](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/d1968a95-0970-4421-b771-9e8498bcbd23)
![Screenshot 2024-01-07 195433](https://github.com/anurag70/ElasticsearchSurvey/assets/72279629/96fa30cd-d175-44cd-a765-896053889205)
