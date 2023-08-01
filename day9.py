# #first_dictionary_challenge
# student_scores = {
#     "faftini": 13,
#     "bebe" : 60,
#     "usman" : 93,
#     "momed" : 85,
#     "fascroba" : 97,
#     "olajiga" : 23,
#     "esther" : 78,
# }
# students_grades = {}
# for key in student_scores:
#     if student_scores[key] > 90:
#         students_grades[key] = "Outstanding"
#     elif student_scores[key] > 80:
#         students_grades[key] = "Exceeds expections"
#     elif student_scores[key] > 70:
#         students_grades[key] = "Acceptable"
#     else:
#         students_grades[key] = "failed"
# print(students_grades)

# #second_dictionary_challenge
# travel_log = [
#     {
#         "countries_visited": "france", 
#         "cities_visited": ["paris", "lille", "Djon"], 
#         "total_visits": 12
#     },
#     {
#         "countries_visited":"germany", 
#         "cities_visited": ["Berlin", "Harbug", "Stutgartt"], 
#         "total_visits": 12
#     }
# ]

# def add_dictionary(country, amounts_of_visits, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["cities_visted"] = cities 
#     new_country["total_visits"] = amounts_of_visits
#     travel_log.append(new_country)
    

# add_dictionary("Russia", 2, ["moscow", "saint petersburg"])
# print(travel_log)

#Auction_challenge
from python import clear
print("welcome to my first silent auction, if you would like to place a bid, please state your name and price below.")
bid_over = False
contestants = {}
while not bid_over:
    name = input("what is your name?\n")
    bid = int(input("How much would you like to bid?\n$"))
    def auction(Name, Bidding_price):
        contestants[Name] = Bidding_price
    auction(Name = name, Bidding_price = bid)
    end = input("Are there any other bidders? Yes/no\n")
    End = end.lower()
    if End == "no":
        bid_over = True
    else:
        bid_over = False
        clear()
highest_price = 0
for contender in contestants:
    if contestants[contender] > highest_price:
        highest_price = contestants[contender]
        winner = contender
print(f"The winner is {winner} with a bid of ${highest_price}")