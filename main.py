import requests
from bs4 import BeautifulSoup
import logging

# Setting up the logging system
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User input prompt
user_input = input("Enter the username: ")

# Profile URL
url = f"https://twstalker.com/{user_input}"

# Adding a simulated user header
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Sending a GET request to the site
response = requests.get(url, headers=headers)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the HTML of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Checking if the account does not exist
    error_message = soup.find("span", style="font-size: 18px;font-weight: 400;color: #847577;margin-bottom: 30px;line-height: 24px;display: block;")
    if error_message:
        print("The account does not exist. Try searching for another one.")
    else:
        # Extracting specific information
        name = soup.find("h3").text.strip() if soup.find("h3") else "N/A"  # Name
        username = soup.find("h3").span.text.strip() if soup.find("h3") and soup.find("h3").span else "N/A"  # Username

        # Removing "@" and any text after it in the username
        name = name.split('@')[0]
      
        joined_date = soup.find("div", class_="my-dash-dt").find_all("span")[-1].text.strip() if soup.find("div", class_="my-dash-dt") else "N/A"  # Join date
        tweet_count = soup.find("div", class_="dscun-numbr").text.strip() if soup.find("div", class_="dscun-numbr") else "N/A"  # Number of tweets
        followers_count = soup.find_all("div", class_="dscun-numbr")[1].text.strip() if len(soup.find_all("div", class_="dscun-numbr")) > 1 else "N/A"  # Number of followers
        following_count = soup.find_all("div", class_="dscun-numbr")[2].text.strip() if len(soup.find_all("div", class_="dscun-numbr")) > 2 else "N/A"  # Number following
        likes_count = soup.find_all("div", class_="dscun-numbr")[3].text.strip() if len(soup.find_all("div", class_="dscun-numbr")) > 3 else "N/A"  # Number of likes

        # Displaying the information without log messages
        print(f"Name: {name}")
        print(f"Username: {username}")
        print(f"Join date: {joined_date}")
        print(f"Number of tweets: {tweet_count}")
        print(f"Number of followers: {followers_count}")
        print(f"Number following: {following_count}")
        print(f"Number of likes: {likes_count}")

else:
    logger.error(f"Error accessing the page. Status code: {response.status_code}")
