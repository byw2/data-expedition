#-----------------------------------------------------------------------
# scrape.py
# Author: Brendan Wang
#-----------------------------------------------------------------------

import requests 
from bs4 import BeautifulSoup as bs
import json

#-----------------------------------------------------------------------

def get_player_names(soup):
    """Returns a list of a players names from soup."""
    player_names = []
    player_cells = soup.find_all('th', attrs={'data-stat': 'player'})
    # ignore the top cell
    for j in range(1, len(player_cells)):
        player_names.append(player_cells[j].find('a').text)
    return player_names

#-----------------------------------------------------------------------

def get_player_positions(soup):
    """Returns a list of a players position from soup."""
    player_positions = []
    position_cells = soup.find_all('td', attrs={'data-stat': 'pos'})
    for j in range(len(position_cells)):
        player_positions.append(position_cells[j].text)
    return player_positions

#-----------------------------------------------------------------------

def get_name_to_pos(names, positions):
    """Zips together a dictionary with names as keys and positions as 
    values."""
    return dict(zip(names, positions))

#-----------------------------------------------------------------------

def scraper(base_url, alphabet):
    """Generates a name to position dictionary for all NBA players."""
    all_name_to_pos = dict()
    for letter in alphabet:
        url = f'{base_url}/{letter}/' 
        # send get request
        response = requests.get(url)
        # create the soup which uses HTML parser to parse content in bytes
        soup = bs(response.content, features='html.parser')
        # get player names and positions
        names = get_player_names(soup)
        positions = get_player_positions(soup)
        name_to_pos = get_name_to_pos(names, positions)
        # get dictionary
        all_name_to_pos = {**all_name_to_pos, **name_to_pos}
    return all_name_to_pos

#-----------------------------------------------------------------------

def dump_dict(fn, dictionary):
    """Dumps dictionary to a file with name fn."""
    with open(fn, 'w') as file:
        file.write(json.dumps(dictionary))

#-----------------------------------------------------------------------

def load_dict(fn):
    """Loads dictionary from a file with name fn."""
    with open(fn, 'r') as file:
        res = json.load(file)
    return res

#-----------------------------------------------------------------------

def main():
    # defines base url
    base_url = "https://www.basketball-reference.com/players"

    # alphabet list over which to loop for requests 
    # note that 'X' is omitted since no last names start with X
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w', 'y', 
                'z']

    fn = "names_to_positions.txt"

    all_name_to_pos = scraper(base_url, alphabet)

    # dump_dict(fn, all_name_to_pos)
    # all_name_to_pos = load_dict(fn)

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
