import csv

DATASET_PATH = "books-en.csv"

def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(";")
    title = [col.strip() for col in title]
    return title

def get_object_alt(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    result = next(reader)
    return result


def filter_len(dataset, title, mn):
    cnt = 0
    for line in dataset:
        obj = get_object_alt(line, title)
        book_title = obj.get('Book-Title')
        if len(book_title) > mn:
            cnt += 1
    return cnt

if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)
        result = filter_len(dataset, title, 30)
        print(result)