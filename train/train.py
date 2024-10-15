import csv
import json
from collections import defaultdict

# Построение простого классификатора на основе частоты слов
word_category_counts = defaultdict(lambda: defaultdict(int))

with open('train_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row['category']
        words = row['text'].lower().split()
        for word in words:
            word_category_counts[word][category] += 1


def classify_text(text):
    words = text.lower().split()
    category_scores = defaultdict(int)

    for word in words:
        if word in word_category_counts:
            for category, count in word_category_counts[word].items():
                category_scores[category] += count

    if category_scores:
        return max(category_scores, key=category_scores.get)
    else:
        return "unknown"


# Классификация текстов из JSON
with open('test_data.json', 'r') as file:
    test_data = json.load(file)

for entry in test_data:
    entry['predicted_category'] = classify_text(entry['text'])

with open('classified_test_data.json', 'w') as file:
    json.dump(test_data, file, indent=4)