class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    def get_email(self):
        print(self.email)
        return self.email
    def change_email(self, address):
        self.address = address
        print("Update email to {}".format(self.address))
    def __repr__(self):
        books_read = list(self.books.keys())
        num_books_read = len(list(self.books.keys()))
        for a in books_read:
            num_books_read += 1
        return "{name} using email : {email} has read {read} books".format(name=self.name, email = self.email, read = num_books_read)
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
    def read_book(self, book, rating=None):
        self.books[book] = rating
    def get_average_rating(self):
        count = 0
        avg_rate = 0
        for a in self.books:
            count += 1
            avg_rate += self.books.get(a)
        return avg_rate/count
            
                    
                
        

#Rikki = User("Rikki G S", "VikasS0618@gmail.com")
#print(Rikki)
#Rikki.change_email("Seema_rb@hotmail.com")
#RikkiGS = User("Rikki G S", "VikasS0618@gmail.com")
#print(RikkiGS)
#print(Rikki == RikkiGS)
#Rikki.read_book("Harry Potter", 3.5)
#Rikki.read_book("Bourne Supremacy", 2.5)
#print(Rikki.average_rating())
#Seema_RB = User("Seema", "Seema_rb@hotmail.com")
#print(Seema_RB)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    def __repr__(self):
        return "{title}  {isbn}".format(title=self.title, isbn=self.isbn)
    def get_title(self):
        print(self.title)
        return self.title
    def get_isbn(self):
        print(self.isbn)
        return self.isbn
    def set_isbn(self, new_isbn):
        if type(new_isbn) == int:
            self.isbn = new_isbn
            print("ISBN updated to {}".format(self.isbn))
        else:
            print("ISBN can only be whole numbers(integers). Please re-enter ISBN")
    def add_rating(self, rating):
        if rating >=0 and rating <=4:
            self.ratings.append(rating)
        else:
            print("Rating must be a number between 0 and 4. Invalid rating.")
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
    def get_average_rating(self):
        count = 0
        avg_rate = 0
        for a in self.ratings:
            count += 1
            avg_rate += self.ratings[a]
        return avg_rate/count
    def __hash__(self):
        return hash(self.title, self.isbn)

#Rikki.read_book("Harry Potter", 3.5)
#Rikki.read_book("Bourne Supremacy", 2.5)
#RikkiGS.read_book("Harry Potter", 1.5)
#print(Rikki.get_average_rating())
#harry_potter = Book("Harry Potter", 1010)
#print(harry_potter.get_average_rating())
#print(harry_potter.title)    
            
#tale_o_2_cities = Book("A Tale of Two Cities", 9119)            
#tale_o_2_cities.get_title()
#tale_o_2_cities.get_isbn()
#tale_o_2_cities.set_isbn(1991)
#tale_o_2_cities.set_isbn("1991")
#tale_o_2_cities.add_rating(3)
#tale_o_2_cities.add_rating(5)
#tale_o_2_cities.get_isbn()
#Rikki.books["Moby Dick"] = 29
class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        print(self.author)
        return self.author
    def __repr__(self):
        return "{title} has been written by {author}".format(title=self.title, author=self.author)
#Moby_dick = Fiction("Moby Dick", 8282, "I forgot")
#print(Moby_dick)    
class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject(self):
        print(self.subject)
        return self.subject
    def get_level(self):
        print(self.level)
        return self.level
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level= self.level, subject=self.subject)
#Htmmis = Non_Fiction("How to make money in stocks", 2020, "Stock Market", "Comprehensive")
#print(Htmmis)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
# will do later when I figure out how to map object to attribute        
    def create_book(title, isbn):
        title = Book(title, isbn)
        print(title)
        return title
    def create_novel(title, isbn, author):
        title = Fiction(title, isbn, author)
        print(title)
        return title
    def create_non_fiction(title, isbn, subject, level):
        title = Non_Fiction(title, isbn, subject, level)
        print(title)
        return title
    def add_book_to_user(self,book, email, rating=None):
        if email in self.users.keys():
            user = self.users.key(email)
            user.read_book(self.users[email], rating)
            user.add_rating(book, rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return "No user with email {email}".format(email=email)
    def add_user(self, name, email, books=None):
        user = User(name, email, books)
        self.users[email] = user
        if books != None:
            for b in books:
                user.add_book_to_user(b,email)
    def print_catalog():
        for b in TomeRater.books:
            print(b, b.title)
            print(b.title)
    def print_users():
        for u in TomeRater.users:
            print(TomeRater.users[u])
    def most_read_book():
        for book, read in list(TomeRater.books.items()):
            if read == max(list(TomeRater.books.items())):
                return "{title} is currently the most read book on TomeRater.".format(title=book.title), book.title
    def highest_rated_book():
        book_ratings = {}
        for b in TomeRater.books:
            temp = b.get_average_rating()
            book_ratings[b] = temp
        for bk, rtg in list(book_ratings.items()):
            if rtg == max(list(book_ratings.items())):
                return "{title} is currently the highest rated book on TomeRater".format(title=bk.title), bk.title
    def most_positive_user():
        user_avg_rating = {}
        for user in TomeRater.users:
            temp_rating = user.get_average_rating()
            user_avg_rating[user] = temp_rating
        for usr, ratng in list(user_avg_rating.items()):
            if ratng == max(list(user_avg_rating.items())):
                return "{pos_user} has given books the highest average rating so far on TomeRater".format(pos_user=user.name), user.name
            
        
        
            
        
            
             
        

#TomeRater.create_book("Moby_Dick", 3030)
#TomeRater.create_novel("Ramayana", 2929, "Valmiki")
#TomeRater.create_non_fiction("Kill or get Killed", 7676, "Hand to hand combat", "Serious")
    

        