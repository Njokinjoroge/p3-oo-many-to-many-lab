class Author:
    all = []
    def __init__(self, name):
        self.name = name
        self.all.append(self)
        self.books_list = []
        self.contracts_list = []

    def add_book(self, book):
        self.books_list.append(book)
        book.add_author(self)
        
    def add_contract(self, contract):
        self.contracts_list.append(contract)
        contract.author = self

    def contracts(self):
        return [contract for contract in self.contracts_list]
    
    def books(self):
        return [book for book in self.books_list]
    
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        book.add_contract(contract)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts_list])    

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self.all.append(self)
        self.authors_list = []
        self.contracts_list = []

    def add_author(self, author):
        if not isinstance (author, Author):
            raise Exception('The author must be an instance of the Author class.')
        else:
            self.authors_list.append(author)
        author.books_list.append(self)

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise Exception('The contract must be an instance of the Contract class.')
        else:
            self.contracts_list.append(contract)

    def authors(self):
        return [author for author in self.authors_list]
            
    def contracts(self):
        return [contract for contract in self.contracts_list]

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance (author, Author):
            self.author = author
        else:
            raise Exception('The author must be an instance of the Author class.')    
        if isinstance (book, Book):
            self.book = book
        else:
            raise Exception('The book must be an instance of the Book class.')    
        if isinstance (date, str):
            self.date = date
        else:
            raise Exception('The date must be a string.')    
        if isinstance (royalties, int):
            self.royalties = royalties
        else:
            raise Exception('The royalties must be a integer.')    
        self.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]    