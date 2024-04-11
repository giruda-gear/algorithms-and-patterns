from solutions.trade_comic_books_for_novel_books import (
    trade_comic_books_for_novel_books,
)


def test_trade_comic_books_for_novel_books():
    assert trade_comic_books_for_novel_books(0, 1, 2, 3) == 0
    assert trade_comic_books_for_novel_books(4, 8, 4, 3) == 2
    assert trade_comic_books_for_novel_books(393, 896, 787, 920) == 212
    assert trade_comic_books_for_novel_books(3, 6, 4, 5) == 2
