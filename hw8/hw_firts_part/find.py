import redis
from redis_lru import RedisLRU
import connect
from models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> list[str | None]:
    print(f"Find by {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


def find_by_name(name):
    print(f"Find by {name}")
    author = Author.objects(name=name).first()
    return author.quotes if author else "none found"


def parser():
    while True:
        user_input = input("Input command: ")
        command, *args = user_input.split(":")
        if command == 'tag':
            return find_by_tag(' '.join(args).strip())
        elif command == 'name':
            return find_by_name(' '.join(args).strip())
        elif command == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid command")

if __name__ == '__main__':
    while True:
        result = parser()
        if result:
            print(result)