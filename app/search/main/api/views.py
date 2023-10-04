import requests
from bs4 import BeautifulSoup
import os

# List of health-related sentences to search for
health_sentences = [
    "Vitales no disponibles",
    "transferencias de valor",
    # Add your 100 sentences here
]

# Define a directory to store scraped data
output_directory = "result_data"
os.makedirs(output_directory, exist_ok=True)

# Loop through each sentence and perform a web search
for sentence in health_sentences:
    # Create a directory for each sentence's data
    sentence_directory = os.path.join(output_directory, sentence[:30])  # Truncate for directory name
    os.makedirs(sentence_directory, exist_ok=True)

    # Perform a web search using a search engine (e.g., Google)
    search_query = f"{sentence.replace(' ', '+')}"
    print("la direccion de busqueda es: ", search_query)
    search_url = f"https://www.google.com/search?q={search_query}"
    print("search_url", search_url)
    # Send an HTTP GET request to the search engine
    response = requests.get(search_url)
    print("response", response)
    if response.status_code == 200:
        # Parse the search results page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        print("soup ", soup)
        # Extract and print search result URLs
        result_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("www")] # and not a['href'].startswith("https://maps.google.com/") and not a['href'].startswith("https://policies.google.com/") and not a['href'].startswith("https://preferences.google.com/")]
        print("result_links ", result_links)

        print(f"Search results for '{sentence}':")
        for i, link in enumerate(result_links, start=1):
            print(f"{i}. {link}")

            # Scrape information from the web source (you can modify this part)
            source_response = requests.get(link)
            if source_response.status_code == 200:
                # Parse the source page and extract data
                source_soup = BeautifulSoup(source_response.text, 'html.parser')
                # Example: Extract the text content from paragraphs
                paragraphs = source_soup.find_all('p')
                content = '\n'.join(paragraph.text for paragraph in paragraphs)

                # Save the collected data to a file
                output_file = os.path.join(sentence_directory, f"source_{i}.txt")
                with open(output_file, 'w', encoding='utf-8') as file:
                    file.write(content)

            # Limit the number of sources to scrape per sentence
            if i >= 15:  # Adjust the number as needed
                break

    else:
        print(f"Failed to perform a web search for '{sentence}'.")

print("Web data collection completed.")
