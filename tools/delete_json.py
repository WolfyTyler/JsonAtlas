import json

class DeleteJSON:
    def __init__(self, path, *key_to_delete, key = None, index = None, sub_index = None):
        self.path = path
        self.key_to_delete = key_to_delete
        self.key = key
        self.index = index
        self.sub_index = sub_index

    def read_json(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                return json.load(file)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo em '{self.path}' não encontrado.")
        except json.JSONDecodeError:
            raise ValueError(f"O arquivo '{self.path}' contém JSON inválido.")
        except RuntimeError as e:
            raise RuntimeError(f"Erro ao ler o arquivo JSON: {e}")

    def simple_dict(self, data): # Dicionário Simples.
        for key in self.key_to_delete:
            data.pop(key, None)

    def nested_dict(self, data): # Dicionário Aninhado.
        if self.key in data:
            item = data[self.key]
            if isinstance(item, dict):
                for key in self.key_to_delete:
                    item.pop(key, None)
            else:
                raise TypeError(f"Esperado um dicionário, mas recebido {type(item).__name__}.")
        else:
            raise KeyError(f"Chave '{self.key}' não existe no arquivo JSON.")

    def grouped_dict(self, data): # Dicionário Agrupado.
        if self.key in data: 
            if self.index >= 0 and self.index < len(data[self.key]):
                item = data[self.key][self.index]
                if isinstance(item, dict):
                    for key in self.key_to_delete:
                        item.pop(key, None)
                else:
                    raise TypeError(f"Esperado um dicionário, mas recebido {type(item).__name__}.")
            else:
                raise IndexError(f"Index '{self.index}' não existe no arquivo JSON.")
        else:
            raise KeyError(f"Chave '{self.key}' não existe no arquivo JSON.")

    def simple_list(self, data): # Lista Simples.
        if self.index >= 0 and self.index < len(data):
            item = data[self.index]
            if isinstance(item, dict):
                for key in self.key_to_delete:
                    item.pop(key, None)
            else:
                raise TypeError(f"Esperado um dicionário, mas recebido {type(item).__name__}.")
        else:
            raise IndexError(f"Index '{self.index}' não existe no arquivo JSON.")

    def nested_list(self, data): # Lista com Dicionário Aninhada.
        if self.index >= 0 and self.index < len(data):
            if self.key in data[self.index]:
                item = data[self.index][self.key]
                if isinstance(item, dict):
                    for key in self.key_to_delete:
                        item.pop(key, None)
                else:
                    raise TypeError(f"Esperado um dicionário, mas recebido {type(item).__name__}.")
            else:
                raise KeyError(f"Chave '{self.key}' não existe no arquivo JSON.")
        else:
            raise IndexError(f"Index '{self.index}' não existe no arquivo JSON.")

    def grouped_list(self, data): # Lista com Dicionário Agrupado.
        if self.index >= 0 and self.index < len(data):
            if self.key in data[self.index]:
                if self.sub_index >= 0 and self.sub_index < len(data[self.index][self.key]):
                    item = data[self.index][self.key][self.sub_index]
                    if isinstance(item, dict):
                        for Key in self.key_to_delete:
                            item.pop(Key, None)
                    else:
                        raise TypeError(f"Esperado um dicionário, mas recebido {type(item).__name__}.")
                else:
                    raise IndexError(f"Sub-index '{self.sub_index}' não existe no arquivo JSON.")
            else:
                raise KeyError(f"Chave '{self.key}' não existe no arquivo JSON.")
        else:
            raise IndexError(f"Index '{self.index}' não existe no arquivo JSON.")

    def delele_json(self):
        data = self.read_json()

        if isinstance(data, dict):
            if self.key is not None and self.index is not None:
                self.grouped_dict(data)

            elif self.key is not None:
                self.nested_dict(data)

            else:
                self.simple_dict(data)

        elif isinstance(data, list):
            if self.index is not None and self.key is not None and self.sub_index is not None:
                self.grouped_list(data)

            elif self.index is not None and self.key is not None:
                self.nested_list(data)

            elif self.index is not None:
                self.simple_list(data)

            else:
                raise IndexError(f"Parâmetro 'index' não pode ser vazio para lista.")

        try:
            with open(self.path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

        except Exception as e:
            raise RuntimeError(f"Erro ao salvar o arquivo JSON: {e}")
        
def deleteJson(path, *key_to_delete, key = None, index = None, sub_index = None):
    DeleteJSON(path, *key_to_delete, key=key, index=index, sub_index=sub_index).delele_json()

