from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

if __name__ == "__main__":
    
    print("xandAi iniciou!")
    system_prompt = SystemMessage("Responda as perguntas do usuário da melhor forma possível, utilizando seus conhecimentos e adicionando uma informação adicional sobre a pergunta, mas seja conciso.")
    
    llm = ChatOllama(model="llama3.2:latest")
    
    mensagens = [system_prompt]
    
    mensagem = "None"
    
    while mensagem != "xau":
        usr_msg = HumanMessage(input("\nUsuario: "))
        
        mensagem = usr_msg.content.lower()
        
        mensagens.append(usr_msg)
        
        resposta = llm.invoke(mensagens)
        
        print("\nxandAi: ", resposta.content)
        
        mensagens.append(resposta.content)