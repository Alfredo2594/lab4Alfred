#Exercise 1: Student Grades Analysis----------------------------------------------------------------------------------
#1. Calculate and print the average score for each student.
students = {
    "Alice": [85, 78, 92],
    "Bob": [79, 74, 81],
    "Charlie": [91, 82, 85],
    "David": [76, 85, 83],
    "Eve": [88, 79, 92]
}
for student, scores in students.items():
    average_score = sum(scores) / len(scores)
    print(f"{student}'s average score: {average_score:}")

#2. Find and print the name of the student with the highest average score.
highest=max(students, key=lambda x:students[x])
print('Highest score: ', highest, '   ',students[highest])

#3. Find and print the name of the student with the lowest average score.
lowest=min(students, key=lambda x:students[x])
print('Lowest score: ', lowest, '   ',students[lowest])
#4. Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary.
students ["Frank"] = [80, 90, 85]
print(students)

print()
print()

#Exercise 2: Product Inventory Management------------------------------------------------------------------------------
inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}
#1. Print the current inventory in a user-friendly format.
print("Current Inventory:")
for fruit, (quantity, price) in inventory.items():
    print(f"{fruit.capitalize()}: {quantity} units at ${price:.2f} each")
#2. Calculate and print the total value of the inventory.
total_value = 0
for fruit, (quantity, price) in inventory.items():
    total_value += quantity * price
print()
print(f"Total inventory value: ${total_value:.2f}")
#3. Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
inventory ["mango"] = [30, 0.6]
#4. Update the quantity of "banana" to 120 and print the updated inventory.
inventory["banana"] = (120, inventory["banana"][1])  # Keep the same price
print("Updated Inventory:")
for fruit, (quantity, price) in inventory.items():
    print(f"{fruit.capitalize()}: {quantity} units at ${price:.2f} each")
print()
#5. Remove "pear" from the inventory and print the updated inventory.
del(inventory["pear"])
print("List After Remove pear:")
print()
for fruit, (quantity, price) in inventory.items():
    print(f"{fruit.capitalize()}: {quantity} units at ${price:.2f} each")
print()
print()
#Exercise 3: Employee Records------------------------------------------------------------------------------------------
employees = [
    ("John Doe", "Accounting", "john.doe@example.com"),
    ("Jane Smith", "Marketing", "jane.smith@example.com"),
    ("Emily Davis", "HR", "emily.davis@example.com"),
    ("Michael Brown", "IT", "michael.brown@example.com")
]

#Print names and departments
for employee in employees:
    name, department, _ = employee
    print(f"Name: {name}, Department: {department}")
#Print the email addresses of all employees in alphabetical order by their last names.
sorted_employees = sorted(employees, key=lambda emp: emp[0].split()[-1])
for employee in sorted_employees:
    print(employee[2])
#3. Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.
employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
for employee in employees:
    print(f"Name: {employee}")
#Find and print the department of Jane Smith
for employee in employees:
    if employee[0] == "Jane Smith":
        print(f"Jane Smith works in the {employee[1]} department.")
print()
print()

#Exercise 4: Book Library System--------------------------------------------------------------------------------------
library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye",
"author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird",
"author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}
#Print details of all books
for isbn, details in library.items():
    print(f"ISBN: {isbn}")
    print(f"Title: {details['title']}")
    print(f"Author: {details['author']}")
    print(f"Year: {details['year']}")
#Find and print the details of the book with the ISBN "978-0-14-028329-7".
isbn = "978-0-14-028329-7"
if isbn in library:
    details = library[isbn]
    print(f"ISBN: {isbn}")
    print(f"Title: {details['title']}")
    print(f"Author: {details['author']}")
    print(f"Year: {details['year']}")
else:
    print(f"No book found with ISBN {isbn}")
#Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby",author "F. Scott Fitzgerald", and year 1925.
new_book_isbn = "978-1-4028-9462-6"
library[new_book_isbn] = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
# Update the year of "To Kill a Mockingbird" to 1961
library["978-0-7432-7356-5"]["year"] = 1961
# Print the updated details of "To Kill a Mockingbird"
isbn = "978-0-7432-7356-5"
details = library[isbn]
print(f"ISBN: {isbn}")
print(f"Title: {details['title']}")
print(f"Author: {details['author']}")
print(f"Year: {details['year']}")
#Remove the book with ISBN "978-0-452-28423-4" and print the updated library.
del library["978-0-452-28423-4"]
# Print the updated library
for isbn, details in library.items():
    print(f"ISBN: {isbn}")
    print(f"Title: {details['title']}")
    print(f"Author: {details['author']}")
    print(f"Year: {details['year']}")

print()
print()
#Exercise 5: City Population Data-------------------------------------------------------------------------------------
cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}
#1. Print the population of each city in a user-friendly format.
for city, population in cities.items():
    print(f"The population of {city} is {population}.")
#2. Find and print the city with the highest population.
city_with_highest_population = max(cities, key=cities.get)
highest_population = cities[city_with_highest_population]
print(f"The city with the highest population is {city_with_highest_population} with a population of {highest_population}.")
#3. Find and print the city with the lowest population.
city_with_highest_population = min(cities, key=cities.get)
highest_population = cities[city_with_highest_population]
print(f"The city with the lowest population is {city_with_highest_population} with a population of {highest_population}.")
#4. Update the population of "Phoenix" to 1700000 and print the updated data.
cities["Phoenix"] = 1700000
for city, population in cities.items():
    print(f"The population of {city} is {population}.")
#5. Add a new city "San Francisco" with a population of 884000 and print the updated data.
cities["San Francisco"] = 884000
for city, population in cities.items():
    print(f"The population of {city} is {population}.")

print()
print()
#Exercise 6: Movie Database--------------------------------------------------------------------------------------------
movies = {

"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}
#1. Print the details of all movies in a user-friendly format.
for title, details in movies.items():
    print(f"Movie: {title}")
    print(f"Year: {details['year']}")
    print(f"Rating: {details['rating']}")
    print(f"Genre: {details['genre']}")
#2. Find and print the highest-rated movie.
highest_rated_movie = max(movies, key=lambda movie: movies[movie]["rating"])
highest_rating = movies[highest_rated_movie]["rating"]
print(f"The highest-rated movie is '{highest_rated_movie}' with a rating of {highest_rating}.")
#3. Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}

# Print the updated movie database
for title, details in movies.items():
    print(f"{title}: Year: {details['year']}, Rating: {details['rating']}, Genre: {details['genre']}")
#4. Update the rating of "Inception" to 9.0 and print the updated details.
movies["Inception"]["rating"] = 9.0
updated_movie = movies["Inception"]
print(f"Inception: Year: {updated_movie['year']}, Rating: {updated_movie['rating']}, Genre: {updated_movie['genre']}")
#5. Remove "Pulp Fiction" from the database and print the updated list.
del movies["Pulp Fiction"]
for title, details in movies.items():
    print(f"{title}: Year: {details['year']}, Rating: {details['rating']}, Genre: {details['genre']}")

print()
print()

#Exercise 7: Country Capitals-----------------------------------------------------------------------------------------
countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}
#1. Print the names of all countries and their capitals.
for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")
#2. Find and print the capital of Germany.
germany_capital = countries["Germany"]
print(f"The capital of Germany is {germany_capital}.")
#3. Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
countries["Australia"] = "Canberra"
for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")
#4. Update the capital of "USA" to "New Washington" and print the updated dictionary.
countries["USA"] = "New Washington"
for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")
#5. Remove "France" from the dictionary and print the updated dictionary.
del countries["France"]
for country, capital in countries.items():
    print(f"The capital of {country} is {capital}.")

print()
print()
#Exercise 8: Shopping Cart--------------------------------------------------------------------------------------------
cart = [
    {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
    {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
    {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
    {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]
#1. Print the details of all items in the cart
for item in cart:
    print(f"Item: {item['item']}, Quantity: {item['quantity']}, Price per unit: ${item['price_per_unit']:.2f}")
#2. Calculate the total cost of the cart
total_cost = sum(item["quantity"] * item["price_per_unit"] for item in cart)
print(f"The total cost of the cart is: ${total_cost:.2f}")
#3. Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
new_item = {"item": "grape", "quantity": 5, "price_per_unit": 0.6}
cart.append(new_item)
for item in cart:
    print(f"Item: {item['item']}, Quantity: {item['quantity']}, Price per unit: ${item['price_per_unit']:.2f}")
#4. Update the quantity of "banana" to 10 and print the updated cart.
for item in cart:
    if item["item"] == "banana":
        item["quantity"] = 10
#5. Remove "pear" from the cart and print the updated cart.
cart = [item for item in cart if item["item"] != "pear"]
for item in cart:
    print(f"Item: {item['item']}, Quantity: {item['quantity']}, Price per unit: ${item['price_per_unit']:.2f}")

print()
print()
#Exercise 9: Weather Data----------------------------------------------------------------------------------------------
weather = {
"Monday": {"temperature": 20, "humidity": 60},
"Tuesday": {"temperature": 22, "humidity": 55},
"Wednesday": {"temperature": 19, "humidity": 65},
"Thursday": {"temperature": 23, "humidity": 50},
"Friday": {"temperature": 21, "humidity": 70}
}
#1. Print the weather details for each day.
for day, details in weather.items():
    print(f"{day}: Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%")
#2. Find and print the day with the highest temperature.
highest_temp_day = None
highest_temp = float('-inf')

for day, details in weather.items():
    if details["temperature"] > highest_temp:
        highest_temp = details["temperature"]
        highest_temp_day = day

print(f"The day with the highest temperature is {highest_temp_day} with a temperature of {highest_temp}°C.")
#3. Find and print the day with the lowest humidity.
lowest_humidity_day = None
lowest_humidity = float('inf')

for day, details in weather.items():
    if details["humidity"] < lowest_humidity:
        lowest_humidity = details["humidity"]
        lowest_humidity_day = day

print(f"The day with the lowest humidity is {lowest_humidity_day} with a humidity of {lowest_humidity}%.")
#4. Update the temperature of "Wednesday" to 25 and print the updated weather data.
weather["Wednesday"]["temperature"] = 25
for day, details in weather.items():
    print(f"{day}: Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%")
#5. Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data.
# Add weather data for Saturday
weather["Saturday"] = {"temperature": 24, "humidity": 60}
for day, details in weather.items():
    print(f"{day}: Temperature: {details['temperature']}°C, Humidity: {details['humidity']}%")

print()
print()
#Exercise 10: Library Members------------------------------------------------------------------------------------------
members = [
{"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
{"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
{"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
{"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]
#1. Print the names and ages of all members.
for member in members:
    print(f"Name: {member['name']}, Age: {member['age']}")
#2. Find and print the books borrowed by "Charlie".
for member in members:
    if member["name"] == "Charlie":
        books_borrowed = member["books_borrowed"]
        print(f"Books borrowed by Charlie: {', '.join(books_borrowed)}")
        break
#3. Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
new_member = {"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]}
members.append(new_member)
for member in members:
    print(f"Name: {member['name']}, Age: {member['age']}, Books Borrowed: {', '.join(member['books_borrowed'])}")
#4. Update the age of "Bob" to 31 and print the updated list.
for member in members:
    if member["name"] == "Bob":
        member["age"] = 31
        break

for member in members:
    print(f"Name: {member['name']}, Age: {member['age']}, Books Borrowed: {', '.join(member['books_borrowed'])}")
#5. Remove "David" from the list and print the updated list.
members = [member for member in members if member["name"] != "David"]

for member in members:
    print(f"Name: {member['name']}, Age: {member['age']}, Books Borrowed: {', '.join(member['books_borrowed'])}")