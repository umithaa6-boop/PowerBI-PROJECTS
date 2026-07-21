import requests
import re

def get_page_title(url):
    """
    Fetch the webpage and extract its title using regex.
    Returns the title string, or None if not found.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for bad status codes

        # Search for <title>...</title> (case-insensitive)
        match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            return title
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def save_title_to_file(title, filename="page_title.txt"):
    """Write the title to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        if title:
            f.write(f"Page Title: {title}\n")
        else:
            f.write("No title found or page could not be loaded.\n")
    print(f"Title saved to {filename}")

if __name__ == "__main__":
    URL = "https://codealpna.tech"   # Use https
    print(f"Scraping title from {URL} ...")
    title = get_page_title(URL)
    save_title_to_file(title)
