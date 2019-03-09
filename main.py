import hashlib
import json
import urllib.parse


def from_json(file="countries.json"):
    with open(file) as datafile:
        json_data = json.load(datafile)
    countries = []
    for country in json_data:
        countries.append((country['name']['common'], country['name']['official']))
    return countries


def save_to_file(data, file="url_wiki_countries.txt"):
    with open(file, 'w', encoding='utf-8') as datafile:
        datafile.write(f'{data}')


class UrlWiki:
    def __init__(self, countries_names):
        self.prefix_url = 'https://en.wikipedia.org/wiki/'
        self.countries_names = countries_names
        self.index = 0
        self.len = len(countries_names)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.countries_names) - 1:
            raise StopIteration
        self.index += 1
        return str(f"{self.countries_names[self.index][1]} - "
                   f"{self.prefix_url}{urllib.parse.quote(self.countries_names[self.index][0])}")

    def __str__(self):
        countries_urls = []
        for pair in self:
            countries_urls.append(pair)
        return '\n'.join(countries_urls)


if __name__ == '__main__':
    save_to_file(
        UrlWiki(
            from_json()
        )
    )

def hash_lines(filename):
    try:
        with open(filename, 'rb') as datafile:
            m = hashlib.md5()
            line = datafile.readline()
            while line:
                m.update(line)
                line = datafile.readline()
                yield m.hexdigest()
    except FileNotFoundError as text_error:
        print(text_error)


if __name__ == '__main__':
    for number, hash_line in enumerate(hash_lines(input('Введите путь к файлу: ')), 1):
        print(f'{number}: {hash_line}')
