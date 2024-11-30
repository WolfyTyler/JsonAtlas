# **_Biblioteca JsonAtlas_**

![Versão do JsonAtlas](https://img.shields.io/badge/Distribuição-1.0.0-blue)
![Versões do Python](https://img.shields.io/badge/Python-3.8%2B-blue)

**JsonAtlas** é uma biblioteca projetada para **simplificar a manipulação de arquivos JSON**, oferecendo funcionalidades intuitivas para _leitura_, _escrita_ e _exclusão de dados_. Com **JsonAtlas**, os desenvolvedores podem gerenciar facilmente suas estruturas de dados em JSON, tornando o trabalho com informações nesse formato mais **eficiente e acessível**.

## _1. Função readJson:_

A função ``readJson`` lê um arquivo JSON no caminho especificado e retorna os dados em formato Python (dicionário ou lista). Caso o arquivo não seja encontrado ou o conteúdo do JSON seja inválido, a função gera erros específicos.

### **Parâmetros:**

- ``path`` **(str):** Caminho do arquivo JSON a ser lido. 

### **Exeções:**

- ``FileNotFoundError``: O arquivo especificado não foi encontrado.
- ``ValueError``: O conteúdo do arquivo não é um JSON válido.
- ``RuntimeError``: Qualquer outro erro durante a leitura do arquivo.`

### **Exemplo:**

```py
from JsonAtlas import readJson

data = readJson("database/data.json")
```

## _2. Função writeJson:_

A função ``writeJson`` manipula a escrita de dados em arquivos JSON. Ela permite adicionar ou atualizar dados em arquivos existentes, considerando diferentes tipos de estrutura (dicionário ou lista). A função oferece várias opções para modificar o arquivo de maneira simples ou aninhada.

### **Parâmetros:**

- ``path`` **(str)**: Caminho do arquivo JSON a ser modificado.
- ``new_data`` **(dict)**: Dados a serem adicionados ou atualizados.
- ``key`` **(str, opcional)**: Chave usada para acesso ou modificação de dados em dicionários ou listas.
- ``index`` **(int, opcional)**: Índice para acesso ou modificação em listas ou dicionários agrupados.
- ``sub_index`` **(int, opcional)**: Índice secundário usado para manipular listas dentro de dicionários agrupados.
- ``structure_type`` **(str, opcional)**: Define o tipo de estrutura do arquivo, podendo ser 'dict' ou 'list' (padrão é 'dict').

### **Exemplo:**

```py
from JsonAtlas import writeJson

writeJson('database/data.json', {'name': 'Maria', "age": 20}, key='user', index=0, sub_index=0)
```

## _3. Função deleteJson:_

A função ``deleteJson`` permite a exclusão de dados dentro de um arquivo JSON. É possível remover chaves específicas de um dicionário ou elementos de uma lista, considerando várias formas de organização do arquivo (simples, aninhado ou agrupado).

### **Parâmetros:**

- ``path`` **(str)**: Caminho do arquivo JSON a ser modificado.
- ``key_to_delete`` **(str)**:  Chaves a serem removidas do arquivo JSON.
- ``key``: **(str, opcional)**: Chave usada para acessar dados em dicionários ou listas.
- ``index`` **(int, opcional)**: Índice para acessar ou modificar listas ou dicionários agrupados.
- ``sub_index`` **(int, opcional)**: Índice secundário para listas dentro de dicionários agrupados.

### **Exemplo:**

```py
from JsonAtlas import deleteJson

deleteJson('database/data.json', "name", "age", key='user', index=0, sub_index=0)
```