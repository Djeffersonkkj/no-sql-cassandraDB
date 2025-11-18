# no-sql-cassandraDB
SEMINÁRIO 2 | Para conclusão da matéria banco de dados não relacionais.

# Sistema de Mensagens com Apache Cassandra

Projeto acadêmico demonstrando a aplicação de bancos de dados NoSQL colunares (Apache Cassandra) em um sistema de mensagens em tempo real.

## 🎯 Objetivo

Implementar um sistema simplificado de mensagens (similar a WhatsApp/Telegram) utilizando Apache Cassandra para demonstrar as vantagens de bancos colunares em cenários de alta escalabilidade e disponibilidade.

## 🏗️ Arquitetura

### Tecnologias Utilizadas
- **Banco de Dados:** Apache Cassandra (via DataStax Astra DB)
- **Linguagem:** Python 3.x
- **Bibliotecas:** astrapy, python-dotenv
- **Ambiente:** Cloud (DataStax Astra)

### Modelagem de Dados

#### Tabela: `usuarios`
```sql
CREATE TABLE usuarios (
    usuario_id UUID PRIMARY KEY,
    nome TEXT,
    email TEXT,
    criado_em TIMESTAMP
);
```
- **Partition Key:** `usuario_id` - Distribui usuários uniformemente pelos nós
- **Propósito:** Armazenar informações básicas dos usuários

#### Tabela: `mensagens`
```sql
CREATE TABLE mensagens (
    conversa_id UUID,
    mensagem_id TIMEUUID,
    remetente_id UUID,
    destinatario_id UUID,
    conteudo TEXT,
    enviada_em TIMESTAMP,
    PRIMARY KEY (conversa_id, mensagem_id)
) WITH CLUSTERING ORDER BY (mensagem_id DESC);
```
- **Partition Key:** `conversa_id` - Agrupa mensagens da mesma conversa no mesmo nó
- **Clustering Key:** `mensagem_id` (TIMEUUID) - Ordena mensagens cronologicamente
- **Propósito:** Armazenar mensagens otimizadas para leitura por conversa

### Decisões de Modelagem

**Por que usar TIMEUUID para mensagem_id?**
- Garante ordenação temporal automática
- IDs únicos globalmente distribuídos
- Evita conflitos em inserções concorrentes

**Por que conversa_id como Partition Key?**
- Coloca todas as mensagens de uma conversa no mesmo nó (locality)
- Queries extremamente rápidas: buscar histórico de conversa = 1 leitura de partição
- Escalabilidade: conversas diferentes distribuídas em nós diferentes

## 🔍 Por que Cassandra ao invés de SQL?

### Limitações de Bancos Relacionais para Mensagens

| Problema | Impacto em SQL | Solução Cassandra |
|----------|----------------|-------------------|
| **Escritas massivas** | Locks, contenção, lentidão | Escritas distribuídas sem locks |
| **Escalabilidade horizontal** | Complexo (sharding manual) | Linear e automático |
| **Ordenação temporal** | Índices custosos | Clustering key nativo |
| **Alta disponibilidade** | Master-slave (single point of failure) | Sem ponto único de falha |
| **Latência** | Aumenta com volume | Consistente mesmo com bilhões de registros |

### Vantagens do Cassandra

1. **Performance em Escrita:** Otimizado para inserções massivas (milhões/segundo)
2. **Particionamento Inteligente:** Cada conversa isolada em uma partição
3. **Ordenação Nativa:** TIMEUUID garante ordem cronológica sem índices
4. **Escalabilidade Linear:** Adicionar nós = aumentar capacidade proporcionalmente
5. **Disponibilidade:** Replicação multi-datacenter sem downtime

### Caso de Uso Real

WhatsApp processa **~100 bilhões de mensagens/dia**. Com SQL tradicional:
- Locks constantes em tabelas de mensagens
- Índices gigantescos para ordenação
- Sharding complexo e custoso
- Downtime para manutenção

Com Cassandra:
- ✅ Escritas distribuídas sem contenção
- ✅ Particionamento automático por conversa
- ✅ Adição de nós sem parar o sistema
- ✅ Replicação transparente

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Conta no DataStax Astra (gratuita)

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/projeto-cassandra.git
cd projeto-cassandra
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as credenciais
Crie um arquivo `.env` com suas credenciais do Astra:
```
ASTRA_TOKEN=seu_token_aqui
ASTRA_DB_ENDPOINT=seu_endpoint_aqui
ASTRA_KEYSPACE=default_keyspace
```

### 4. Teste a conexão
```bash
python connection.py
```

### 5. Execute queries CQL
Copie o conteúdo de `queries.cql` e execute no CQL Console do Astra DB.

## 📊 Exemplos de Queries

### Buscar histórico de uma conversa
```sql
SELECT * FROM mensagens 
WHERE conversa_id = 1d89c60a-cfb8-40b5-90d5-8cf1796ab60b
ORDER BY mensagem_id DESC
LIMIT 50;
```
**Performance:** O(1) - Uma única leitura de partição

### Listar usuários
```sql
SELECT * FROM usuarios;
```

## 📁 Estrutura do Projeto
```
projeto-cassandra/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
├── .env                      # Credenciais (não commitado)
├── .gitignore               # Arquivos ignorados
├── connection.py            # Script de conexão
├── queries.cql              # Queries de exemplo
└── docs/
    └── justificativa.md     # Justificativa técnica detalhada
```

## 🎓 Conceitos Demonstrados

- ✅ Modelagem orientada a queries (Query-driven design)
- ✅ Partition Keys e Clustering Keys
- ✅ Ordenação por timestamp (TIMEUUID)
- ✅ Distribuição de dados (Partitioning)
- ✅ Alta disponibilidade e escalabilidade

## 📚 Referências

- [DataStax Astra Documentation](https://docs.datastax.com/en/astra/docs/)
- [Apache Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
- [Cassandra Data Modeling Best Practices](https://cassandra.apache.org/doc/latest/data_modeling/)

## 👥 Autores

- Seu Nome
- Nome do Colega

## 📄 Licença

Este projeto é acadêmico e foi desenvolvido para fins educacionais.
```

---

### 3️⃣ **Criar o arquivo de justificativa técnica**

**Arquivo: `docs/justificativa.md`** (já fizemos antes, mas vou repassar)

---

### 4️⃣ **Criar `.gitignore`**

**Arquivo: `.gitignore`**
```
# Credenciais
.env
*.zip

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
