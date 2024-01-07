
from rest_framework import serializers

class CompensationDataSerializer(serializers.Serializer):
      Timestamp = serializers.SerializerMethodField()
      salary = serializers.SerializerMethodField()
      age = serializers.SerializerMethodField()
      industry = serializers.SerializerMethodField()
      job_title = serializers.SerializerMethodField()
      currency = serializers.SerializerMethodField()
      location = serializers.SerializerMethodField()
      experience = serializers.SerializerMethodField()
      additional_information = serializers.SerializerMethodField()
      other = serializers.SerializerMethodField()
      
      
      def get_Timestamp(self,obj):
         return obj.get("Timestamp")
      
      def get_salary(self,obj):
         return obj.get("Salary")
      
      def get_age(self,obj):
         return obj.get("Age")
      
      def get_currency(self,obj):
         return obj.get("Currency")
      
      def get_location(self,obj):
         print(obj)
         return obj.get("Location")
      
      def get_other(self,obj):
         return obj.get("Other")
      
      def get_experience(self,obj):
         return obj.get("Experience")
      
      def get_job_title(self,obj):
         return obj.get("Job title")
      
      def get_additional_information(self,obj):
         return obj.get("Additional_information")
      
      def get_industry(self,obj):
         return obj.get("Industry")
      
      




