import json
from pathlib import Path
import sys
from pprint import pprint as pp

# This makes the directory that the module is loaded from as "source path"
source_path = Path(__file__).resolve()
source_dir = source_path.parent


# Called in main.py
# example: get_tarot_names('tarot-images.json')

def get_tarot_names(json_file_path):
    # opening json file
    tarot_json = open(json_file_path)
    # return a JSON object as a dictionary
    tarot_cards_file = json.load(tarot_json)

    # list containing dictionaries
    all_cards_info = []
    card_names = []

    for all_card_info in tarot_cards_file['cards']:
        all_cards_info.append(all_card_info)

    for all_card_info in all_cards_info:
        card_names.append(all_card_info['name'])
    tarot_json.close()
    return card_names


tarot_names_list = get_tarot_names(f'{source_dir}/../data/tarot-cards.json')


def get_tarot_names_list():
    return tarot_names_list