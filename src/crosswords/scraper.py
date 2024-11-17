from bs4 import BeautifulSoup
import requests
import re
import time

from crosswords.entry import Entry


max_attempts = 5
timeout = 5
def get_html(url: str):
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Attempt {attempt} of {max_attempts}...")
            response = requests.get(url, timeout=timeout)
            
            # If the request is successful
            if response.status_code == 200:
                print("Connection successful!")
                return response.text
            else:
                print(f"Received unexpected status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")

        # If not the last attempt, wait before retrying
        if attempt < max_attempts:
            wait_time = 2  # seconds
            print(f"Retrying in {wait_time} seconds...\n")
            time.sleep(wait_time)
    raise NetworkError("Failed to connect after multiple attempts.")

def getCluesFromUrl(url: str):

    response = get_html(url)
    soup = BeautifulSoup(response, 'html.parser')


    # Initialize variables
    clues = []
    current_direction = None

    # Process the HTML to extract clues
    for row in soup.select('.entry-content table tr'):
        # Check for direction change (Across/Down)
        header_cell = row.find('td', colspan="2")
        if header_cell:
            current_direction = header_cell.text.strip()
            continue

        # Extract clue number and text
        clue_number_cell, clue_text_cell = row.select('td')

        if not clue_number_cell.text.strip():
            continue

        if clue_number_cell and clue_text_cell:
            clue_number = int(clue_number_cell.text.strip())
            clue_text = clue_text_cell.text.strip()
            is_across = current_direction == "Across"

            # Find the answer
            answer_row = row.find_next_sibling('tr')
            answer_cell = answer_row.find('b') if answer_row else None
            answer = answer_cell.text.strip() if answer_cell else None

            if answer:
                answer = re.sub(r'[^a-zA-Z0-9]', '', answer)

            # Add the clue details to the list
            clues.append(Entry(
                clue_text,
                answer,
                clue_number,
                is_across
            ))

    clues.sort(key=lambda e: e.number)
    return clues


class NetworkError(Exception):
    pass