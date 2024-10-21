import csv

DATASET_PATH = 'books-en.csv'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    return title


def get_object_alt(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    result = next(reader)
    return result


def filter_author(dataset, author):
    title = get_title(dataset)
    ans = []

    for line in dataset:
        obj = get_object_alt(line, title)
        if obj['Book-Author'] == author and int(obj['Price']) >= 150:
            ans.append(obj['Book-Title'])
    return ans


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        author = input('Введите автора: ')
        found_books = filter_author(dataset, author)

        if found_books:
            print("Список книг данного автора: ")
            for book in found_books:
                print(book)

        else:
            print("Ничего не найдено")