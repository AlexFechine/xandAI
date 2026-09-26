# xandAI

Um chatbot de IA local, desenvolvido com o intuito de estudar e entender a tecnologia **LangChain**

## Tecnologias utlizadas

```
Python
LangChain
Ollama
llama 3.2
```

## Funcionalidades

```
Memória temporária para conversação
Chat interativo via terminal
Execução local com o Ollama
Integração com LangChain
```

## Como utilizar

**Instalação**
**1. Clone o repositório**
```
git clone https://github.com/AlexFechine/xandAI.git
```
```
cd xandAI
```

**2. Crie o ambiente virtual**

```
python -m venv .venv
```

**No Windows PowerShell:**

```
.venv\Scripts\Activate.ps1
```

**3. Instale as dependências**

```
pip install -r requirements.txt
```

**4. Instale e configure o Ollama**

**Instale o Ollama e baixe o modelo utilizado pelo XandAi:**

```
ollama pull llama3.2
```

Certifique-se de que o Ollama esteja funcionando antes de iniciar o chatbot.

**5. Execute o XandAi**

A partir da raiz do projeto:

```
python src/xandAi/main.py
```
¨
## Próximos objetivos

- Memória persistente

- Memória semântica

- Embeddings

- Banco de dados vetorial

- Tool calling

- RAG

- Interface web

##
Esse projeto está sendo desenvolvido para fins educacionais e experimentais.
