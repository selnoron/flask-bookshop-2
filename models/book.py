class CompareBooks():
    """Compare books"""

    def compare(book1: dict, book2: dict) -> bool:
        if book1 == book2:
            return True
        else:
            return False


class Book:
    """Модель книги для нашего проекта."""

    def __init__(
        self,
        title: str,
        description: str,
        list_count: int,
        price: float,
        rate_list: list[int],
        compar: CompareBooks
    ) -> None:
        self.title = title
        self.description = description
        self.list_count = list_count
        self.price = price 
        self.rate_list = rate_list
        self.compar = compar

    @property
    def rate(self) -> float:
        return sum(self.rate_list) / len(self.rate_list)
    
    def save(self) -> None:
        pass

    def delete(self) -> None:
        pass

    def update() -> None:
        pass
