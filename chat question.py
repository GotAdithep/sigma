class Movie:
    def __init__(self,title = "unknown",director = "unknown",rental_price = 100.00):
        self.__title = title
        self.__director = director
        self.__rental_price = rental_price

    def get_director(self):
        return self.director
    def set_director(self,director):
        self.__director = director

    def get_title(self):
        return self.title
    def set_title(self,title):
        self.__title = title

    def get_rental_price(self):
        return self.rental_price
    def set_rental_price(self, price):
        self.__rental_price = price

    def display_movie_info(self):
        print(f"title: {self.__title} director: {self.__director} rental_price: {self.__rental_price}")

class DVD(Movie):
    def __init__(self,title = "unknown",director = "unknown",rental_price = 100.00,is_scratched = True):
        super().__init__(title,director,rental_price)
        self.__is_scratched = is_scratched

    def check_condition(self):
        if self.__is_scratched == True:
            print(f"Scratched")
        else:
            print(f"Good condition")

    def display_movie_info(self):
        what to do?