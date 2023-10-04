from googlesearch import search
import requests
from bs4 import BeautifulSoup
import os

google_query = "vitales no disponibles"
# Define a directory to store scraped data
output_directory = "result_data"
os.makedirs(output_directory, exist_ok=True)


# Create a directory for each sentence's data
sentence_directory = os.path.join(output_directory, google_query[:30])  # Truncate for directory name
os.makedirs(sentence_directory, exist_ok=True)
j=0
for i in search(google_query, start=0, pause=2):
    print(i)
    # Scrape information from the web source (you can modify this part)
    source_response = requests.get(i)
    if source_response.status_code == 200:
        # Parse the source page and extract data
        source_soup = BeautifulSoup(source_response.text, 'html.parser')
        # Example: Extract the text content from paragraphs
        paragraphs = source_soup.find_all('p')
        content = '\n'.join(paragraph.text for paragraph in paragraphs)

        # Save the collected data to a file
        output_file = os.path.join(sentence_directory, f"source_{j}.txt")
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)

    # Limit the number of sources to scrape per sentence
    if j >= 15:  # Adjust the number as needed
        break
    j+=1