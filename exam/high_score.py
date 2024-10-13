import csv

def high_score(name):
    with open(name, 'r', encoding='utf8') as file:
        readers = csv.DictReader(file)
        max_score = ['', float(0)]
        for read in readers:
            if max_score[1] < float(read['score']):
                max_score = [read['student'], float(read['score'])]
        print(max_score)

high_score('exam_results.csv')

def test_write_to_csv():
    dict_my = ["one", "two"]
    with open("test.csv", 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, dict_my, lineterminator="\n")
        writer.writeheader()
        writer.writerow({'one':1231, "two":"fghfg"})
        writer.writerow({'one': 1231, "two": 4525})
test_write_to_csv()