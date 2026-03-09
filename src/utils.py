def format_name(first: str, last: str) -> str:
    return f"{first.strip()} {last.strip()}"

def calculate_discount(price: float, percent: float) -> float:
    return round(price * (1 - percent / 100), 2)

def paginate(items: list, page: int, page_size: int = 10) -> list:
    start = (page - 1) * page_size
    return items[start:start + page_size]
