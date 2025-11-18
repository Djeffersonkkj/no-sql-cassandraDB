import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="NoSQL com Cassandra: Sistema de Mensagens Escalável",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS ENXUTO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    .main { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
    .block-container { background: white; border-radius: 15px; padding: 1.5rem; margin-top: 1rem; }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.8rem;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-size: 0.95rem;
        color: #666;
        text-align: center;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    
    .section-header {
        font-size: 1.6rem;
        font-weight: 700;
        color: #2D3748;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    
    .card {
        background: linear-gradient(135deg, #f6f8fb 0%, #ffffff 100%);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.07);
        margin: 0.6rem 0;
        border-left: 3px solid #667eea;
        font-size: 0.9rem;
    }
    
    .card-purple {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 6px 15px rgba(102,126,234,0.3);
        margin: 0.6rem 0;
    }
    
    .card-title {
        font-size: 1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .team-card {
        background: linear-gradient(135deg, #E9D5FF 0%, #DDD6FE 100%);
        padding: 0.8rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.4rem;
        font-size: 0.85rem;
    }
    
    .team-name {
        font-size: 0.95rem;
        font-weight: 600;
        color: #5B21B6;
        margin-bottom: 0.2rem;
    }
    
    .team-role {
        font-size: 0.8rem;
        color: #7C3AED;
    }
    
    .metric-big {
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        text-align: center;
    }
    
    .metric-label {
        font-size: 0.8rem;
        color: rgba(255,255,255,0.9);
        text-align: center;
    }
    
    .comparison-bad {
        background: linear-gradient(135deg, #FEE2E2 0%, #FECACA 100%);
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #EF4444;
        font-size: 0.85rem;
    }
    
    .comparison-good {
        background: linear-gradient(135deg, #D1FAE5 0%, #A7F3D0 100%);
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid #10B981;
        font-size: 0.85rem;
    }
    
    .numbered-step {
        display: flex;
        align-items: flex-start;
        margin: 0.8rem 0;
    }
    
    .step-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-center;
        font-size: 1rem;
        font-weight: 700;
        margin-right: 0.8rem;
        flex-shrink: 0;
    }
    
    .footer {
        text-align: center;
        color: #666;
        padding: 1.5rem;
        margin-top: 2rem;
        border-top: 1px solid #E5E7EB;
        font-size: 0.85rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🎯 Navegação")
    menu = st.radio(
        "",
        ["🏠 Início", 
         "🏗️ Arquitetura & Stack",
         "⚡ Por que Cassandra?",
         "🌍 Casos Reais",
         "💡 Implementação",
         "📚 Referências"]
    )
    
    st.markdown("---")
    st.markdown("### 🏫 Instituição")
    st.markdown("**UEPB - Campus V**  \nCiência de Dados  \n2025")

# PÁGINA INÍCIO
if menu == "🏠 Início":
    st.markdown('<div class="hero-title">NoSQL com Cassandra: Sistema de Mensagens Escalável</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="hero-subtitle">
    Projeto acadêmico demonstrando a aplicação de Apache Cassandra na construção de um sistema de mensagens em tempo real, 
    explorando suas vantagens sobre bancos SQL tradicionais.
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card-purple"><div class="metric-big">100B+</div><div class="metric-label">Mensagens/dia (WhatsApp)</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card-purple"><div class="metric-big">99.999%</div><div class="metric-label">Disponibilidade</div></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="card-purple"><div class="metric-big">&lt;10ms</div><div class="metric-label">Latência de Escrita</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Equipe
    st.markdown('<div class="section-header">👥 A Equipe</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="team-card"><div style="font-size: 1.8rem;">👤</div><div class="team-name">Luan Torres</div><div class="team-role">Desenvolvedor e Analista</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="team-card"><div style="font-size: 1.8rem;">💼</div><div class="team-name">Lucas Edson</div><div class="team-role">Arquiteto de Soluções</div></div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="team-card"><div style="font-size: 1.8rem;">👥</div><div class="team-name">Nathalia Rayssa</div><div class="team-role">Designer e Documentadora</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="team-card"><div style="font-size: 1.8rem;">🎓</div><div class="team-name">Djefersson</div><div class="team-role">Especialista em BD</div></div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="team-card"><div style="font-size: 1.8rem;">🔐</div><div class="team-name">Rianderson</div><div class="team-role">Arquiteto de Segurança</div></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Objetivo
    st.markdown('<div class="section-header">🎯 Objetivo</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="card">
        Desenvolver um sistema de mensagens simplificado (similar ao WhatsApp/Telegram) 
        utilizando <strong>Apache Cassandra</strong> para demonstrar suas capacidades em cenários de alta escalabilidade.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-good">
        <strong>✅ Entregas:</strong><br>
        • Troca de mensagens em tempo real<br>
        • Alta disponibilidade e escalabilidade<br>
        • Análise de performance<br>
        • Documentação completa
        </div>
        """, unsafe_allow_html=True)

# PÁGINA ARQUITETURA
elif menu == "🏗️ Arquitetura & Stack":
    st.markdown('<div class="section-header">Arquitetura e Tecnologias</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
        <div class="card-title">🗄️ Apache Cassandra (DataStax Astra)</div>
        Cassandra-as-a-Service na nuvem, simplificando infraestrutura e permitindo foco na modelagem.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <div class="card-title">🐍 Python 3.x + astrapy</div>
        Flexibilidade para desenvolvimento rápido com integração nativa ao Astra DB.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <div class="card-title">☁️ Ambiente Cloud</div>
        Escalabilidade instantânea, alta disponibilidade e ambiente robusto.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <div class="card-title">🔐 Segurança</div>
        Gerenciamento seguro de credenciais com <code>python-dotenv</code> e <code>.gitignore</code>.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Modelagem
    st.markdown('<div class="section-header">💾 Modelagem de Dados</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    <strong>Princípio: Query-Driven Design</strong><br>
    No Cassandra, modelamos pelas <em>queries</em> que a aplicação fará, não por entidades (normalização SQL).
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Tabela: `usuarios`**")
        st.code("""CREATE TABLE usuarios (
    usuario_id UUID PRIMARY KEY,
    nome TEXT,
    email TEXT,
    criado_em TIMESTAMP
);""", language="sql")
    
    with col2:
        st.markdown("**Tabela: `mensagens`**")
        st.code("""CREATE TABLE mensagens (
    conversa_id UUID,
    mensagem_id TIMEUUID,
    remetente_id UUID,
    conteudo TEXT,
    PRIMARY KEY (conversa_id, mensagem_id)
) WITH CLUSTERING ORDER BY (mensagem_id DESC);""", language="sql")
    
    st.markdown("""
    <div class="comparison-good">
    <strong>Decisões:</strong> 
    <code>conversa_id</code> como Partition Key (agrupa mensagens fisicamente) | 
    <code>mensagem_id (TIMEUUID)</code> como Clustering Key (ordenação cronológica automática)
    </div>
    """, unsafe_allow_html=True)

# PÁGINA POR QUE CASSANDRA
elif menu == "⚡ Por que Cassandra?":
    st.markdown('<div class="section-header">Por que Cassandra ao invés de SQL?</div>', unsafe_allow_html=True)
    
    # Vantagens
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card-purple"><div class="card-title">⚡ Performance em Escrita</div>Milhões de operações/segundo sem locks, ideal para mensagens contínuas.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card-purple"><div class="card-title">🎯 Particionamento Inteligente</div>Cada conversa isolada em uma partição, garantindo acesso rápido.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card-purple"><div class="card-title">📈 Escalabilidade Linear</div>Adiciona nós = aumenta capacidade proporcionalmente, sem downtime.</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card-purple"><div class="card-title">⏰ Ordenação Nativa (TIMEUUID)</div>Mensagens armazenadas e recuperadas em ordem cronológica automaticamente.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card-purple"><div class="card-title">🌍 Alta Disponibilidade</div>Replicação multi-datacenter, disponibilidade contínua mesmo com falhas.</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Caso WhatsApp
    st.markdown('<div class="section-header">📊 Caso Real: WhatsApp (100B msgs/dia)</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**❌ Com SQL Tradicional:**")
        st.markdown('<div class="comparison-bad"><strong>🔒 Locks Constantes</strong> - Bloqueios frequentes, impacta concorrência</div>', unsafe_allow_html=True)
        st.markdown('<div class="comparison-bad"><strong>📊 Índices Gigantescos</strong> - Degrada performance</div>', unsafe_allow_html=True)
        st.markdown('<div class="comparison-bad"><strong>🔧 Sharding Complexo</strong> - Manual, caro, difícil</div>', unsafe_allow_html=True)
        st.markdown('<div class="comparison-bad"><strong>⏸️ Downtime</strong> - Manutenção exige interrupções</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("**✅ Com Cassandra:**")
        st.markdown('<div class="comparison-good"><strong>⚡ Escritas Distribuídas</strong> - Minimiza contenção</div>', unsafe_allow_html=True)
        st.markdown('<div class="comparison-good"><strong>🎯 Particionamento Automático</strong> - Acesso eficiente</div>', unsafe_allow_html=True)
        st.markdown('<div class="comparison-good"><strong>📈 Adição Flexível de Nós</strong> - Sem interromper serviço</div>', unsafe_allow_html=True)
        st.markdown('<div class="comparison-good"><strong>🔄 Replicação Transparente</strong> - Alta disponibilidade garantida</div>', unsafe_allow_html=True)

# PÁGINA CASOS REAIS
elif menu == "🌍 Casos Reais":
    st.markdown('<div class="section-header">Quem Usa Cassandra em Produção?</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    Estas empresas processam <strong>bilhões de operações por dia</strong> e escolheram Cassandra 
    pelos mesmos motivos: escalabilidade massiva, disponibilidade crítica e latência consistente.
    </div>
    """, unsafe_allow_html=True)
    
    # WhatsApp
    with st.expander("📱 **WhatsApp** - 100 Bilhões de Mensagens/Dia", expanded=True):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Desafio:**
            - Mais de **100 bilhões de mensagens por dia**
            - **2+ bilhões de usuários** ativos
            - Latência abaixo de 100ms
            - 99.99% de disponibilidade
            
            **Solução Cassandra:**
            - Armazena metadados de mensagens e estados de conversas
            - Particionamento por `user_id` ou `conversation_id`
            - Replicação multi-datacenter para alcance global
            - Escritas distribuídas sem locks
            
            **Resultado:**
            - Sistema escala horizontalmente conforme cresce
            - Adicionar capacidade = adicionar nós
            - Zero downtime mesmo com bilhões de mensagens
            """)
        
        with col2:
            st.markdown("""
            <div class="card-purple">
            <div style="font-size: 2rem; text-align: center; margin-bottom: 0.5rem;">📊</div>
            <div style="text-align: center;">
                <strong>100B+</strong><br>
                msgs/dia<br><br>
                <strong>2B+</strong><br>
                usuários<br><br>
                <strong>&lt;100ms</strong><br>
                latência
            </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Instagram
    with st.expander("📸 **Instagram** - Feed de Atividades"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Desafio:**
            - Bilhões de posts, comentários e likes
            - Feed personalizado para cada usuário
            - Ordenação cronológica inversa (mais recente primeiro)
            - Notificações em tempo real
            
            **Solução Cassandra:**
            - Tabela `user_feed` particionada por `user_id`
            - Clustering key com `timestamp` para ordenação temporal
            - Armazena IDs de posts + metadados
            - Timeline de atividades por usuário
            
            **Modelagem:**
            ```sql
            CREATE TABLE user_feed (
                user_id UUID,
                activity_time TIMEUUID,
                post_id UUID,
                activity_type TEXT,
                PRIMARY KEY (user_id, activity_time)
            ) WITH CLUSTERING ORDER BY (activity_time DESC);
            ```
            
            **Por que funciona:**
            - Buscar feed = leitura de uma partição (O(1))
            - Ordenação nativa por timestamp
            - LIMIT 50 = apenas 50 primeiros registros
            """)
        
        with col2:
            st.markdown("""
            <div class="comparison-good">
            <strong>Vantagem Principal:</strong><br><br>
            🎯 <strong>Ordenação Temporal Nativa</strong><br><br>
            Clustering key com TIMEUUID garante que posts apareçam na ordem correta sem índices custosos.
            </div>
            """, unsafe_allow_html=True)
    
    # Netflix
    with st.expander("🎬 **Netflix** - Histórico de Visualizações"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Desafio:**
            - **230 milhões de assinantes** globalmente
            - Histórico de visualizações de cada usuário
            - Sistema de recomendações em tempo real
            - Petabytes de dados de preferências
            
            **Solução Cassandra:**
            - Tabela `user_viewing_history` por `user_id`
            - Armazena: título assistido, timestamp, % assistido, dispositivo
            - Queries rápidas mesmo com milhões de visualizações por usuário
            - Alimenta algoritmo de recomendação em tempo real
            
            **Modelagem:**
            ```sql
            CREATE TABLE viewing_history (
                user_id UUID,
                watch_time TIMEUUID,
                content_id UUID,
                percent_watched INT,
                device_type TEXT,
                PRIMARY KEY (user_id, watch_time)
            ) WITH CLUSTERING ORDER BY (watch_time DESC);
            ```
            
            **Impacto:**
            - Recomendações personalizadas instantâneas
            - Performance consistente mesmo com petabytes
            - Escalabilidade linear conforme base de usuários cresce
            """)
        
        with col2:
            st.markdown("""
            <div class="card-purple">
            <div style="font-size: 2rem; text-align: center; margin-bottom: 0.5rem;">📈</div>
            <div style="text-align: center;">
                <strong>230M+</strong><br>
                assinantes<br><br>
                <strong>Petabytes</strong><br>
                de dados<br><br>
                <strong>Tempo Real</strong><br>
                recomendações
            </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Apple
    with st.expander("🍎 **Apple** - Apple Music & iCloud"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Desafio:**
            - **75 milhões de músicas** no catálogo
            - Preferências e playlists de milhões de usuários
            - Sincronização entre dispositivos (iPhone, Mac, iPad)
            - Disponibilidade 24/7 global
            
            **Solução Cassandra:**
            - Metadados de músicas (artista, álbum, gênero)
            - Playlists e preferências de usuários
            - Histórico de reprodução
            - Replicação multi-datacenter para baixa latência global
            
            **Por que Cassandra:**
            - Alta disponibilidade crítica (Apple não pode ficar fora do ar)
            - Escalabilidade para crescimento imprevisível
            - Replicação geográfica (datacenters EUA, Europa, Ásia)
            - Performance consistente independente do volume
            """)
        
        with col2:
            st.markdown("""
            <div class="comparison-good">
            <strong>Caso de Uso:</strong><br><br>
            🌍 <strong>Distribuição Global</strong><br><br>
            Replicação multi-datacenter garante que usuários no Japão tenham mesma latência que nos EUA.
            </div>
            """, unsafe_allow_html=True)
    
    # Uber
    with st.expander("🚗 **Uber** - Histórico de Viagens"):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Desafio:**
            - Milhões de viagens por dia
            - Histórico completo por usuário e motorista
            - Dados de localização em tempo real
            - Análise de padrões de viagem
            
            **Solução Cassandra:**
            - Tabela `trip_history` particionada por `user_id` ou `driver_id`
            - Armazena: origem, destino, valor, duração, avaliação
            - Time-series data para análise de padrões
            - Suporta consultas rápidas de "últimas 50 viagens"
            
            **Arquitetura:**
            ```sql
            CREATE TABLE trip_history (
                user_id UUID,
                trip_time TIMEUUID,
                trip_id UUID,
                origin TEXT,
                destination TEXT,
                fare DECIMAL,
                rating INT,
                PRIMARY KEY (user_id, trip_time)
            ) WITH CLUSTERING ORDER BY (trip_time DESC);
            ```
            """)
        
        with col2:
            st.markdown("""
            <div class="card-purple">
            <div style="font-size: 2rem; text-align: center; margin-bottom: 0.5rem;">🚗</div>
            <div style="text-align: center;">
                <strong>Milhões</strong><br>
                viagens/dia<br><br>
                <strong>Real-time</strong><br>
                tracking<br><br>
                <strong>Global</strong><br>
                operação
            </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Padrão Comum
    st.markdown('<div class="section-header">🎯 Padrão Comum Entre Todos</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="comparison-good">
        <strong>✅ Por que escolheram Cassandra:</strong><br><br>
        📈 <strong>Escalabilidade Massiva</strong><br>
        Bilhões de operações sem degradação<br><br>
        ⏱️ <strong>Latência Consistente</strong><br>
        Performance não degrada com volume<br><br>
        🌍 <strong>Distribuição Global</strong><br>
        Multi-datacenter nativo<br><br>
        🔄 <strong>Alta Disponibilidade</strong><br>
        99.99%+ uptime garantido
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="comparison-bad">
        <strong>❌ Por que SQL falharia:</strong><br><br>
        🔒 <strong>Locks em Escritas</strong><br>
        Contenção com alto volume<br><br>
        📊 <strong>Índices Custosos</strong><br>
        Performance degrada com bilhões de registros<br><br>
        🔧 <strong>Sharding Manual</strong><br>
        Complexo, caro, propenso a erros<br><br>
        ⏸️ <strong>Downtime</strong><br>
        Manutenção requer parar sistema
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tabela Comparativa
    st.markdown('<div class="section-header">📊 Comparação de Casos de Uso</div>', unsafe_allow_html=True)
    
    df_casos = pd.DataFrame({
        'Empresa': ['WhatsApp', 'Instagram', 'Netflix', 'Apple', 'Uber'],
        'Volume': ['100B msgs/dia', 'Bilhões posts', '230M users', '75M músicas', 'Milhões trips/dia'],
        'Caso de Uso': ['Metadados msgs', 'Feed timeline', 'Histórico views', 'Preferências', 'Trip history'],
        'Partition Key': ['conversation_id', 'user_id', 'user_id', 'user_id', 'user_id'],
        'Clustering Key': ['TIMEUUID', 'activity_time', 'watch_time', 'timestamp', 'trip_time'],
        'Vantagem Principal': ['Escritas massivas', 'Ordenação temporal', 'Petabytes data', 'Multi-DC', 'Time-series']
    })
    
    st.dataframe(df_casos, use_container_width=True, hide_index=True)

# PÁGINA IMPLEMENTAÇÃO
elif menu == "💡 Implementação":
    st.markdown('<div class="section-header">Conceitos Demonstrados</div>', unsafe_allow_html=True)
    
    concepts = [
        ("1", "Modelagem Orientada a Queries", "Definir esquema baseado em como os dados serão consultados."),
        ("2", "Partition Keys e Clustering Keys", "Partition Key para distribuição, Clustering Key para ordenação."),
        ("3", "Ordenação por TIMEUUID", "Garantir ordenação cronológica automática das mensagens."),
        ("4", "Distribuição de Dados", "Cassandra distribui dados eficientemente entre nós do cluster."),
        ("5", "Alta Disponibilidade", "Arquitetura suporta automaticamente escalabilidade horizontal.")
    ]
    
    for num, title, desc in concepts:
        st.markdown(f"""
        <div class="numbered-step">
            <div class="step-number">{num}</div>
            <div>
                <strong style="font-size: 1rem;">{title}</strong><br>
                <span style="font-size: 0.85rem; color: #666;">{desc}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # CHAT SIMULADO
    st.markdown('<div class="section-header">💬 Demonstração: Chat em Tempo Real</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Container do chat
        st.markdown("""
        <div style="background: white; padding: 1.2rem; border-radius: 12px; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.1); border: 1px solid #e0e0e0;">
        """, unsafe_allow_html=True)
        
        # Header do chat
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <strong style="font-size: 1.1rem;">💬 Conversa: João ↔ Maria</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # Área de mensagens
        st.markdown("""
        <div style="padding: 1rem; min-height: 250px; background: #fafafa; 
                    border-radius: 8px; margin-bottom: 1rem; overflow-y: auto;">
        """, unsafe_allow_html=True)
        
        # Mensagem 1 - João
        st.markdown("""
        <div style="background: #E3F2FD; padding: 0.8rem; border-radius: 12px; 
                    margin-bottom: 0.8rem; max-width: 75%; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div style="color: #1976D2; font-size: 0.8rem; font-weight: 600; margin-bottom: 0.3rem;">
                👤 João • 14:27
            </div>
            <div style="font-size: 0.95rem; color: #333;">
                Oi, tudo bem?
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Mensagem 2 - Maria
        st.markdown("""
        <div style="background: #F3E5F5; padding: 0.8rem; border-radius: 12px; 
                    margin-bottom: 0.8rem; max-width: 75%; margin-left: auto; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div style="color: #7B1FA2; font-size: 0.8rem; font-weight: 600; 
                        margin-bottom: 0.3rem; text-align: right;">
                14:28 • Maria 👥
            </div>
            <div style="font-size: 0.95rem; color: #333; text-align: right;">
                Tudo ótimo! E você?
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Mensagem 3 - João
        st.markdown("""
        <div style="background: #E3F2FD; padding: 0.8rem; border-radius: 12px; 
                    margin-bottom: 0.8rem; max-width: 75%; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div style="color: #1976D2; font-size: 0.8rem; font-weight: 600; margin-bottom: 0.3rem;">
                👤 João • 14:28
            </div>
            <div style="font-size: 0.95rem; color: #333;">
                Show! Vamos revisar o projeto? 📚
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Mensagem 4 - Maria
        st.markdown("""
        <div style="background: #F3E5F5; padding: 0.8rem; border-radius: 12px; 
                    max-width: 75%; margin-left: auto; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <div style="color: #7B1FA2; font-size: 0.8rem; font-weight: 600; 
                        margin-bottom: 0.3rem; text-align: right;">
                14:29 • Maria 👥
            </div>
            <div style="font-size: 0.95rem; color: #333; text-align: right;">
                Perfeito! Às 15h? 👍
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)  # Fecha área de mensagens
        
        # Input de mensagem
        st.text_input("Digite sua mensagem...", key="msg_input", label_visibility="collapsed")
        st.button("📤 Enviar Mensagem", type="primary", use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)  # Fecha container do chat
    
    with col2:
        st.markdown("""
        <div class="comparison-good">
        <strong>✅ Mensagem Enviada!</strong><br><br>
        ⏱️ <strong>Latência:</strong> 8ms<br>
        📊 <strong>Status:</strong> Replicada<br>
        🌍 <strong>Datacenters:</strong> 3<br>
        💾 <strong>Partição:</strong> conv-001<br>
        🔑 <strong>TIMEUUID:</strong> e2a7f3d0...
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="card">
        <strong style="font-size: 0.9rem;">🔄 O que aconteceu:</strong><br>
        <span style="font-size: 0.8rem;">
        1. Escrita no Commit Log<br>
        2. Inserção na Memtable<br>
        3. Retorno de sucesso<br>
        4. Replicação assíncrona
        </span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # TABELA DO CASSANDRA
    st.markdown('<div class="section-header">📊 Como os Dados Ficam no Cassandra</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
    As mensagens são organizadas em <strong>partições</strong> pela <code>conversa_id</code> e ordenadas 
    dentro de cada partição pelo <code>mensagem_id (TIMEUUID)</code> em ordem decrescente (mais recente primeiro).
    </div>
    """, unsafe_allow_html=True)
    
    # Tabela Partição 1
    st.markdown("**🔹 PARTIÇÃO 1:** `conversa_id = 'conv-001'` (João ↔ Maria)")
    
    df_conv1 = pd.DataFrame({
        'mensagem_id (TIMEUUID)': [
            'e2a7f3d0-c41b-11f0...',
            'e1f8b2c0-c41b-11f0...',
            'e0f37ca0-c41b-11f0...'
        ],
        'remetente_id': [
            'user-maria',
            'user-joao',
            'user-joao'
        ],
        'conteudo': [
            'Perfeito! Às 15h? 👍',
            'Show! Vamos revisar o projeto? 📚',
            'Oi, tudo bem?'
        ],
        'enviada_em': [
            '2025-11-18 14:29:15',
            '2025-11-18 14:28:42',
            '2025-11-18 14:27:23'
        ]
    })
    
    st.dataframe(df_conv1, use_container_width=True, hide_index=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabela Partição 2
    st.markdown("**🔹 PARTIÇÃO 2:** `conversa_id = 'conv-002'` (Lucas ↔ Ana)")
    
    df_conv2 = pd.DataFrame({
        'mensagem_id (TIMEUUID)': [
            'f3b8c4e0-c41b-11f0...',
            'f2d1a5d0-c41b-11f0...',
            'f1c28ba0-c41b-11f0...'
        ],
        'remetente_id': [
            'user-ana',
            'user-lucas',
            'user-ana'
        ],
        'conteudo': [
            'Combinado! 🎯',
            'Vamos apresentar às 15h?',
            'Oi Lucas, tudo certo?'
        ],
        'enviada_em': [
            '2025-11-18 14:30:55',
            '2025-11-18 14:30:28',
            '2025-11-18 14:30:01'
        ]
    })
    
    st.dataframe(df_conv2, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="comparison-good" style="margin-top: 1rem;">
    <strong>🎯 Observações Importantes:</strong><br>
    • Cada conversa = 1 partição isolada fisicamente<br>
    • Mensagens ordenadas por timestamp (DESC)<br>
    • Buscar conversa = leitura de UMA partição (O(1))<br>
    • Conversas diferentes em nós diferentes = balanceamento<br>
    • LIMIT 50 = lê apenas 50 primeiros registros da partição
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Query de exemplo
    st.markdown('<div class="section-header">🔍 Query em Ação</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Query CQL:**")
        st.code("""
SELECT * FROM mensagens 
WHERE conversa_id = 'conv-001'
ORDER BY mensagem_id DESC
LIMIT 50;
        """, language="sql")
    
    with col2:
        st.markdown("**Performance:**")
        st.markdown("""
        <div class="card">
        ⚡ <strong>Tempo:</strong> ~5ms<br>
        📍 <strong>Operação:</strong> Leitura de partição única<br>
        💾 <strong>Complexidade:</strong> O(1)<br>
        🎯 <strong>Dados lidos:</strong> Apenas 50 mensagens<br>
        ✅ <strong>Índice usado:</strong> Nenhum (ordenação nativa)
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown('<div class="section-header">🔒 Segurança e Boas Práticas</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
        <strong>Arquivos Ignorados (.gitignore):</strong><br>
        • <code>.env</code> (credenciais)<br>
        • <code>__pycache__/</code> (Python cache)<br>
        • <code>venv/</code> (ambientes virtuais)<br>
        • <code>.vscode/</code>, <code>.idea/</code> (IDEs)
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <strong>Licença Acadêmica:</strong><br>
        Projeto desenvolvido para fins educacionais. 
        Não se destina a uso comercial sem modificações apropriadas.
        </div>
        """, unsafe_allow_html=True)

# PÁGINA REFERÊNCIAS
elif menu == "📚 Referências":
    st.markdown('<div class="section-header">Referências</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="card">
        <div style="text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem;">📘</div>
        <strong>DataStax Astra</strong><br>
        <a href="https://docs.datastax.com/" target="_blank" style="font-size: 0.85rem;">Documentação Oficial</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
        <div style="text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem;">⭐</div>
        <strong>Apache Cassandra</strong><br>
        <a href="https://cassandra.apache.org/doc/latest/" target="_blank" style="font-size: 0.85rem;">Documentação Completa</a>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
        <div style="text-align: center; font-size: 2.5rem; margin-bottom: 0.5rem;">🎯</div>
        <strong>Best Practices</strong><br>
        <a href="https://cassandra.apache.org/doc/latest/data_modeling/" target="_blank" style="font-size: 0.85rem;">Data Modeling Guide</a>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 📖 Bibliografia")
    
    st.markdown("""
    <div class="card">
    <p style="font-size: 0.85rem; margin: 0.3rem 0;"><strong>FOWLER, Martin; SADALAGE, Pramod J.</strong> <em>NoSQL Distilled.</em> Addison-Wesley, 2012.</p>
    <p style="font-size: 0.85rem; margin: 0.3rem 0;"><strong>HEWITT, Eben.</strong> <em>Cassandra: The Definitive Guide.</em> O'Reilly Media, 2010.</p>
    <p style="font-size: 0.85rem; margin: 0.3rem 0;"><strong>LAKSHMAN, A.; MALIK, P.</strong> Cassandra: a decentralized structured storage system. <em>ACM SIGOPS,</em> 2010.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <strong>NoSQL com Cassandra: Sistema de Mensagens Escalável</strong><br>
    UEPB - Campus V | Ciência de Dados | 2025 | Feito com Gamma
</div>
""", unsafe_allow_html=True)
