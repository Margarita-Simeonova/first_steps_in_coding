def vacation_books_list(pages_in_book, pages_per_hour, days):
    # count days func
    
    days_needed = int((pages_in_book / pages_per_hour) / days)

    return days_needed


# input
book_pages = int(input())
pages = int(input())
days = int(input())
result = vacation_books_list(book_pages, pages, days)

print(result)
