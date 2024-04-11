"""
    trade:  n * novel_boooks = n * (comic_books + coins_needed)
    sell:   1 comic_books = 1 coins_offered
"""


def trade_comic_books_for_novel_books(
    comic_books, coins, coins_needed, coins_offered
) -> int:
    # needed_coins = coins_needed * comic_books
    # if coins >= needed_coins:
    #     return comic_books

    while comic_books > 0:
        needed_coins = coins_needed * comic_books

        if coins >= needed_coins:
            return comic_books
        else:
            comic_books -= 1
            coins += coins_offered

    return comic_books
