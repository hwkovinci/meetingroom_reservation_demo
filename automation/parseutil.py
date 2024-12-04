import json
import re
import os
from dotenv import load_dotenv
from typing import Dict, List, Tuple
load_dotenv()

def load_config(file_path: str) -> List[dict]:
    with open(file_path, 'r') as file:
        return json.load(file)

def replace_with_index(str_target: str, pattern: str, replace_list : List[str] ) -> str:
    # Find all matches of the pattern
    match_col = re.findall(pattern, str_target)

    # Replace each match with its index
    for i, match in enumerate(match_col):
        str_target = str_target.replace(match, f"{{{i}}}")
      
    str_target = str_target.format( *replace_list )
    return str_target


def apply_userinput(actions: List[Dict[str, any]], 
                    user_input: Dict[int, Tuple[Dict[str, any], Dict[str, any]]]) -> List[Dict[str, any]]:
    """
    Modifies the 'actions' list of dictionaries based on the 'user_input' mappings.

    Args:
    - actions: List of action dictionaries where each dictionary represents an action.
    - user_input: A dictionary mapping indices of 'actions' to a tuple of two dictionaries.
                  The first dictionary in the tuple maps a target key to a value to be updated,
                  and the second dictionary optionally defines changes to a 'subaction' key within an action.

    Returns:
    - List[Dict[str, any]]: The modified list of actions with updates applied based on user input.
    """
    for index, updates in user_input.items():
        action = actions[index]
        # Update the main action
        if len(updates[0]) > 0:
            action_target : str, action_value : List[str] = updates[0].get('target'), updates[0].get('value')
            if action_target and action_value:
                action[action_target] = replace_with_index( action[action_target] , os.getenv( 'REPLACE_PATTERN' ), *action_value )
        # Update the subaction, if any
        if len(updates[1]) > 0:
            subaction_target : str, subaction_value : List[str] = updates[1].get('target'), updates[1].get('value')
            if subaction_target and subaction_value:
                current_str = action.setdefault('subaction', {})[subaction_target]
                action.setdefault('subaction', {})[subaction_target] = replace_with_index( current_str, os.getenv( 'REPLACE_PATTERN' ), *subaction_value)
  

    return actions
