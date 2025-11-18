import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Sistema de Mensagens com Cassandra",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para deixar GOSTOSO
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1F4788;
        text-align: center;
        padding: 2rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2E5C8A;
        font-weight: bold;
        margin-top: 2rem;
    }
    .highlight-box {
        background-color: #E8F5E9;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E7D32;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #FFF3E0;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #F57C00;
        margin: 1rem 0;
    }
    .danger-box {
        background-color: #FFEBEE;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #C62828;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cassandra.apache.org/_/img/logos/cassandra_logo.svg", width=200)
    st.markdown("---")
    
    menu = st.radio(
        "📋 Navegação",
        ["🏠 Início", 
         "📊 Arquitetura", 
         "⚡ Cassandra vs SQL", 
         "💾 Modelagem",
         "🔥 Demo ao Vivo",
         "📚 Casos Reais",
         "🎯 Conclusão"]
    )
    
    st.markdown("---")
    st.markdown("### 👥 Equipe")
    st.markdown("""
    - Lucas Cosendey
    - [Seus colegas aqui]
    """)
    st.markdown("---")
    st.markdown("*UEPB - 2025*")

# PÁGINA PRINCIPAL
if menu == "🏠 Início":
    st.markdown('<div class="main-header">💬 Sistema de Mensagens com Apache Cassandra</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h2>100B+</h2>
            <p>Mensagens/dia no WhatsApp</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h2>99.999%</h2>
            <p>Disponibilidade</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h2>&lt;10ms</h2>
            <p>Latência de escrita</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 🎯 Objetivo do Projeto")
    st.markdown("""
    Demonstrar a aplicação prática de *bancos de dados NoSQL colunares* (Apache Cassandra) 
    em um sistema de mensagens em tempo real, destacando as vantagens sobre bancos SQL tradicionais.
    """)
    
    st.markdown("## 🚀 Por que Cassandra?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
            <h3>✅ Vantagens</h3>
            <ul>
                <li><b>Escritas massivas</b>: Milhões de msgs/segundo</li>
                <li><b>Escalabilidade linear</b>: Adiciona nós = mais capacidade</li>
                <li><b>Sem ponto único de falha</b>: Arquitetura peer-to-peer</li>
                <li><b>Ordenação temporal nativa</b>: Clustering keys</li>
                <li><b>Multi-datacenter</b>: Distribuição geográfica</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="danger-box">
            <h3>❌ SQL Tradicional Falha Em:</h3>
            <ul>
                <li><b>Locks</b>: Contenção em escritas simultâneas</li>
                <li><b>Sharding</b>: Escalabilidade complexa e manual</li>
                <li><b>Master-Slave</b>: Single point of failure</li>
                <li><b>Índices custosos</b>: Para ordenação temporal</li>
                <li><b>Downtime</b>: Para manutenção e upgrades</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# PÁGINA ARQUITETURA
elif menu == "📊 Arquitetura":
    st.markdown('<div class="main-header">📊 Arquitetura do Sistema</div>', unsafe_allow_html=True)
    
    st.markdown("## 🏗 Stack Tecnológica")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("*Banco de Dados*\n\nApache Cassandra (DataStax Astra)")
    with col2:
        st.info("*Backend*\n\nPython 3.x + astrapy")
    with col3:
        st.info("*Ambiente*\n\nCloud (DataStax Astra)")
    
    st.markdown("---")
    
    st.markdown("## 🔄 Arquitetura Cassandra")
    
    st.markdown("""
    ### Wide-Column Store
    
    O Cassandra *NÃO é um banco colunar puro, mas sim um **wide-column store*:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        *🗄 Bancos Colunares Puros*
        - BigQuery, Redshift
        - Otimizados para OLAP
        - Agregações rápidas
        """)
    
    with col2:
        st.markdown("""
        *📦 Cassandra (Wide-Column)*
        - Híbrido colunar + chave-valor
        - Otimizado para OLTP distribuído
        - Famílias de colunas dinâmicas
        """)
    
    st.markdown("---")
    
    st.markdown("## 🧬 Origem")
    
    st.markdown("""
    <div class="highlight-box">
    <b>Desenvolvido no Facebook (2007)</b><br>
    Por Avinash Lakshman (Amazon Dynamo) e Prashant Malik<br><br>
    
    <b>Síntese de dois papers seminais:</b><br>
    • <b>Google Bigtable</b>: Modelo de dados (wide-column, SSTables)<br>
    • <b>Amazon Dynamo</b>: Distribuição (peer-to-peer, hash ring, consistência eventual)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Características Principais")
    
    features = {
        "Descentralizado": "Todos os nós são iguais (sem master)",
        "Tolerante a Falhas": "Replicação automática de dados",
        "Alta Disponibilidade": "Sistema continua operando durante falhas",
        "Protocolo Gossip": "Comunicação P2P entre nós",
        "Consistência Tunável": "Escolha entre consistência forte ou eventual"
    }
    
    for feature, desc in features.items():
        st.success(f"{feature}: {desc}")

# PÁGINA COMPARAÇÃO
elif menu == "⚡ Cassandra vs SQL":
    st.markdown('<div class="main-header">⚡ Cassandra vs SQL Tradicional</div>', unsafe_allow_html=True)
    
    # Tabela comparativa
    st.markdown("## 📊 Comparação Técnica")
    
    comparison_data = {
        "Cenário": [
            "Inserir 1M msgs/seg",
            "Escalar 1TB → 10TB",
            "Últimas 50 msgs",
            "Falha de servidor",
            "Multi-datacenter",
            "Ordenação temporal"
        ],
        "SQL Tradicional ❌": [
            "Locks, lentidão, travamento",
            "Sharding manual, downtime",
            "Index scan custoso",
            "Sistema para",
            "Replicação manual complexa",
            "Índices custosos"
        ],
        "Apache Cassandra ✅": [
            "Linear, sem degradação",
            "Adiciona nós, zero downtime",
            "Leitura de partição O(1)",
            "Sistema continua operando",
            "Nativo, automático",
            "Clustering key nativa"
        ]
    }
    
    df = pd.DataFrame(comparison_data)
    
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    
    st.markdown("## 🔥 Problemas Específicos do SQL")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🔒 Locks", "📈 Escalabilidade", "⏱ Ordenação", "💥 SPOF"])
    
    with tab1:
        st.markdown("### 🔒 Performance em Escritas")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            *Problema SQL:*
            - Locks em operações INSERT
            - Contenção com milhões de escritas
            - Degradação exponencial
            """)
        with col2:
            st.markdown("""
            *Solução Cassandra:*
            - LSM-tree (Log-Structured Merge-Tree)
            - Append-only writes
            - Sem locks, sem contenção
            """)
    
    with tab2:
        st.markdown("### 📈 Escalabilidade Horizontal")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            *Problema SQL:*
            - Sharding manual
            - Complexidade alta
            - Downtime para rebalancear
            """)
        with col2:
            st.markdown("""
            *Solução Cassandra:*
            - Hash ring automático
            - Rebalanceamento dinâmico
            - Zero downtime
            """)
    
    with tab3:
        st.markdown("### ⏱ Ordenação Temporal")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            *Problema SQL:*
            - Índices B-tree custosos
            - Performance degrada com volume
            - Overhead de manutenção
            """)
        with col2:
            st.markdown("""
            *Solução Cassandra:*
            - Clustering Key ordena fisicamente
            - Ordenação no disco (nativa)
            - Performance constante O(1)
            """)
    
    with tab4:
        st.markdown("### 💥 Single Point of Failure")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            *Problema SQL:*
            - Arquitetura Master-Slave
            - Master = ponto único de falha
            - Sistema para se master cai
            """)
        with col2:
            st.markdown("""
            *Solução Cassandra:*
            - Arquitetura peer-to-peer
            - Todos os nós são iguais
            - Falha de nó não para sistema
            """)

# PÁGINA MODELAGEM
elif menu == "💾 Modelagem":
    st.markdown('<div class="main-header">💾 Modelagem de Dados</div>', unsafe_allow_html=True)
    
    st.markdown("## 🎯 Princípio: Query-Driven Design")
    
    st.warning("""
    *Cassandra pensa diferente do SQL!*
    
    - ❌ NÃO modelamos por entidades (normalização)
    - ✅ Modelamos pelas *queries* que a aplicação fará
    - ✅ Desnormalização é *incentivada*
    """)
    
    st.markdown("---")
    
    st.markdown("## 📋 Tabelas do Sistema")
    
    tab1, tab2 = st.tabs(["👤 Usuários", "💬 Mensagens"])
    
    with tab1:
        st.markdown("### Tabela: usuarios")
        st.code("""
CREATE TABLE usuarios (
    usuario_id UUID PRIMARY KEY,
    nome TEXT,
    email TEXT,
    criado_em TIMESTAMP
);
        """, language="sql")
        
        st.markdown("""
        *Decisões de Design:*
        - usuario_id como PRIMARY KEY
        - Simples e direta
        - Busca rápida por ID
        """)
    
    with tab2:
        st.markdown("### Tabela: mensagens")
        st.code("""
CREATE TABLE mensagens (
    conversa_id UUID,
    mensagem_id TIMEUUID,
    remetente_id UUID,
    destinatario_id UUID,
    conteudo TEXT,
    enviada_em TIMESTAMP,
    PRIMARY KEY (conversa_id, mensagem_id)
) WITH CLUSTERING ORDER BY (mensagem_id DESC);
        """, language="sql")
        
        st.markdown("""
        *Decisões de Design:*
        
        1. **conversa_id como Partition Key**
           - Agrupa todas as mensagens da mesma conversa FISICAMENTE juntas
           - Query "buscar mensagens da conversa X" = 1 única leitura de partição
           - Conversas diferentes distribuídas em nós diferentes
        
        2. **mensagem_id (TIMEUUID) como Clustering Key**
           - Ordenação cronológica AUTOMÁTICA
           - IDs únicos globalmente distribuídos
           - Inserções sempre no "final" da partição
        
        3. *ORDER BY DESC*
           - Mensagens mais recentes primeiro
           - Otimizado para "buscar últimas N mensagens"
        """)
    
    st.markdown("---")
    
    st.markdown("## 🔍 Queries Principais")
    
    query1, query2 = st.columns(2)
    
    with query1:
        st.markdown("*1. Buscar mensagens de uma conversa*")
        st.code("""
SELECT * FROM mensagens 
WHERE conversa_id = ?
LIMIT 50;
        """, language="sql")
        st.success("Performance: *O(1)* - Leitura de partição única")
    
    with query2:
        st.markdown("*2. Listar usuários*")
        st.code("""
SELECT * FROM usuarios;
        """, language="sql")
        st.info("Operação simples e direta")

# PÁGINA DEMO AO VIVO
elif menu == "🔥 Demo ao Vivo":
    st.markdown('<div class="main-header">🔥 Demonstração ao Vivo</div>', unsafe_allow_html=True)
    
    st.markdown("## 🎮 Interaja com o Sistema")
    
    st.info("💡 Esta é uma simulação da interface. O código real conecta no Astra DB!")
    
    # Simulação de inserção
    st.markdown("### 📝 Enviar Nova Mensagem")
    
    col1, col2 = st.columns(2)
    
    with col1:
        remetente = st.text_input("Remetente", "João Silva")
        destinatario = st.text_input("Destinatário", "Maria Santos")
    
    with col2:
        mensagem = st.text_area("Mensagem", "Oi, tudo bem? Vamos revisar o projeto hoje?")
    
    if st.button("📤 Enviar Mensagem", type="primary"):
        with st.spinner("Inserindo no Cassandra..."):
            import time
            time.sleep(0.5)
        st.success("✅ Mensagem enviada com sucesso! Latência: *8ms*")
    
    st.markdown("---")
    
    st.markdown("### 💬 Histórico de Conversa")
    
    # Dados simulados
    mensagens_demo = [
        {"Hora": "14:23", "Remetente": "João", "Mensagem": "E aí, vamos revisar?"},
        {"Hora": "14:25", "Remetente": "Maria", "Mensagem": "Bora! Já terminei minha parte."},
        {"Hora": "14:27", "Remetente": "João", "Mensagem": "Show! Te espero às 15h."},
        {"Hora": "14:28", "Remetente": "Maria", "Mensagem": "Fechado! 👍"},
    ]
    
    df_msgs = pd.DataFrame(mensagens_demo)
    st.dataframe(df_msgs, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    st.markdown("### 📊 Métricas de Performance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Latência Escrita", "8ms", "-2ms")
    col2.metric("Latência Leitura", "12ms", "+1ms")
    col3.metric("Msgs/segundo", "1.2M", "+5%")
    col4.metric("Disponibilidade", "99.998%", "0%")

# PÁGINA CASOS REAIS
elif menu == "📚 Casos Reais":
    st.markdown('<div class="main-header">📚 Casos de Uso Reais</div>', unsafe_allow_html=True)
    
    st.markdown("## 🌍 Empresas que usam Cassandra")
    
    # WhatsApp
    with st.expander("📱 WhatsApp", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            ### 📊 Números
            - *~100 bilhões* msgs/dia
            - *2+ bilhões* de usuários
            - *99.99%* uptime
            """)
        with col2:
            st.markdown("""
            ### 🎯 Por que Cassandra?
            - Única solução com escala horizontal mantendo latência baixa
            - Escritas massivas distribuídas
            - Multi-datacenter para usuários globais
            """)
    
    # Instagram
    with st.expander("📸 Instagram"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            ### 📊 Números
            - *Bilhões* de posts
            - *500M+* stories/dia
            - Feed personalizado
            """)
        with col2:
            st.markdown("""
            ### 🎯 Por que Cassandra?
            - Feed de atividades ordenado cronologicamente
            - Ordenação temporal nativa (clustering keys)
            - Alta disponibilidade global
            """)
    
    # Netflix
    with st.expander("🎬 Netflix"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            ### 📊 Números
            - *230M+* assinantes
            - *Petabytes* de dados
            - Recomendações personalizadas
            """)
        with col2:
            st.markdown("""
            ### 🎯 Por que Cassandra?
            - Histórico de visualizações
            - Leituras rápidas mesmo com petabytes
            - Sistema de recomendações em tempo real
            """)
    
    # Apple
    with st.expander("🍎 Apple"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            ### 📊 Números
            - *75M+* músicas
            - Apple Music global
            - iCloud services
            """)
        with col2:
            st.markdown("""
            ### 🎯 Por que Cassandra?
            - Metadados de músicas
            - Preferências de usuários
            - Disponibilidade global 24/7
            """)
    
    st.markdown("---")
    
    st.markdown("## 💡 Padrão Comum")
    
    st.markdown("""
    <div class="highlight-box">
    Todas essas empresas escolheram Cassandra pelos mesmos motivos:
    
    ✅ <b>Escalabilidade massiva</b> (bilhões de operações)<br>
    ✅ <b>Disponibilidade crítica</b> (99.99%+)<br>
    ✅ <b>Latência consistente</b> (mesmo com crescimento)<br>
    ✅ <b>Distribuição global</b> (multi-datacenter)<br>
    ✅ <b>Sem downtime</b> (manutenção zero-downtime)
    </div>
    """, unsafe_allow_html=True)

# PÁGINA CONCLUSÃO
elif menu == "🎯 Conclusão":
    st.markdown('<div class="main-header">🎯 Conclusão</div>', unsafe_allow_html=True)
    
    st.markdown("## 📝 Resumo do Projeto")
    
    st.markdown("""
    Demonstramos com sucesso a aplicação de *Apache Cassandra* em um sistema de mensagens,
    evidenciando suas vantagens sobre bancos de dados SQL tradicionais.
    """)
    
    st.markdown("---")
    
    st.markdown("## ✅ O que entregamos")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📦 Entregas Técnicas
        - ✅ Repositório GitHub completo
        - ✅ Modelagem de dados documentada
        - ✅ Scripts CQL funcionais
        - ✅ Código Python conectando ao Astra
        - ✅ Justificativa técnica robusta
        """)
    
    with col2:
        st.markdown("""
        ### 🎓 Conceitos Demonstrados
        - ✅ Query-driven design
        - ✅ Partition Keys & Clustering Keys
        - ✅ Ordenação por TIMEUUID
        - ✅ Distribuição de dados
        - ✅ Alta disponibilidade
        """)
    
    st.markdown("---")
    
    st.markdown("## 🏆 Conclusão Final")
    
    st.markdown("""
    <div class="highlight-box">
    <h3>Para sistemas de mensagens que exigem:</h3>
    
    • Alta volumetria de escritas (milhões/segundo)<br>
    • Crescimento imprevisível<br>
    • Disponibilidade crítica (99.999%)<br>
    • Latência consistente<br>
    • Distribuição geográfica<br><br>
    
    <h2 style="color: #2E7D32;">Apache Cassandra é a escolha técnica superior! ✅</h2>
    
    O modelo wide-column distribuído resolve problemas fundamentais que SQL não foi projetado para enfrentar.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("## 📚 Referências")
    
    st.markdown("""
    *FOWLER, Martin; SADALAGE, Pramod J.* NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence. 
    Upper Saddle River, NJ: Addison-Wesley, 2012.
    
    *HEWITT, Eben.* Cassandra: The Definitive Guide. Sebastopol, CA: O'Reilly Media, 2010.
    
    *LAKSHMAN, Avinash; MALIK, Prashant.* Cassandra: a decentralized structured storage system. 
    ACM SIGOPS Operating Systems Review, v. 44, n. 2, p. 35-40, 2010.
    
    *DATASTAX.* Apache Cassandra Documentation. Disponível em: https://cassandra.apache.org/doc/latest/
    """)
    
    st.markdown("---")
    
    st.balloons()
    
    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <h2>🎉 Obrigado pela atenção! 🎉</h2>
        <p>Dúvidas? Perguntas? Estamos aqui! 😊</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    Sistema de Mensagens com Apache Cassandra | UEPB 2025<br>
    Desenvolvido para a disciplina de Bancos de Dados NoSQL
</div>
""", unsafe_allow_html=True)