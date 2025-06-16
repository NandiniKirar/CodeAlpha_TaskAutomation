import requests
from bs4 import BeautifulSoup

def scrape_webpage_title(url, output_file):
    """
    Scrapes the title of a webpage and saves it to a file
    :param url: URL of the webpage to scrape
    :param output_file: Path to output text file
    """
    try:
        # Fetch webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title found"
        
        # Save title to file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(title)
        
        print(f"Title saved to {output_file}: {title}")
    
    except requests.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
url = "https://example.com"
output_path = "webpage_title.txt"
scrape_webpage_title(url, output_path)