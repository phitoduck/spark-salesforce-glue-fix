from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from dataclasses import dataclass

from typing import List, Optional, OrderedDict, Type
import os


#####################
# --- Constants --- #
#####################

USERNAME = os.environ.get("SALESFORCE_USERNAME", "dummy-username")
PASSWORD = os.environ.get("SALESFORCE_PASSWORD", "dummy-password")
# get this here: https://docs.idalko.com/exalate/display/ED/Salesforce%3A+How+to+generate+a+security+token
SECURITY_TOKEN = os.environ.get("SALESFORCE_SECURITY_TOKEN", "dummy-token")

PASSWORD_WITH_TOKEN = PASSWORD + SECURITY_TOKEN

#####################
# --- Spark Job --- #
#####################

SOQL_STMT = """\
SELECT id,
       isdeleted,
       accountid,
       isprivate,
       NAME,
       description,
       stagename,
       amount,
       probability,
       expectedrevenue,
       totalopportunityquantity,
       closedate,
       type,
       nextstep,
       leadsource,
       isclosed,
       iswon,
       forecastcategory,
       forecastcategoryname,
       campaignid,
       hasopportunitylineitem,
       pricebook2id,
       ownerid,
       createddate,
       createdbyid,
       lastmodifieddate,
       lastmodifiedbyid,
       systemmodstamp,
       lastactivitydate,
       laststagechangedate,
       fiscal,
       contactid,
       lastvieweddate,
       lastreferenceddate,
       hasopenactivity,
       hasoverduetask,
       lastamountchangedhistoryid,
       lastclosedatechangedhistoryid,
       deliveryinstallationstatus__c,
       trackingnumber__c,
       ordernumber__c,
       currentgenerators__c,
       maincompetitors__c
FROM   opportunity 
LIMIT  10
"""

def run():
    sc = SparkContext.getOrCreate()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session
    job = Job(glueContext)

    df = (
        spark
            .read
            .format("com.springml.spark.salesforce")
            .option("username", USERNAME)
            .option("password", PASSWORD_WITH_TOKEN)
            .option("soql", SOQL_STMT)
            .option("bulk", True)
            # Opportunity.LastStageChangeDate is only availaable in API v52
            .option("version", 52)
            .option("sfObject", "opportunity")
            .load()
    )

    print(df.show())

run()
