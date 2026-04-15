from pathlib import Path
import json


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
    with open(file_path, mode= 'r') as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    else:
        return None

def linear_search(searched_data, searched_number):
    count = 0
    index = 0
    position = []
    searched_dictionary = {}
    while index < len(searched_data):
        if searched_data[index] == searched_number:
            count += 1
            position.append(index)
        index+=1
    searched_dictionary['position'] = position
    searched_dictionary['count'] = count
    return searched_dictionary

def binary_search(searched_data, searched_number):
    left = 0
    right = len(searched_data) -1
    while left <= right:
        middle = (left + right)//2
        if searched_data[middle] == searched_number:
            return middle
        elif searched_data[middle] < searched_number:
            left = middle + 1
        elif searched_data[middle] > searched_number:
            right = middle + 1
    return None



def main():
    my_data = read_data("sequential.json",  "unordered_numbers" )
    print(my_data)
    my_data2 = read_data("sequential.json", "ordered_numbers")
    print(my_data2)
    n = 21
    ls = linear_search(my_data, n)
    print(ls)
    bn = binary_search(my_data2, n)
    print(bn)

if __name__ == "__main__":
    main()
