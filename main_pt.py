import requests
from bs4 import BeautifulSoup
import logging

# Configurando o sistema de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Solicitar entrada do usuário
user_input = input("Digite o usuário: ")

# URL do perfil
url = f"https://twstalker.com/{user_input}"

# Adicionando um cabeçalho de usuário simulado
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Enviar uma solicitação GET para o site
response = requests.get(url, headers=headers)

# Verificar se a solicitação foi bem-sucedida (código 200)
if response.status_code == 200:
    # Parsear o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Verificar se a conta não existe
    error_message = soup.find("span", style="font-size: 18px;font-weight: 400;color: #847577;margin-bottom: 30px;line-height: 24px;display: block;")
    if error_message:
        print("A conta não existe. Tente procurar por outra.")
    else:
        # Extrair informações específicas
        name = soup.find("h3").text.strip() if soup.find("h3") else "N/A"  # Nome
        username = soup.find("h3").span.text.strip() if soup.find("h3") and soup.find("h3").span else "N/A"  # Nome de usuário

        # Remover o "@" e qualquer texto após ele no nome de usuário
        name = name.split('@')[0]
      
        joined_date = soup.find("div", class_="my-dash-dt").find_all("span")[-1].text.strip() if soup.find("div", class_="my-dash-dt") else "N/A"  # Bio do perfil
        tweet_count = soup.find("div", class_="dscun-numbr").text.strip() if soup.find("div", class_="dscun-numbr") else "N/A"  # Número de tweets
        followers_count = soup.find_all("div", class_="dscun-numbr")[1].text.strip() if len(soup.find_all("div", class_="dscun-numbr")) > 1 else "N/A"  # Número de seguidores
        following_count = soup.find_all("div", class_="dscun-numbr")[2].text.strip() if len(soup.find_all("div", class_="dscun-numbr")) > 2 else "N/A"  # Número de seguidos
        likes_count = soup.find_all("div", class_="dscun-numbr")[3].text.strip() if len(soup.find_all("div", class_="dscun-numbr")) > 3 else "N/A"  # Número de curtidas

        # Exibir as informações sem as mensagens de log
        print(f"Nome: {name}")
        print(f"Nome de usuário: {username}")
        print(f"Data de entrada: {joined_date}")
        print(f"Número de tweets: {tweet_count}")
        print(f"Número de seguidores: {followers_count}")
        print(f"Número de seguidos: {following_count}")
        print(f"Número de curtidas: {likes_count}")

else:
    logger.error(f"Erro ao acessar a página. Código de status: {response.status_code}")
