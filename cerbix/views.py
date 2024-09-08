from django.shortcuts import render
from django.http import HttpResponse
from azure.storage.blob import BlobServiceClient

from dotenv import load_dotenv

from .az_keyvault import config_vault, az_credentials

load_dotenv()

# Name of the container in Azure Data Storage
container_name = 'testdata'
# Name of the file from $container_name
blob_name = 'testload.txt'


def get_blob_data(request):
  
  # Set client to access azure storage container
  blob_service_client = BlobServiceClient(account_url = config_vault().account_url, credential = az_credentials())
  
  # Get the container client
  container_client = blob_service_client.get_container_client(container=container_name)

  # Download blob data
  blob_client = container_client.get_blob_client(blob = blob_name)
  data = blob_client.download_blob().readall().decode("utf-8")
  
  return HttpResponse(data)
