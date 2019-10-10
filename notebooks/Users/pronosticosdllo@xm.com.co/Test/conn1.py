# Databricks notebook source
# MAGIC %sh
# MAGIC ping 172.16.1.4

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install git+https://github.com/osimloeff/PI-Web-API-Client-Python.git

# COMMAND ----------

# MAGIC %sh 
# MAGIC python setup.py install --user

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install --upgrade pip
# MAGIC sudo pip install osisoft.pidevclub.piwebapi

# COMMAND ----------

from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient

# COMMAND ----------

"""
Created on Thu Sep 26 22:39:04 2019

@author: John Jairo Orozco G - Intergrupo
"""
#from piwebapi import PIWebApiClient
from osisoft.pidevclub.piwebapi.pi_web_api_client import PIWebApiClient
client = PIWebApiClient ("https://172.16.1.4/piwebapi", username ="BG1222", password ="YlbrI7UchlsW", verifySsl = False)
client.data.point(webid="P0g8Zg6yQHRES3Jt6ZV1FTQQcKIAAAU1JWWE01OFwwMzBFOUJFNS00QzM5LTQxOTAtQTYyOC0yRkQxMzM5RkFEM0U", 'TYUMBO:34.5:Gen1:P:MvMoment')
client.assetServer.
#df1 = client.data.get_recorded_values("pi:\\\\SRVXM58\\sinusoid", start_time="*-1d", end_time="*")
df2 = client.data.get_interpolated_values("pi:\\\\SRVXM58\\sinusoid", start_time="*-1d", end_time="*", interval="1h")
#TYUMBO:34.5:Gen1:P:MvMoment