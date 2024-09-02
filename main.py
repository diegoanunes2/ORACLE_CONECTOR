import oracledb
import query as qr
import pandas as pd
import functions as fn
import sys

# =========================================== #
# === Ler os dados do arquivo config.ini  === #
# =========================================== #

# Chamar a função para ler as configurações
configuracoes = fn.ler_configuracoes('config.ini')

if configuracoes:
    # Sessão [config_oracle]: Obtém as credenciais de acesso ao banco de dados Oracle
    user_bd = configuracoes['user']
    password_bd = configuracoes['password']
    dsn_bd = configuracoes['dsn']
    port_bd = int(configuracoes['port'])
    query_to_run = qr.query
    
else:
    sys.exit(1)

# Estabeleça a conexão com o banco de dados
connection = oracledb.connect(
    user = user_bd,
    password = password_bd,
    dsn = dsn_bd,
    port = port_bd)

# Crie um cursor para executar a query
cursor = connection.cursor()

# Execute a query desejada
cursor.execute(query_to_run)

# Obtenha todos os resultados
result = cursor.fetchall()

df = pd.DataFrame(result)
print(df)

cursor.close()
connection.close()
