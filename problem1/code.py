import json

import requests


def sort_dict_keys(list_of_dicts):
    """
    Returns a new list of dicts with keys sorted in alphabetical order case-insensitive
    """
    if isinstance(list_of_dicts, dict):
        # if we find a dict then let's order its keys
        return {
            k: sort_dict_keys(v)
            for k, v in sorted(list_of_dicts.items(), key=lambda item: item[0].lower())
        }

    elif isinstance(list_of_dicts, list):
        # if we find a list let's call recursively this function for each item
        return [sort_dict_keys(item) for item in list_of_dicts]

    return list_of_dicts


def remove_duplicates(list_of_dicts):
    """
    Return a new list of dicts without duplicated dictionaries within the same list
    """
    if isinstance(list_of_dicts, list):
        new_list = []
        seen = []

        for item in list_of_dicts:
            if isinstance(item, dict):
                if item not in seen:  # if not seen then we save it
                    seen.append(item)
                    new_list.append(remove_duplicates(item))
            else:
                # if again we find a list let's call recursively this function for each item
                if item not in new_list:
                    new_list.append(remove_duplicates(item))

        return new_list

    elif isinstance(list_of_dicts, dict):
        # if we find a list let's call recursively this function for each item
        return {k: remove_duplicates(v) for k, v in list_of_dicts.items()}

    return list_of_dicts


def clean(list_of_dicts):
    """
    Return a new list of dicts without [], {}, "" and None values
    """
    if isinstance(list_of_dicts, list):
        # if we find a dict then let's remove [], {}, "" and None values
        cleaned_list = [clean(item) for item in list_of_dicts]
        return [item for item in cleaned_list if item not in ([], {}, "", None)]

    elif isinstance(list_of_dicts, dict):
        # if we find a list let's call recursively this function for each item except for values [], "" and None
        return {
            k: v
            for k, v in ((k, clean(v)) for k, v in list_of_dicts.items())
            if v not in ([], "", None)
        }

    return list_of_dicts


response = requests.get("https://coderbyte.com/api/challenges/json/wizard-list")
data = json.loads(response.content)
print(clean(remove_duplicates(sort_dict_keys(data))))
