from random import shuffle

destinations = ["Third Ward","Water St","lakefront"]
restaurants = ["AJ Bombers","Vegabond","Ians"]
transportations = ["Scooters","Uber","Bus"]
entertainments = ["Brewers game","shopping","beach day"]

def get_lists (lists):
    shuffle (lists)
    list = lists[0]
    return list

def final_day_trip(destination, restaurant, transportation, entertainment):
    print ("----------------------------")
    print ("Your final day trip is: ")
    print (" ")
    print (destination)
    print (restaurant)
    print (transportation)
    print (entertainment)
    print (" ")
    print ("----------------------------")
    print ("1. home")
    print ("2. settings")
    final_option = input("please input an option: ")
    if (final_option == "1"):
        start()
    elif (final_option == "2"):
        settings()
    else:
        final_day_trip (destination, restaurant, transportation, entertainment)

def settings():
     print ("------------------------------")
     print ("1. Add to list")
     print ("2. clear lists")
     print ("3. home")
     print (" ")
     settings_option = input ("Please input an option: ")
     if (settings_option == "1"):
         add_choice()
     elif (settings_option == "2"):
         clear_option = input ("Are you sure? (y for yes, n for no): ")
         if clear_option == "y":
             destinations.clear()
             restaurants.clear()
             transportations.clear()
             entertainments.clear()
             print ("Lists have been cleared.")
             settings()
         elif clear_option == "n":
             settings()
         else:
             print ("Invalid option. Please try again.")
             settings()
     elif (settings_option == "3"):
         start()
     else:
         print ("Invalid option. Try again.")
         settings()

def add_choice ():
    print ("--------------------------------")
    print ("1. Add to destinations list")
    print ("2. Add to restaurants list")
    print ("3. Add to transportations list")
    print ("4. Add to entertainments list")
    print ("5. Back to settings")
    print ("6. Home")
    print ("--------------------------------")
    add_option = input("Please input an option: ")
    if add_option == "1":
        add_lists(destinations)
    elif add_option == "2":
        add_lists(restaurants)
    elif add_option == "3":
        add_lists(transportations)
    elif add_option == "4":
        add_lists(entertainments)
    elif add_option == "5":
        settings()
    elif add_option == "6":
        start()
    else:
        print ("Invalid option. Try again.")
        add_choice()

def add_lists (lists):
    print ("--------------------------------")
    lists_input = input("What would you like to add?: ")
    lists.append(lists_input)
    print (lists_input + " add to list.")
    add_choice()

def reshuffle_individual(destination, restaurant, transportation, entertainment):
    print ("-----------------------------------")
    print ("1. " + destination)
    print ("2. " + restaurant)
    print ("3. " + transportation)
    print ("4. " + entertainment)
    print (" ")
    individual_choice = input ("What do you want to change?: ")
    if individual_choice == "1":
        print ("Your new destination is: ")
        individual_destination = get_lists(destinations)
        new_day_trip(individual_destination, restaurant, transportation, entertainment)
    elif individual_choice == "2":
        print ("Your new restaurant is: ")
        individual_restaurant = get_lists(restaurants)
        new_day_trip(destination, individual_restaurant, transportation, entertainment)
    elif individual_choice == "3":
        print ("Your new mode of transportation is: ")
        individual_transportation = get_lists(transportations)
        new_day_trip(destination, restaurant, individual_transportation, entertainment)
    elif individual_choice == "4":
        print ("Your new form of entertainment is: ")
        individual_entertainment = get_lists(entertainments)
        new_day_trip(destination, restaurant, transportation, individual_entertainment)
    else:
        print ("Invalid option. Please try again.")
        reshuffle_individual(destination, restaurant, transportation, entertainment)
    
def reshuffle_choice (destination, restaurant, transportation, entertainment):
     print ("Options: ")
     print ("-----------")
     print ("1. Reshuffle All")
     print ("2. Reshuffle individual option")
     print ("3. confirm day trip")
     print (" ")
     confirm_option = input("Please input an option: ")
     if (confirm_option == "1"):
         reshuffle_destination = get_lists(destinations)
         reshuffle_restaurant = get_lists(restaurants)
         reshuffle_transportation = get_lists(transportations)
         reshuffle_entertainment = get_lists(entertainments)
         new_day_trip(reshuffle_destination, reshuffle_restaurant, reshuffle_transportation, reshuffle_entertainment)
     elif (confirm_option == "2"):
        reshuffle_individual(destination, restaurant, transportation, entertainment)
     elif (confirm_option == "3"):
        final_day_trip(destination, restaurant, transportation, entertainment)
     else:
        print ("Invalid option. try again.")
        reshuffle_choice(destination, restaurant, transportation, entertainment)

def new_day_trip(destination, restaurant, transportation, entertainment):
     print ("------------------------------")
     print (destination)
     print (restaurant)
     print (transportation)
     print (entertainment)
     print (" ")
     reshuffle_choice(destination,restaurant,transportation,entertainment)

def start_choice():
    print ("------------------------------")
    print ("Day Trip generator")
    print (" ")
    print ("1. New Day Trip")
    print ("2. Settings")
    start_option = input ("please input the number of the option you want: ")
    if (start_option == "1"):
        return
    elif (start_option == "2"):
        settings()
    else:
        print ("Invalid option. try again.")
        start_choice()

def start ():
    start_choice()
    destination = get_lists(destinations)
    restaurant = get_lists(restaurants)
    transportation = get_lists(transportations)
    entertainment = get_lists(entertainments)
    new_day_trip(destination, restaurant, transportation, entertainment)

start()