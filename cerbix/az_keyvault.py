from azure.identity import ClientSecretCredential
from dotenv import load_dotenv
import os

load_dotenv()

class KeyVault:
  def __init__(self, client_id, tenant_id, client_secret, account_url):
    self.client_id = client_id
    self.tenant_id = tenant_id
    self.client_secret = client_secret
    self.account_url = account_url

def config_vault():
  configuration = KeyVault(
    client_id=os.environ['AZURE_CLIENT_ID'],
    tenant_id=os.environ['AZURE_TENANT_ID'],
    client_secret=os.environ['AZURE_CLIENT_SECRET'],
    account_url=os.environ['AZURE_STORAGE_URL']
  )
  return configuration

def az_credentials():
    configuration_params = config_vault()
    credentials = ClientSecretCredential(
      client_id = configuration_params.client_id,
      client_secret = configuration_params.client_secret,
      tenant_id = configuration_params.tenant_id
    )
    return credentials



if __name__ =="__main__":
   config_vault()