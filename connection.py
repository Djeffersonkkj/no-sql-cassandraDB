from astrapy import DataAPIClient
import os
from dotenv import load_dotenv

print("🔄 Carregando variáveis de ambiente...")
load_dotenv()

print("🔄 Pegando credenciais...")
token = os.getenv("ASTRA_TOKEN")
endpoint = os.getenv("ASTRA_DB_ENDPOINT")
keyspace = os.getenv("ASTRA_KEYSPACE")

print(f"Token: {token[:20]}...")  # mostra só o início
print(f"Endpoint: {endpoint}")
print(f"Keyspace: {keyspace}")

print("🔄 Conectando ao Astra DB...")
client = DataAPIClient(token)

print("🔄 Pegando database...")
db = client.get_database_by_api_endpoint(
    endpoint,
    keyspace=keyspace
)

print(f"✅ Conectado ao Astra DB!")
print(f"Collections disponíveis: {db.list_collection_names()}")