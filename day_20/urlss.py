import requests
from collections import Counter
# noinspection PyUnresolvedReferences
from pprint import pprint
import numpy
# noinspection PyUnresolvedReferences
from bs4 import BeautifulSoup

response = requests.get('https://www.gutenberg.org/files/1112/1112.txt')


def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    # Cnter.sort(reverse=True)
    return Cnter[:10]


# print(most_common_words(response.text))

cat_pi = requests.get('https://api.thecatapi.com/v1/breeds')
data = cat_pi.json()


def metric_weights(data):
    metric_weights = []

    for breed in data:
        metric_weights.append(
            (int(breed['weight']['metric'].split()[0]) + int(breed['weight']['metric'].split()[-1])) / 2)

    median = numpy.median(metric_weights)
    mean = numpy.mean(metric_weights)
    min_metric = min(metric_weights)
    max_metric = max(metric_weights)
    sd = numpy.std(metric_weights)
    print("WEIGHT DATA")
    print("Standard Deviation: %0.2f" % sd)
    print("Minimum:", min_metric)
    print("Maximum:", max_metric)
    print("Median:", median)
    print("Mean: %0.2f" % mean)


def life_spans(data):
    lifespans = []
    for breed in data:
        lifespans.append((int(breed['life_span'].split()[0]) + int(breed['life_span'].split()[-1])) / 2)

    median = numpy.median(lifespans)
    mean = numpy.mean(lifespans)
    min_span = min(lifespans)
    max_span = max(lifespans)
    sd = numpy.std(lifespans)
    print("LIFESPAN DATA")
    print("Standard Deviation: %0.2f" % sd)
    print("Minimum:", min_span)
    print("Maximum:", max_span)
    print("Median:", median)
    print("Mean: %0.2f" % mean)


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def freq_origin(data):
    origins = []
    for breed in data:
        origins.append(breed['origin'])
    print(sort_dict_by_value(dict(Counter(origins)), True))


'''
r = requests.get('https://archive.ics.uci.edu/ml/datasets.php')

soup = BeautifulSoup(r.content, features='lxml')
print(soup.prettify())
'''