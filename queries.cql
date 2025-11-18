-- ============================================
-- SISTEMA DE MENSAGENS - QUERIES CASSANDRA
-- ============================================

-- Usar o keyspace
USE default_keyspace;

-- ============================================
-- CONSULTAS DE USUÁRIOS
-- ============================================

-- Listar todos os usuários
SELECT * FROM usuarios;

-- Buscar usuário por ID (substitua pelo ID real)
SELECT * FROM usuarios WHERE usuario_id = 3e32601e-25ed-4ee8-b9e0-57312efa65fa;

-- ============================================
-- CONSULTAS DE MENSAGENS
-- ============================================

-- Listar todas as mensagens
SELECT * FROM mensagens;

-- Buscar mensagens de uma conversa específica (substitua pelo ID real)
SELECT * FROM mensagens 
WHERE conversa_id = 1d89c60a-cfb8-40b5-90d5-8cf1796ab60b
ORDER BY mensagem_id DESC;

-- Contar mensagens por conversa
SELECT conversa_id, COUNT(*) as total_mensagens 
FROM mensagens 
GROUP BY conversa_id;

-- ============================================
-- INSERÇÕES DE EXEMPLO
-- ============================================

-- Inserir novo usuário
INSERT INTO usuarios (usuario_id, nome, email, criado_em) 
VALUES (uuid(), 'Carlos Lima', 'carlos@email.com', toTimestamp(now()));

-- Inserir nova mensagem
INSERT INTO mensagens (conversa_id, mensagem_id, remetente_id, destinatario_id, conteudo, enviada_em)
VALUES (uuid(), now(), uuid(), uuid(), 'Olá! Como vai?', toTimestamp(now()));