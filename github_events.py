import sys #manipula argumentos da linha de comando
import requests #importa o request para fazer a requisição HTTP

def fetch_github_activity(username): #definindo uma função para a busca da atividade 
    try:
        url = f"https://api.github.com/users/{username}/events" #URL da API do github com o nome de usuario fornecido no comando 
        response = requests.get(url) # GET para buscar os eventos 
        
        
        if response.status_code == 404: #verificação para os erros
            print(f"Erro: Usuario '{username}' não encontrado.")
            return
        
        elif response.status_code != 200:
            print(f"Erro: Falha ao buscar dados (codigo {response.status_code}).")
            return
        
        events = response.json() #converte a resposta da API de json para um dicionario
        
        if not events: #se não tiver atividades, avisa 
            print(f"O usuario '{username}' não tem atividades recentes.")
            return
        
        print(f"Atividades recentes de '{username}':")
        
        for event in events[:10]: #Exibir os 10 eventos mais recentes 
            
            event_type = event.get("type", "Eventos desconhecido")
            repo_name = event.get("repo", {}).get("name", "Repositorio desconhecido")
            print(f"- {event_type.replace('Event', '')} em {repo_name}")
            
    
    except Exception as e: #informa qualquer erro inesperado que possa aparecer
        print(f"Erro: {e}")
        
if __name__ == "__main__":
    if len(sys.argv) != 2: #verifica se o comando tem 2 argumentos 
        print("Uso: python github_events.py <username>") #caso a pessoa mande o comando errado um print para mostrar o jeito certo
    else:
        fetch_github_activity(sys.argv[1])
            