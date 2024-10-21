import csv
import random

DATASET_PATH = 'books-en.csv'

if __name__ == '__main__':
    with open(DATASET_PATH) as File:
        rd = list(csv.DictReader(File, delimiter=';'))
        result = open('result.txt', 'w')
        for i in range(20):
            num = random.randint(1000, 9000)
            result.write(f"{i + 1} {rd[num]['Book-Author']}. {rd[num]['Book-Title']} - {str(rd[num]['Year-Of-Publication'])} \n")