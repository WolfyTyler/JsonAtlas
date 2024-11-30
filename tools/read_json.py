import json

def readJson(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo JSON em '{path}' não foi encontrado.")
    except json.JSONDecodeError:
        raise ValueError(f"O arquivo '{path}' contém JSON inválido.")
    except Exception as e:
        raise RuntimeError(f"Erro ao ler o arquivo: {e}")