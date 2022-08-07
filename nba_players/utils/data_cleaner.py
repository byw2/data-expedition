#-----------------------------------------------------------------------
# data_cleaner.py
# Author: Brendan Wang
#-----------------------------------------------------------------------

import unidecode
from scraper import load_dict, dump_dict

#-----------------------------------------------------------------------

def remove_accents(mapping: dict) -> dict:
    """Remove accents from all the keys of mapping. The mapping
    is a dictionary where key:value is of the format name:position."""
    new_names = [unidecode.unidecode(name) for name in mapping.keys()]
    return dict(zip(new_names, mapping.values()))

#-----------------------------------------------------------------------

def clean_names(names_to_positions: dict, name_mapping: dict) -> dict:
    """Replace names with those found in names_to_positions."""
    new_names = [name_mapping.get(name, name) 
                for name in names_to_positions.keys()]
    return dict(zip(new_names, names_to_positions.values()))

#-----------------------------------------------------------------------

def add_alternative_names(names_to_positions: dict) -> dict:
    """Some players have more than one name in the data frame."""
    return {**names_to_positions,
            'Marcus Morris': names_to_positions.get('Marcus Morris Sr.'),
            'Charles Jones': names_to_positions.get('Charles R. Jones'),
            'Danuel House Jr.': names_to_positions.get('Danuel House'),
            'T.J. Warren': names_to_positions.get('TJ Warren'),
            'P.J. Tucker': names_to_positions.get('PJ Tucker'),
            'T.J. Leaf': names_to_positions.get('TJ Leaf'),
            'Norman Richardson': names_to_positions.get('Norm Richardson'),
    }
#-----------------------------------------------------------------------

def main():
    # names_to_dict = load_dict('../files/names_to_positions.txt')
    # new_mapping = remove_accents(names_to_dict)
    # dump_dict('../files/names_to_positions.txt', new_mapping)

    # names_to_position = load_dict('../files/names_to_positions.txt')
    # name_mapping = load_dict('../files/name_mapping.txt')
    # new_mapping = clean_names(names_to_position, name_mapping)
    # new_mapping = add_alternative_names(new_mapping)
    # dump_dict('../files/names_to_positions.txt', new_mapping)
    pass

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()