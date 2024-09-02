from configparser import ConfigParser
import os

def ler_configuracoes(arquivo_config):
    """Lê o arquivo de configuração e retorna um dicionário com as configurações.

    Args:
        arquivo_config (str): Caminho completo para o arquivo de configuração.

    Returns:
        dict: Dicionário com as configurações, ou None se ocorrer algum erro.
    """

    if not os.path.exists(arquivo_config):
        print(
            f"\n(!) O arquivo de configuração '{arquivo_config}' não foi encontrado.\nCertifique-se que ele se encontra na raiz do diretório desta aplicação")
        return None

    config = ConfigParser(interpolation=None)
    config.read(arquivo_config, encoding='utf-8')

    configuracoes = {}
    try:
        # Sessão [config_oracle]
        configuracoes['user'] = config.get(
            'config_oracle', 'user')
        configuracoes['password'] = config.get(
            'config_oracle', 'password')
        configuracoes['dsn'] = config.get(
            'config_oracle', 'dsn')
        configuracoes['port'] = int(
            config.get('config_oracle', 'port'))
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        print(f"(!) Erro ao ler o arquivo de configuração: {e}")
        return None

    return configuracoes
