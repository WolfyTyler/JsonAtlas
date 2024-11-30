import json
import os

class WriteJSON:
    def __init__(self, path, new_data, key = None, index = None, sub_index = None, structure_type = 'dict'):
        self.path = path
        self.new_data = new_data
        self.key = key
        self.index = index
        self.sub_index = sub_index
        self.structure_type = structure_type

    def read_json(self):
        try:
            if os.path.getsize(self.path) == 0:
                if self.structure_type == 'dict':
                    return {}
                elif self.structure_type == 'list':
                    return []
                else:
                    raise ValueError(f"Parâmetro 'structure_type' deve ser 'dict' ou 'list'.")

            with open(self.path, 'r', encoding='utf-8') as file:
                return json.load(file)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo em '{self.path}' não encontrado.")
        except RuntimeError as e:
            raise RuntimeError(f"Erro ao ler o arquivo JSON: {e}")

    def simple_dict(self, data): # Dicionário Simples.
        data.update(self.new_data)

    def nested_dict(self, data): # Dicionário Aninhado.
        if self.key not in data:
            data[self.key] = {}
        data[self.key] = self.new_data

    def grouped_dict(self, data): # Dicionário Agrupado.
        if self.key not in data:
            data[self.key] = []
        if self.index >= 0:
            while len(data[self.key]) <= self.index:
                data[self.key].append({})
            data[self.key][self.index] = self.new_data

    def simple_list(self, data): # Lista Simples.
        if self.index >= 0:
            while len(data) <= self.index:
                data.append({})
            data[self.index] = self.new_data
        else:
            raise IndexError(f"Parâmetro 'index' não pode ser vazio.")

    def nested_list(self, data): # Lista com Dicionário Aninhada.
        if self.index >= 0:
            while len(data) <= self.index:
                data.append({})
            if self.key not in data[self.index]:
                data[self.index][self.key] = {}
            data[self.index][self.key] = self.new_data
        else:
            raise IndexError(f"Parâmetro 'index' não pode ser vazio.")

    def grouped_list(self, data): # Lista com Dicionário Agrupado.
        if self.index >= 0:
            while len(data) <= self.index:
                data.append({})
            if self.key not in data[self.index]:
                data[self.index][self.key] = []
            if self.sub_index >= 0:
                while len(data[self.index][self.key]) <= self.sub_index:
                    data[self.index][self.key].append({})
                data[self.index][self.key][self.sub_index] = self.new_data
        else:
            raise IndexError(f"Parâmetro 'index' não pode ser vazio.")

    def write_json(self):
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
        
def writeJson(path, new_data, key = None, index = None, sub_index = None, structure_type = 'dict'):
    WriteJSON(path, new_data, key, index, sub_index, structure_type).write_json()