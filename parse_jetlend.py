import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> str:
    """Получает html-код главной страницы jetlend.ru."""
    result = requests.get(url)
    return result.text


def quantity_tags(html_page: str) -> tuple[int, int]:
    """Считает сколько всего тегов и тегов без атрубутов."""
    soup = BeautifulSoup(html_page, 'html.parser')
    tags = soup.find_all(True)
    counter = 0
    for tag in tags:
        if not tag.attrs:
            counter += 1
    return len(tags), counter


if __name__ == '__main__':
    html = get_html('https://jetlend.ru/borrower/')
    amount_tags, amount_tags_without_attr = quantity_tags(html)
    print(f'Общее число тегов на главной странице jetlend.ru - {amount_tags}')
    print(f'Чиcло тегов без атрибутов {amount_tags_without_attr}')    