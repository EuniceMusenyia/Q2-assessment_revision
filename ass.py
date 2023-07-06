# class Book :
#     def __init__(self, title, author, copies ):
#         self.title = title
#         self.author = author
#         self.copies = copies
    
#     def __str__(self):
#         return f"Title: {self.title}"
    

# class Books_Catalog:
#     def __init__(self):
#         self.books = []


        

#     def add_boks(self,title, author, copies ):
#         new_book = Book("river", "source", 2)
#         self.books.append(new_book)

#     def search(self, title):
#         avail = []
#         for book in self.books:
#             if book.title == title:
#                 avail.append
#         return avail
    
#     def copies(self, title, num):
#         for book in self.books:
#             if book.title == title:
#                 book.copies+= num
#                 break


# catalog = Books_Catalog()
# catalog.add_boks("river", "source", 1)  
# catalog.copies("river", 5)

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nAvailable Copies: {self.copies}"

class BooksCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        new_book = Book(title, author, copies)
        self.books.append(new_book)

    def search(self, title):
        avail = []
        for book in self.books:
            if book.title == title:
                avail.append(book)
        return avail
    
    def update_copies(self, title, num):
        for book in self.books:
            if book.title == title:
                book.copies += num
               
    def get_available_copies(self, title):
        for book in self.books:
            if book.title == title:
                return book.copies
        return 0

catalog = BooksCatalog()
catalog.add_book("River", "Source", 1)
catalog.update_copies("River", 5)
available_copies = catalog.get_available_copies("River")
print(f"Available copies of 'River': {available_copies}")

searched_books = catalog.search("River")
for book in searched_books:
    print(book)



#  class FlightBooking:
#     def __init__(self):
#         self.flights = {}
    
#     def add_flight(self, flight_number, destination, date, total_seats):
#         self.flights[flight_number] = {
#             'destination': destination,
#             'date': date,
#             'total_seats': total_seats,
#             'available_seats': total_seats,
#             'passengers': []
#         }
    
#     def search_flights(self, destination, date):
#         available_flights = []
#         for flight_number, flight in self.flights.items():
#             if flight['destination'] == destination and flight['date'] == date and flight['available_seats'] > 0:
#                 available_flights.append(flight_number)
#         return available_flights
    
#     def reserve_seat(self, flight_number, passenger_name):
#         if flight_number in self.flights:
#             flight = self.flights[flight_number]
#             if flight['available_seats'] > 0:
#                 flight['available_seats'] -= 1
#                 flight['passengers'].append(passenger_name)
#                 return True
#         return False
    
#     def get_passenger_list(self, flight_number):
#         if flight_number in self.flights:
#             return self.flights[flight_number]['passengers']
#         return []
    
#     def generate_booking_confirmation(self, flight_number):
#         if flight_number in self.flights:
#             flight = self.flights[flight_number]
#             confirmation = f"Booking Confirmation for Flight {flight_number}:\n"
#             confirmation += f"Destination: {flight['destination']}\n"
#             confirmation += f"Date: {flight['date']}\n"
#             confirmation += "Passenger List:\n"
#             for passenger in flight['passengers']:
#                 confirmation += f"- {passenger}\n"
#             return confirmation
#         return "Invalid flight number"


# # Creating a flight booking object
# booking = FlightBooking()

# # Adding flights to the system
# booking.add_flight("FL001", "New York", "2023-07-05", 100)
# booking.add_flight("FL002", "London", "2023-07-05", 200)
# booking.add_flight("FL003", "Paris", "2023-07-06", 150)

# # Searching for available flights
# available_flights = booking.search_flights("New York", "2023-07-05")
# print("Available Flights:", available_flights)

# # Reserving seats for customers
# booking.reserve_seat("FL001", "John Doe")
# booking.reserve_seat("FL001", "Jane Smith")
# booking.reserve_seat("FL002", "David Johnson")

# # Getting passenger list for a flight
# passenger_list = booking.get_passenger_list("FL001")
# print("Passenger List for Flight FL001:", passenger_list)

# # Generating booking confirmation
# confirmation = booking.generate_booking_confirmation("FL001")
# print(confirmation)

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_student_info(self):
        return(f"Name: {self.name}")
        return(f"Age: {self.age}")
        return(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60


student1 = Student("Becky", 60, [45, 80, 95, 40])
student1.display_student_info()
average_grade1 = student1.calculate_average_grade()
print(f"Average Grade: {average_grade1}")
passed1 = student1.has_passed()
print(f"Passed: {passed1}")
print()

student2 = Student("Jannet", 80, [70, 98, 20, 78])
student2.display_student_info()
average_grade2 = student2.calculate_average_grade()
print(f"Average Grade: {average_grade2}")
passed2 = student2.has_passed()
print(f"Passed: {passed2}")

# # # # class Product:
# # # #     def __init__(self, name, price, quantity):
# # # #         self.name = name
# # # #         self.price = price
# # # #         self.quantity = quantity

# # # #     def calculate_total_value(self):
# # # #         return self.price * self.quantity

# # # # # Create multiple objects of the Product class
# # # # product1 = Product("Apple", 1.0, 10)
# # # # product2 = Product("Banana", 0.5, 20)
# # # # product3 = Product("Orange", 0.75, 15)

# # # # # total_value1 = product1.calculate_total_value()
# # # # total_value2 = product2.calculate_total_value()
# # # # total_value3 = product3.calculate_total_value()

# # # # print("Total value of {product1.name}: {product1.calculate_total_value()}")
# # # # print(f"Total value of {product2.name}: {total_value2}")
# # # # print(f"Total value of {product3.name}: {total_value3}")

# # # class MusicFestival:
# # #     def __init__(self):
# # #         self.artists = []
# # #         self.genres = ["hiphop", "reggae", "R&B", "acoustic"]
# # #         self.instruments = []
# # #         self.lineup = []


# # # class Stage(MusicFestival):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.lights = "white"
# # #         self.instruments.extend(["Drum", "microphone"])

# # #     def addToLineup(self, musicType):
# # #         if musicType in self.genres:
# # #             self.lineup.append(musicType)
# # #             return f"Added to lineup: {musicType}"
# # #         else:
# # #             return "This music type is not available"

# # #     def stageManagement(self):
# # #         if self.lineup:
# # #             currentGenre = self.lineup[-1]
# # #             if currentGenre == "hiphop":
# # #                 self.lights = "Blue lights"
# # #             elif currentGenre == "reggae":
# # #                 self.lights = "Green lights"
# # #             elif currentGenre == "R&B":
# # #                 self.lights = "Bright lights"
# # #             return self.lights
# # #         else:
# # #             return self.lights

# # #     def instrumentAssign(self):
# # #         if self.lineup:
# # #             currentGenre = self.lineup[-1]
# # #             if currentGenre == "hiphop":
# # #                 self.instruments.append("bass")
# # #             elif currentGenre == "R&B":
# # #                 self.instruments.append("saxophone")
# # #             elif currentGenre == "reggae":
# # #                 self.instruments.append("lead")
# # #         return self.instruments


# # # festival = MusicFestival()
# # # stage = Stage()
# # # stage.addToLineup("hiphop")
# # # stage.addToLineup("reggae")
# # # print(stage.lineup)
# # # print(stage.stageManagement())
# # # print(stage.instrumentAssign())

