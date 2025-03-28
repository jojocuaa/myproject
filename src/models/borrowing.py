class Borrowing:
    def __init__(self, id, book_id, member_id, borrow_date, return_date, status):
        self.id = id
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.status = status