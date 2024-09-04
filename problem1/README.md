# Coderbyte Back-end Challenge
In the Python file, you have a program that performs a GET request on the route https://coderbyte.com/api/challenges/json/date-list and then sort the object keys alphabetically. However, the sorting should be case-insensitive, and the original data structure should be preserved (e.g., lists should remain lists, dictionaries should remain dictionaries). Keep in mind that while the JSON format uses null, in Python, this is represented as None.

Next, remove any duplicate dictionaries from lists. Two dictionaries are considered duplicates if they have the same keys and values in the same order. Only the first occurrence should be preserved when an list contains duplicate dictionaries.

Finally, remove any dictionary properties with all values set to an empty string or None (equivalent to null in JSON), and print a list of modified dictionaries. Be sure to call json.dumps on the final list to convert it back to JSON format, where None in Python will be represented as null.

Example Input:
```bash
[
    {
        "name": "John",
        "age": 30,
        "city": "New York",
        "country": "USA",
        "Hobbies": ["reading", "swimming", "hiking", "swimming"],
        "occupation": "programmer",
        "favorite_foods": {
            "Breakfast": "pancakes",
            "Lunch": "",
            "dinner": "pasta",
            "Snack": "",
        },
        "gear": {"type": "", "material": "", "color": null},
        "affiliations": ["", "", ""],
        "friends": [
            {
                "name": "Jane",
                "age": 28,
                "city": "New York",
                "country": "USA",
                "occupation": null,
            },
            {
                "name": "Tom",
                "age": 32,
                "city": "London",
                "country": "UK",
                "occupation": "teacher",
            },
            {
                "name": "Jane",
                "age": 28,
                "city": "New York",
                "country": "USA",
                "occupation": null,
            },
        ],
    }
]
```


Example Output:
```bash
[
    {
        "age": 30,
        "city": "New York",
        "country": "USA",
        "favorite_foods": {"Breakfast": "pancakes", "dinner": "pasta"},
        "friends": [
            {"age": 28, "city": "New York", "country": "USA", "name": "Jane"},
            {
                "age": 32,
                "city": "London",
                "country": "UK",
                "name": "Tom",
                "occupation": "teacher",
            },
        ],
        "gear": {},
        "Hobbies": ["reading", "swimming", "hiking"],
        "name": "John",
        "occupation": "programmer",
    }
]
```