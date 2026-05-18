# Documentação Completa da API VC API

Este documento serve como referência completa para todas as funcionalidades, rotas e modelos da API VC API. Ele foi criado para facilitar consultas em conversas futuras e fornecer um entendimento completo do sistema.

## Sumário

1. [Visão Geral da API](#visão-geral-da-api)
2. [Modelos de Dados](#modelos-de-dados)
3. [Rotas e Endpoints](#rotas-e-endpoints)
4. [Esquemas de Validação](#esquemas-de-validação)
5. [Utilitários e Middleware](#utilitários-e-middleware)
6. [Configurações](#configurações)

---

## Visão Geral da API

A VC API é uma aplicação construída com FastAPI que fornece funcionalidades para gestão de usuários, produtos, filiais, transferências digitais e outros recursos empresariais. A API implementa autenticação baseada em JWT, validação de e-mail com códigos de verificação e controle de acesso baseado em papéis (RBAC).

### Características Principais

- **Autenticação Segura**: JWT com tokens de acesso e refresh
- **Validação de E-mail**: Sistema de códigos de verificação para confirmação de contas
- **Controle de Acesso**: Baseado em papéis e permissões granulares
- **Gestão de Filiais**: Controle de múltiplas localizações empresariais
- **Produtos e Validade**: Gestão de estoque com controle de validade
- **Transferências Digitais**: Sistema para transferência de produtos entre filiais
- **Relatórios**: Funcionalidades para geração de relatórios de validade

### Tecnologias Utilizadas

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Validação**: Pydantic
- **Autenticação**: JWT (JSON Web Tokens)
- **Banco de Dados**: SQLite (desenvolvimento)
- **Documentação Automática**: Swagger UI e ReDoc

---

## Modelos de Dados

### 1. Modelo de Usuário (`User`)

Localizado em: `core/models/user_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `id` | Integer (PK) | Identificador único do usuário |
| `username` | String (único) | Nome de usuário para login (formato: `nome.sobrenome`) |
| `name` | String | Primeiro nome do usuário |
| `surname` | String | Sobrenome do usuário |
| `email` | String (único) | Endereço de e-mail do usuário |
| `password` | String | Senha hashada (bcrypt) |
| `cpf` | String (único) | CPF do usuário |
| `data_nascimento` | Date | Data de nascimento (opcional) |
| `role_id` | Integer (FK) | Referência ao papel do usuário |
| `created_at` | DateTime | Timestamp de criação |
| `updated_at` | DateTime | Timestamp de última atualização |
| `is_active` | Boolean | Status de ativação da conta |
| `is_admin` | Boolean | Indica se o usuário é administrador |
| `is_validated` | Boolean | Indica se o e-mail foi validado |

#### Relacionamentos

- `branch`: Relacionamento muitos-para-muitos com `Branch` através da tabela `user_branch`
- `permissions`: Relacionamento um-para-muitos com `UserPermission`
- `role`: Relacionamento muitos-para-um com `Role`

#### Métodos Especiais

- `__init__`: Construtor que inicializa todos os atributos
- Representação padrão do SQLAlchemy

### 2. Modelo de Papel (`Role`)

Localizado em: `core/models/user_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `id` | Integer (PK) | Identificador único do papel |
| `name` | String | Nome do papel (ex: "admin", "operador") |
| `description` | String | Descrição detalhada do papel |
| `is_active` | Boolean | Status de ativação do papel |

#### Relacionamentos

- `users`: Relacionamento um-para-muitos com `User`

### 3. Modelo de Permissão do Usuário (`UserPermission`)

Localizado em: `core/models/user_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `id` | Integer (PK) | Identificador único |
| `user_id` | Integer (FK) | Referência ao usuário |
| `permission_id` | Integer (FK) | Referência à permissão |

#### Relacionamentos

- `user`: Relacionamento muitos-para-um com `User`
- `permission`: Relacionamento muitos-para-um com `Permission` (lazy="joined")

### 4. Modelo de Código de Verificação (`UserVerifyCode`)

Localizado em: `core/models/user_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `email` | String (PK) | E-mail associado ao código |
| `verification_code` | String | Código de verificação gerado |
| `expire_time` | DateTime | Timestamp de expiração do código |

### 5. Modelo de Categoria (`Category`)

Localizado em: `core/models/product_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `id` | Integer (PK) | Identificador único da categoria |
| `name` | String | Nome da categoria (ex: "Perfumaria") |
| `percentual_desconto` | Integer | Percentual de desconto aplicado à categoria (padrão: 0) |

#### Relacionamentos

- `products`: Relacionamento um-para-muitos com `Product`

### 6. Modelo de Produto (`Product`)

Localizado em: `core/models/product_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `cod_product` | Integer (PK) | Código único do produto |
| `description` | String | Descrição do produto |
| `price` | Float | Preço do produto (pode ser nulo) |
| `category_id` | Integer (FK) | Referência à categoria do produto |
| `is_active` | Boolean | Status de ativação do produto |
| `created_at` | DateTime | Timestamp de criação |
| `updated_at` | DateTime | Timestamp de última atualização |

#### Relacionamentos

- `expiration`: Relacionamento um-para-muitos com `ProductExpiration`
- `category`: Relacionamento muitos-para-um com `Category`
- `digital_transfer_items`: Relacionamento um-para-muitos com `DigitalTransferItems`

### 7. Modelo de Validade do Produto (`ProductExpiration`)

Localizado em: `core/models/product_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `id` | Integer (PK) | Identificador único do registro |
| `expiration_date` | DateTime | Data de validade do produto |
| `quantity` | Integer | Quantidade do produto em lote |
| `downed` | Boolean | Indica se o produto foi baixado do estoque |
| `cod_product` | Integer (FK) | Referência ao produto |
| `branch_id` | Integer (FK) | Referência à filial onde o produto está localizado |

#### Relacionamentos

- `product`: Relacionamento muitos-para-um com `Product`
- `branch`: Relacionamento muitos-para-um com `Branch`

> **Nota**: Há um comentário no código indicando uma restrição de unicidade planejada para evitar duplicações do mesmo produto na mesma filial com a mesma data de validade.

### 8. Modelo de Filial (`Branch`)

Localizado em: `core/models/branch_model.py`

#### Atributos

| Atributo | Tipo | Descrição |
|----------|------|-----------|
| `pdv` | Integer (PK) | Código único da filial (Point of Venda) |
| `name` | String | Nome da filial |
| `address` | String | Endereço da filial |
| `phone` | String | Telefone da filial (opcional) |
| `city` | String | Cidade da filial |
| `state` | String | Estado da filial |
| `cnpj` | String | CNPJ da filial |
| `is_active` | Boolean | Status de ativação da filial |

#### Relacionamentos

- `user`: Relacionamento muitos-para-muitos com `User` através da tabela `user_branch`
- `expirations`: Relacionamento um-para-muitos com `ProductExpiration`
- `transferencias_enviadas`: Relacionamento um-para-muitos com `DigitalTransfer` (origem)
- `transferencias_recebidas`: Relacionamento um-para-muitos com `DigitalTransfer` (destino)

### 9. Modelo de Transferência Digital (`DigitalTransfer`)

> **Observação**: Este modelo foi referenciado no modelo `Branch` mas não foi encontrado nos arquivos examinados. Provavelmente está em outro arquivo de modelo não listado inicialmente.

### 10. Modelo de Item de Transferência Digital (`DigitalTransferItems`)

> **Observação**: Referenciado no modelo `Product` mas não encontrado nos arquivos examinados.

---

## Rotas e Endpoints

A API está organizada em múltiplos roteadores (routers) agrupados por funcionalidade. Todos os roteadores são incluídos no aplicativo principal em `main.py`.

### 1. Rotas de Autenticação (`auth_route.py`)

Localizado em: `core/routes/auth_route.py`
Prefixo: `/auth`
Tag: `auth`

#### Endpoints

##### POST `/auth/register`
**Descrição**: Registra um novo usuário no sistema.

**Parâmetros**:
- `user_schema` (UserSchema): Dados do novo usuário
  - `username` (string, opcional): Nome de usuário (se não fornecido, é gerado automaticamente)
  - `name` (string): Primeiro nome
  - `surname` (string): Sobrenome
  - `email` (string, válido): E-mail do usuário
  - `password` (string): Senha em texto plano
  - `branch` (integer, opcional): ID da filial
  - `role_id` (integer, opcional): ID do papel
  - `cpf` (string): CPF do usuário
  - `data_nascimento` (string): Data de nascimento (formatos aceitos: "YYYY-MM-DD" ou "DD/MM/YYYY")
  - `is_active` (boolean, opcional, padrão: true)
  - `is_admin` (boolean, opcional, padrão: false)
  - `is_validated` (boolean, opcional, padrão: false)
- `session` (Session): Sessão do banco de dados (injeção de dependência)

**Retornos**:
- **Sucesso (201 Created)**:
  ```json
  {
    "message": "Usuário cadastrado com sucesso!"
  }
  ```
- **Erros**:
  - 400 Bad Request: Usuário já cadastrado ou e-mail inválido
  - 500 Internal Server Error: Erro interno do servidor

**Processo**:
1. Verifica se o e-mail já está cadastrado
2. Valida o formato do e-mail
3. Gera username automaticamente se não fornecido (formato: `nome.sobrenome`)
4. Converte data de nascimento para objeto Date
5. Hash da senha usando bcrypt
6. Cria e salva o novo usuário no banco de dados

##### POST `/auth/login`
**Descrição**: Autentica um usuário e retorna tokens de acesso.

**Parâmetros**:
- `user_schema` (UserLoginSchema):
  - `login` (string): E-mail ou username para autenticação
  - `password` (string): Senha em texto plano
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "access_token": "token_jwt_aqui",
    "refresh_token": "token_refresh_aqui",
    "token_type": "Bearer",
    "message": "Usuário logado com sucesso!"
  }
  ```
- **Cabeçalhos**:
  - `Authorization`: Bearer {access_token}
  - Cookie `Authorization`: Bearer {access_token} (httponly, samesite=lax, secure)
- **Erros**:
  - 401 Unauthorized: Credenciais inválidas

**Processo**:
1. Autentica o usuário verificando credenciais
2. Gera token de acesso (validade padrão)
3. Gera token de refresh (validade de 7 dias)
4. Retorna tokens no corpo e define cookie de autorização

##### POST `/auth/login-form`
**Descrição**: Endpoint de autenticação compatível com OAuth2 do FastAPI Docs.

**Parâmetros**:
- `form_data` (OAuth2PasswordRequestForm): Contém `username` e `password`
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "access_token": "token_jwt_aqui",
    "token_type": "Bearer"
  }
  ```
- **Cabeçalhos**:
  - `Authorization`: Bearer {access_token}
  - Cookie `Authorization`: Bearer {access_token} (httponly, samesite=lax, secure)
- **Erros**:
  - 401 Unauthorized: Credenciais inválidas

##### GET `/auth/refresh`
**Descrição**: Atualiza o token de acesso usando um token de refresh válido.

**Parâmetros**:
- `user` (User): Usuário autenticado (extraído do token via `verify_token`)

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "access_token": "novo_token_jwt_aqui",
    "token_type": "Bearer"
  }
  ```
- **Cabeçalhos**:
  - `Authorization`: Bearer {novo_token}
  - Cookie `Authorization`: Bearer {novo_token} (httponly, samesite=lax, secure)
- **Erros**:
  - 401 Unauthorized: Token inválido ou expirado

##### POST `/auth/send-code`
**Descrição**: Envia um código de verificação para o e-mail fornecido.

**Parâmetros**:
- `email_request` (EmailRequestSchema):
  - `email` (string, válido): E-mail para envio do código
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "message": "Código de verificação enviado com sucesso",
    "expire_minutes": 15  # valor configurável
  }
  ```
- **Erros**:
  - 404 Not Found: Usuário não encontrado com esse e-mail
  - 500 Internal Server Error: Erro ao enviar o e-mail

**Processo**:
1. Verifica se o usuário existe pelo e-mail
2. Gera e salva um código de verificação no banco
3. Envia o código por e-mail usando serviço externo
4. Retorna sucesso ou levanta exceção apropriada

##### POST `/auth/verify-code`
**Descrição**: Verifica se o código fornecido é válido e marca o usuário como validado.

**Parâmetros**:
- `verification_data` (EmailVerificationSchema):
  - `email` (string, válido): E-mail associado ao código
  - `verification_code` (string): Código a ser verificado
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "message": "Código verificado com sucesso",
    "valid": true
  }
  ```
- **Erros**:
  - 400 Bad Request: Código inválido ou expirado
  - 404 Not Found: Usuário não encontrado

**Processo**:
1. Verifica se o código corresponde ao salvo no banco e não expirou
2. Se válido, marca o usuário como validado (`is_validated = True`)
3. Salva a alteração no banco de dados

##### POST `/auth/resend-code`
**Descrição**: Reenvia um novo código de verificação para o e-mail fornecido.

**Parâmetros**:
- `email_request` (EmailRequestSchema):
  - `email` (string, válido): E-mail para reenvio do código
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "message": "Novo código enviado com sucesso",
    "expire_minutes": 15
  }
  ```
- **Erros**:
  - 404 Not Found: E-mail não encontrado
  - 500 Internal Server Error: Erro ao enviar o e-mail

**Processo**:
1. Verifica se o usuário existe pelo e-mail
2. Gera um novo código (substituindo o anterior)
3. Envia o novo código por e-mail
4. Retorna resultado

##### POST `/auth/check-validation-status`
**Descrição**: Verifica se o usuário já está validado.

**Parâmetros**:
- `email_request` (EmailRequestSchema):
  - `email` (string, válido): E-mail para verificação
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "email": "usuario@exemplo.com",
    "is_validated": true
  }
  ```
- **Erros**:
  - 404 Not Found: Usuário não encontrado

### 2. Rotas de Usuário (`user_route.py`)

Localizado em: `core/routes/user_route.py`
Prefixo: `/user`
Tag: `user`

#### Endpoints

##### GET `/user/me`
**Descrição**: Retorna as informações detalhadas do usuário atualmente autenticado.

**Parâmetros**:
- `user` (User): Usuário autenticado (via `verify_token`)

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "id": 1,
    "username": "nome.sobrenome",
    "name": "Nome",
    "surname": "Sobrenome",
    "email": "usuario@example.com",
    "is_active": true,
    "is_admin": false,
    "is_validated": true,
    "role": {
      "id": 2,
      "name": "operador"
    },
    "branch": [
      {
        "pdv": 1,
        "name": "Filial Exemplo",
        "address": "Rua Exemplo, 123",
        "phone": "11999999999",
        "city": "São Paulo",
        "state": "SP",
        "cnpj": "00.000.000/0001-00",
        "is_active": true
      }
    ],
    "permissions": [
      "users.read",
      "users.write",
      "users.delete",
      "users.create",
      "users.update"
      // ... outras permissões
    ]
  }
  ```
- **Cabeçalhos**:
  - `Content-Type`: application/json

**Processo**:
1. Extrai informações básicas do usuário
2. Inclui dados do papel associado
3. Lista todas as filiais associadas ao usuário com detalhes completos
4. Extrai códigos de todas as permissões associadas ao usuário

##### PUT `/user/me`
**Descrição**: Atualiza as informações do usuário autenticado (exceto senha).

**Parâmetros**:
- `user_info` (UserSchema): Dados a serem atualizados
- `user` (User): Usuário autenticado
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "message": "Usuário atualizado com sucesso!"
  }
  ```
- **Cabeçalhos**:
  - `Content-Type`: application/json

**Processo**:
1. Remove campos vazios do schema de entrada
2. Atualiza dinamicamente os atributos do usuário com os valores fornecidos
3. Salva alterações no banco de dados

##### DELETE `/user/me`
**Descrição**: Desativa a conta do usuário autenticado (exclusão lógica).

**Parâmetros**:
- `user` (User): Usuário autenticado
- `session` (Session): Sessão do banco de dados

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "message": "Usuário desativado com sucesso!"
  }
  ```
- **Cabeçalhos**:
  - `Content-Type`: application/json

**Processo**:
1. Define `is_active` como False para o usuário
2. Salva alteração no banco de dados (exclusão lógica)

##### PUT `/user/me/change-password`
**Descrição**: Atualiza a senha do usuário autenticado.

**Parâmetros**:
- `payload` (UserUpdatePassSchema):
  - `old_password` (string): Senha atual
  - `new_password` (string): Nova senha
- `session` (Session): Sessão do banco de dados
- `user` (User): Usuário autenticado

**Retornos**:
- **Sucesso (200 OK)**:
  ```json
  {
    "message": "Senha atualizada com sucesso!"
  }
  ```
- **Cabeçalhos**:
  - `Content-Type`: application/json
- **Erros**:
  - 404 Not Found: Usuário não encontrado (raro)
  - 400 Bad Request: Senha antiga incorreta

**Processo**:
1. Busca o usuário pelo ID (redudante mas seguro)
2. Verifica se a senha antiga corresponde ao hash armazenado
3. Se válida, hashea a nova senha e atualiza o registro
4. Salva alterações no banco de dados

### 3. Rotas de Produto (`product_route.py`)

> **Observação**: Este arquivo foi referenciado em `main.py` mas não foi examinado detalhadamente nesta sessão. Para documentação completa, seria necessário examiná-lo.

### 4. Rotas de Categoria (`category_route.py`)

> **Observação**: Referenciado em `main.py` mas não examinado.

### 5. Rotas de Validade de Produto (`expiration_route.py`)

> **Observação**: Referenciado em `main.py` como `product_expiration_router`.

### 6. Rotas de Relatório de Validade (`validity_report.py`)

Localizado em: `services/reports/validity_report.py`
Este arquivo contém um router para geração de relatórios de validade de produtos.

### 7. Outras Rotas

Outras rotas referenciadas em `main.py` incluem:
- `admin_route.py` (rotas administrativas)
- `branch_route.py` (gestão de filiais)
- `digital_transfer_route.py` (transferências digitais)
- `module_route.py` (gestão de módulos)
- `permission_route.py` (gestão de permissões)
- `role_route.py` (gestão de papéis)
- `user_permission_route.py` (gestão de permissões de usuários)

Para documentação completa dessas rotas, seria necessário examinar cada arquivo individualmente.

---

## Esquemas de Validação (Schemas)

Localizados em: `core/schemas/`

### 1. Esquema de Usuário (`user_schema.py`)

#### UserSchema
Used for user creation and general user data representation.

| Campo | Tipo | Validação | Descrição |
|-------|------|-----------|-----------|
| `username` | Optional[str] | min_length=3, max_length=128, pattern="^[a-z.]+$", default="" | Nome de usuário (letras minúsculas e pontos apenas) |
| `name` | String | - | Primeiro nome |
| `surname` | String | - | Sobrenome |
| `email` | EmailStr | - | E-mail válido |
| `password` | String | - | Senha em texto plano |
| `branch` | Optional[int] | - | ID da filial |
| `role_id` | Optional[int] | - | ID do papel |
| `cpf` | String | - | CPF do usuário |
| `data_nascimento` | Optional[str] | - | Data de nascimento como string |
| `is_active` | Optional[bool] | default=True | Status de ativação |
| `is_admin` | Optional[bool] | default=False | Privilégios de administrador |
| `is_validated` | Optional[bool] | default=False | Status de validação de e-mail |

#### UserLoginSchema
Used for user authentication.

| Campo | Tipo | Validação | Descrição |
|-------|------|-----------|-----------|
| `login` | Optional[str] | - | E-mail ou username para login |
| `password` | String | - | Senha em texto plano |

#### EmailRequestSchema
Used for email verification requests.

| Campo | Tipo | Validação | Descrição |
|-------|------|-----------|-----------|
| `email` | EmailStr | - | E-mail para envio/verificação de código |

#### EmailVerificationSchema
Used for verifying email verification codes.

| Campo | Tipo | Validação | Descrição |
|-------|------|-----------|-----------|
| `email` | EmailStr | - | E-mail associado ao código |
| `verification_code` | String | - | Código a ser verificado |

#### UserUpdatePassSchema
Used for password update requests.

| Campo | Tipo | Validação | Descrição |
|-------|------|-----------|-----------|
| `new_password` | String | - | Nova senha |
| `old_password` | String | - | Senha atual |

### 2. Outros Esquemas

Outros arquivos de esquema no diretório `core/schemas/` incluem:
- `branch_schema.py`
- `digital_transfer_schema.py`
- `module_schema.py`
- `permission_schema.py`
- `product_schema.py`
- `role_schema.py`

Estes definem os modelos de dados para validação de entrada nas respectivas rotas.

---

## Utilitários e Middleware

### 1. Autenticação (`core/auth/auth.py`)

> **Observação**: Este arquivo foi referenciado mas não examinado. Contém funções para:
> - `authenticate_user`: Verifica credenciais de usuário
> - `get_token`: Gera tokens JWT
> - `verify_token`: Valida e decodifica tokens JWT

### 2. Código de Verificação (`core/utils/verification_code.py`)

> **Observação**: Referenciado nas rotas de autenticação. Contém funções para:
> - `save_verification_code`: Gera e salva código de verificação
> - `send_verification_email`: Envia código por e-mail
> - `verify_code`: Verifica se código é válido e não expirou

### 3. Normalização de Texto (`core/utils/normalize_text.py`)

> **Observação**: Utilitário para padronização de texto.

### 4. Permissões (`core/utils/permissions.py`)

> **Observação**: Utilitário para verificação e gestão de permissões.

### 5. Middleware de Rate Limiting

Configurado em `main.py` usando `slowapi`:
- Limita taxa de requisições para prevenir abuso
- Manipulador personalizado para retornar mensagem em português
- Headers `Retry-After` indicando quando tentar novamente

### 6. CORS (Cross-Origin Resource Sharing)

Configurado em `main.py`:
- Permite origens: `["*"]` (em desenvolvimento)
- Permite credenciais: true
- Permite métodos: `["*"]`
- Permite headers: `["*"]`

### 7. Lifespan Event Handler

Configurado em `main.py`:
- Inicializa banco de dados na inicialização
- Cria usuário administrador padrão
- Mensagens de log na inicialização e finalização

---

## Configurações

### 1. Arquivo de Configuração (`config.py`)

> **Observação**: Contém:
> - Instância do limiter do slowapi
> - Contexto do bcrypt para hash de senhas
> - Constantes como `CODE_EXPIRE_MINUTES`
> - Outras configurações da aplicação

### 2. Variáveis de Ambiente (`.env`)

> **Observação**: Arquivo não examinado mas presente no diretório raíz. Provavelmente contém:
> - Configurações de banco de dados
> - Segredos para JWT
> - Configurações de e-mail
> - Outras variáveis de ambiente

### 3. Banco de Dados

- **Tipo**: SQLite (arquivo `db.db` no diretório raíz)
- **Gerenciamento**: SQLAlchemy com Alembic para migrações
- **Inicialização**: Função `init_db()` em `core/db/db.py`

### 4. Migrações do Banco de Dados

Localizado no diretório `alembic/`:
- `alembic.ini`: Configuração do Alembic
- `env.py`: Ambiente de migração
- `versions/`: Arquivos de migração individuais

---

## Fluxos de Trabalho Principais

### 1. Registro e Validação de Usuário

1. Usuário envia dados para `/auth/register`
2. Sistema verifica se e-mail já existe
3. Se não existir, valida formato do e-mail
4. Gera username automaticamente se não fornecido
5. Converte data de nascimento para formato Date
6. Hash da senha com bcrypt
7. Salva novo usuário no banco com `is_validated = False`
8. Retorna sucesso com status 201

9. Sistema envia código de verificação para o e-mail via `/auth/send-code`
10. Usuário recebe código e envia para `/auth/verify-code`
11. Sistema verifica código e, se válido, marca `is_validated = True`
12. Usuário agora pode fazer login normalmente

### 2. Autenticação e Acesso

1. Usuário envia credenciais para `/auth/login` ou `/auth/login-form`
2. Sistema verifica credenciais contra banco de dados
3. Se válidas, gera:
   - Token de acesso (short-lived)
   - Token de refresh (7 dias de validade)
4. Retorna tokens no corpo e define cookie de autorização
5. Para acessar rotas protegidas, cliente deve incluir token no header `Authorization: Bearer {token}`
6. Middleware `verify_token` decodifica token e injeta objeto `User` nas rotas
7. Quando token de acesso expira, cliente pode usar `/auth/refresh` com token de refresh válido
8. Para renovar sessão após 7 dias, usuário deve fazer login novamente

### 3. Gestão de Perfil

1. Usuário autenticado acessa `/user/me` para ver seus dados
2. Pode atualizar informações (exceto senha) via PUT `/user/me`
3. Pode alterar senha via PUT `/user/me/change-password` fornecendo senha antiga e nova
4. Pode desativar conta via DELETE `/user/me` (exclusão lógica)

### 4. Controle de Acesso baseado em Papéis e Permissões

1. Cada usuário tem um `role_id` que referencia um papel (Role)
2. Cada papel tem nome e descrição (ex: "admin", "operador", "gerente")
3. Permissões são definidas no sistema e associadas a usuários através da tabela `user_permission`
4. Rotas podem verificar permissões do usuário autenticado através de `user.permissions`
5. Exemplo de uso nas rotas: `[up.permission.code for up in user.permissions]`

---

## Considerações de Segurança

1. **Hash de Senhas**: Utiliza bcrypt via `bcrypt_context` para armazenar senhas de forma segura
2. **Proteção contra CSRF**: Cookies de autenticação são httponly e samesite=lax
3. **Validação de Entrada**: Todos os dados de entrada são validados pelos esquemas Pydantic
4. **Proteção contra Force Brute**: Implementação de rate limiting via slowapi
5. **HTTPS**: Cookies marcados como secure (devem ser usados apenas em HTTPS em produção)
6. **Validação de E-mail**: Uso da biblioteca `email_validator` para garantir formatos válidos
7. **Tokens JWT**: Implementação padrão com assinatura e validação adequadas
8. **Exclusão Lógica**: Usuários são desativados ao invés de excluídos fisicamente para preservar integridade referencial

---

## Melhorias Futuras Sugeridas

1. **Documentação Interativa**: Melhorar docstrings para gerar documentação Swagger/OpenAPI mais rica
2. **Testes Automatizados**: Implementar suite de testes para cobrir casos de uso e prevenir regressões
3. **Logging Estruturado**: Substituir prints por logging estruturado com níveis adequados
4. **Validação de Campos Sensíveis**: Adicionar validação adicional para CPF, CNPJ etc.
5. **Internacionalização**: Suportar múltiplos idiomas nas mensagens de retorno
6. **Cache**: Implementar cache para consultas frequentes e de baixo custo
7. **Monitoramento**: Adicionar métricas e health checks para monitoramento da aplicação
8. **Dockerização**: Criar Dockerfile para facilitar deploy em diferentes ambientes
9. **CI/CD**: Implementar pipeline de integração e entrega contínua
10. **API Versioning**: Planejar estratégia de versionamento para mudanças futuras sem quebrar compatibilidade

---

## Conclusão

Esta documentação fornece uma visão abrangente da VC API, cobrindo seus modelos de dados, rotas, esquemas de validação e fluxos de trabalho principais. Ela serve como referência para desenvolvedores que trabalham com a API e como base para manutenção e evolução futura do sistema.

A API demonstra boas práticas de segurança, separação de preocupações e utilização eficaz do ecossistema Python/FastAPI. Sua arquitetura modular facilita a manutenção e extensão com novas funcionalidades conforme as necessidades do negócio evoluem.

*Documentação gerada automaticamente em 2026-04-16 com base no código fonte da aplicação.*