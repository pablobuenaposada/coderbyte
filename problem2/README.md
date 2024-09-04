# Coderbyte Back-end Challenge

You're part of the data analytics team for a new app company. User feedback is essential for your company's success, and your task is to analyze user reviews to find trends and areas for improvement.

Each user review is represented as a dictionary with keys: id (unique identifier), rating (integer from 1 to 5), review (string), and date (string in the format "YYYY-MM-DD").

Given a list of these reviews, your task is to:

1. Calculate the average rating.

2. Identify the most common words in the reviews. Exclude any punctuation from the reviews when identifying common words, and transform all words to lowercase for consistency.

3. Find the month with the most reviews submitted.

The current implementation has errors and inefficiencies. Correct the code to perform the tasks accurately.

Note: For this challenge, consider words to be any sequence of characters separated by spaces. You can assume all words in reviews are in lowercase.

Example Input:

[
{"id": 1, "rating": 5, "review": "Great app. Love the features. The design is outstanding.", "date": "2023-01-15"},
{"id": 2, "rating": 4, "review": "Very useful. It's become a daily tool for me.", "date": "2023-01-17"},
{"id": 3, "rating": 3, "review": "Decent, but some features don't work well.", "date": "2023-02-05"},
{"id": 4, "rating": 2, "review": "I experienced some bugs. Needs fixing.", "date": "2023-02-11"},
{"id": 5, "rating": 5, "review": "Outstanding! Everything I wanted in an app.", "date": "2023-02-14"},
{"id": 6, "rating": 4, "review": "Good app overall, just some minor issues.", "date": "2023-02-20"},
{"id": 7, "rating": 3, "review": "Average, but the user experience could be better.", "date": "2023-03-05"}
]

Example Output:

Average Rating: 3.7
Most Common Words: ['app']
Month with Most Reviews: February