from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from dotenv import load_dotenv
import uuid
from datetime import datetime

load_dotenv()

# Configurar autenticação
cloud_config = {
    'secure_connect_bundle': 'secure-connect-bundle.zip'  # Vamos precisar baixar isso
}

auth_provider = PlainTextAuthProvider(
    os.getenv("ASTRA_CLIENT_ID"),
    os.getenv("ASTRA_CLIENT_SECRET")
)

cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

# Usar o keyspace
session.set_keyspace('default_keyspace')

print("✅ Conectado ao Cassandra!")

# Inserir usuário
def inserir_usuario(nome, email):
    query = """
    INSERT INTO usuarios (usuario_id, nome, email, criado_em)
    VALUES (%s, %s, %s, %s)
    """
    session.execute(query, (uuid.uuid4(), nome, email, datetime.now()))
    print(f"✅ Usuário '{nome}' inserido!")

# Inserir mensagem
def inserir_mensagem(conversa_id, remetente_id, destinatario_id, conteudo):
    query = """
    INSERT INTO mensagens (conversa_id, mensagem_id, remetente_id, destinatario_id, conteudo, enviada_em)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    from cassandra.util import uuid_from_time
    session.execute(query, (
        conversa_id,
        uuid_from_time(datetime.now()),
        remetente_id,
        destinatario_id,
        conteudo,
        datetime.now()
    ))
    print(f"✅ Mensagem inserida!")

# Teste
inserir_usuario("Pedro Oliveira", "pedro@email.com")