from app.book import Book
from app.serializer import JsonSerializer, XmlSerializer
from app.printer import ConsolePrint, ReversePrint
from app.display import ConsoleDisplay, ReverseDisplay


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book.content)
            elif method_type == "reverse":
                ReverseDisplay().display(book.content)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                ConsolePrint().print_book(book.title, book.content)
            elif method_type == "reverse":
                ReversePrint().print_book(book.title, book.content)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer().serialize(book.title, book.content)
            elif method_type == "xml":
                return XmlSerializer().serialize(book.title, book.content)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
