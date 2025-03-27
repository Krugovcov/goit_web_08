import json
from mongoengine.errors import NotUniqueError
from typing import List, Any



import common.connect as connect
from hw8.hw_first_part.models_quote import Author, Quote

if __name__ == '__main__':
    with open("authors.json", "r", encoding="utf-8") as file:
        authors_data = json.load(file)

    for el in authors_data:
        try:
            author = Author(
                fullname=el.get("fullname", "Невідомий автор"),
                born_date=el.get("born_date", "Дата невідома"),
                born_location=el.get("born_location", "Місце народження невідоме"),
                description=el.get("description", "Опис відсутній")
            )

            author.save()
        except NotUniqueError:
            print(f"Автор вже існує {el.get('fullname')}")

    with open("quotes.json", "r", encoding="utf-8") as file:
        quotes_data = json.load(file)

    for el in quotes_data:
        author = Author.objects(fullname=el.get("author", "Невідомий автор")).first()

        if author:
            quote = Quote(
                tags=el.get("tags", []),
                author=author,
                quote=el.get("quote", "Цитата відсутня")
            )
            quote.save()
