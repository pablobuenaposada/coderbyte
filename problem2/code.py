import calendar
import string
from collections import Counter
from datetime import datetime


def analyze_reviews(reviews):
    total_rating = 0
    word_count = Counter()
    monthly_reviews = Counter()
    STOPWORDS = {"the", "and", "a", "to", "of", "in", "but", "some", "is", "it", "i", "for", "on", "with", "was"}

    for review in reviews:
        total_rating += review["rating"]
        month = datetime.strptime(review["date"], "%Y-%m-%d").month
        monthly_reviews[month] += 1

        for word in review["review"].strip(string.punctuation).lower().split():
            if word not in STOPWORDS:
                word_count[word] += 1

    most_common_words = sorted([word for word, count in word_count.items() if count == max(word_count.values())])

    print(f"Average Rating: {round(total_rating / len(reviews), 1)}")
    print(f"Most Common Words: {most_common_words}")
    print(f"Month with Most Reviews: {calendar.month_name[max(monthly_reviews, key=monthly_reviews.get)]}")


# test the function below
reviews = [
    {"id": 1, "rating": 5, "review": "The coffee was fantastic.", "date": "2022-05-01"},
    {"id": 2, "rating": 4, "review": "Excellent atmosphere. Love the modern design!", "date": "2022-05-15"},
    {"id": 3, "rating": 3, "review": "The menu was limited.", "date": "2022-05-20"},
    {"id": 4, "rating": 4, "review": "Highly recommend the caramel latte.", "date": "2022-05-22"},
    {"id": 5, "rating": 4, "review": "The seating outside is a nice touch.", "date": "2022-06-01"},
    {"id": 6, "rating": 5, "review": "It's my go-to coffee place!", "date": "2022-06-07"},
    {"id": 7, "rating": 3, "review": "I found the Wi-Fi to be quite slow.", "date": "2022-06-10"},
    {"id": 8, "rating": 3, "review": "Menu could use more vegan options.", "date": "2022-06-15"},
    {"id": 9, "rating": 4, "review": "Service was slow but the coffee was worth the wait.", "date": "2022-06-20"},
    {"id": 10, "rating": 5, "review": "Their pastries are the best.", "date": "2022-06-28"},
    {"id": 11, "rating": 2, "review": "Very noisy during the weekends.", "date": "2022-07-05"},
    {"id": 12, "rating": 5, "review": "Baristas are friendly and skilled.", "date": "2022-07-12"},
    {"id": 13, "rating": 3, "review": "It's a bit pricier than other places in the area.", "date": "2022-07-18"},
    {"id": 14, "rating": 4, "review": "Love their rewards program.", "date": "2022-07-25"},
]

analyze_reviews(reviews)
