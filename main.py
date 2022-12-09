"""
A brief demonstration on parameter passing functions from Sprint 2.
The beginnings of a searchable database of concert information.
A brief explanation of the different kinds of operators from Sprint 1.
"""
__author__ = "Scott Topazi"

from tinydb import TinyDB, \
    Query  # Start by importing the 'books' we need from the tinydb library
# to interact and manipulate data within the database.

import math

db = TinyDB(
    'musicdatabase.json')  # We've created a blank database or uploaded an


# existing database called TinyDB and have assigned it to store its data in a
# .json file.


def triangle_area(a, b, c):
    """
    This function is a set of instructions that will calculate the area of a
    triangle and will return the final answer being the square root area to
    when the function is called in line 43.
    :param a: First side of triangle.
    :param b: Second side of triangle.
    :param c: Third side of triangle.
    :return: Final step in calculating the area of the triangle.
    """
    half_parameters = 0.5 * (a + b + c)
    radicand_area = half_parameters * (half_parameters - a) * (
            half_parameters - b) * (half_parameters - c)
    square_root_area = math.sqrt(radicand_area)
    return square_root_area


def list_of_items(category):
    """
    Defining a function to list all items from the various search queries
    throughout the program with a parameter of category.
    :param category: Date, Type, Name, Performers
    :return: Returns the results from the query of each category.
    """
    for item in category:
        print(item)


def crap_1():
    """
    This is the parameter passing section.
    :return:
    """
    print('\n')
    side_a = int(input("Enter the length of side a: "))
    side_b = int(input("Enter the length of side b: "))
    side_c = int(input("Enter the length of side c: "))

    print("The area of this triangle is", triangle_area(side_a, side_b,
                                                        side_c))


def main():
    """
    This is the main purpose of this program: A searchable database of concert
    program information.
    :return:
    """
    list_of_items(
        db)  # Recalling a function to list all items within the database.

    print('\n')

    #  def insert():
    #      ID = input("Enter ID: ")
    #      dateStr = input("Enter full date: ")
    #      typeStr = input("Enter the type of concert: ")
    #      insertStr = "{'ID': '" + ID + "', 'date': '" + dateStr + "',
    #      'type': '" + typeStr +"'}"
    #      print(insertStr)
    #      db.insert(insertStr)
    #
    #  insert()

    Concert = Query()  # Assigning our search Query 'book' to the variable
    # Concert.

    print("1) Date", "2) Type", "3) Name", sep='\n')  # Listing the first set
    # of options separated by a line feed carriage return.
    do_again = True  # Setting up a condition to test throughout the coming
    # while loop.
    answer1 = input(
        "Enter the appropriate number of category by which you would like to "
        "search our concerts: ")
    print('\n')
    while do_again:  # Initiating a while loop with the condition assigned
        # earlier. Loop will continue as long as the condition is met.
        if answer1 == "1":
            concert_date = input(
                "Please enter the date in the following format: mmddyy ")
            results_date = db.search(
                Concert.ID == concert_date)  # Performing a search within the
            # database using the input from the concert_date variable. This
            # particular date format is actually found in the ID category.
            print('\n')
            list_of_items(
                results_date)  # Recalling a function to list items found in
            # results_date.
            do_again = False  # This will break the condition of the loop, thus
            # stopping and jumping to the end of the loop.
        elif answer1 == "2":
            print(
                "a) Large Ensemble", "b) Nisita Concert Series", "c) Recital "
                                                                 "Class",
                "d) Junior Recital", "e) Senior Recital", sep='\n')
            # Option 2, presents another list of options, all listed separated
            # by a line feed carriage return.
            answer_type = input(
                "Enter the letter of type by which you would like to search "
                "our concerts: ")
            do_type_again = True  # Setting up a condition for a new while loop
            # within the main while loop.
            while do_type_again:  # Initiating a while loop with the condition
                # assigned in the previous line. This loop will continue as
                # long as this condition is met.
                if answer_type == "a":
                    results_type = db.search(
                        Concert.type == "Large Ensemble")  # Performing a
                    # search within the database using the input from the
                    # answer_type variable which in this case is 'a' being
                    # linked to Large Ensemble.
                    print('\n')
                    list_of_items(
                        results_type)  # Recalling a function to list items
                    # found in results_type. In this case, Large Ensemble.
                    do_type_again = False  # This will break the condition of
                    # this inside loop, thus stopping and jumping to the end of
                    # this loop.
                elif answer_type == "b":
                    results_type = db.search(
                        Concert.type == "Nisita Concert Series")  # Performing
                    # asearch within the database using the input from the
                    # answer_type variable which in this case is 'b' being
                    # linked to Nisita Concert Series.
                    print('\n')
                    list_of_items(
                        results_type)  # Recalling a function to list items
                    # found in results_type. In this case, Nisita Concert
                    # Series.
                    do_type_again = False  # This will break the condition of
                    # this inside loop, thus stopping and jumping to the end
                    # of this loop.
                elif answer_type == "c":
                    results_type = db.search(
                        Concert.type == "Recital Class")  # Performing a search
                    # within the database using the input from the answer_type
                    # variable which in this case is 'c' being linked to
                    # Recital Class.
                    print('\n')
                    list_of_items(
                        results_type)  # Recalling a function to list items
                    # found in results_type. In this case, Recital Class.
                    do_type_again = False  # This will break the condition of
                    # this inside loop, thus stopping and jumping to the end of
                    # this loop.
                elif answer_type == "d":
                    results_type = db.search(
                        Concert.type == "Junior Recital")  # Performing a
                    # search within the database using the input from the
                    # answer_type variable which in this case is 'd' being
                    # linked to Junior Recital.
                    print('\n')
                    list_of_items(
                        results_type)  # Recalling a function to list items
                    # found in results_type. In this case, Junior Recital.
                    do_type_again = False  # This will break the condition of
                    # this inside loop, thus stopping and jumping to the end
                    # of this loop.
                elif answer_type == "e":
                    results_type = db.search(
                        Concert.type == "Senior Recital")  # Performing a
                    # search within the database using the input from the
                    # answer_type variable which in this case is 'e' being
                    # linked to Senior Recital.
                    print('\n')
                    list_of_items(
                        results_type)  # Recalling a function to list items
                    # found in results_type. In this case, Senior Recital.
                    do_type_again = False  # This will break the condition of
                    # this inside loop, thus stopping and jumping to the end
                    # of this loop.
                else:
                    answer_type = input(
                        "Invalid entry...please enter a valid entry: ")
                    do_type_again = True  # Loop condition is met which means
                    # the loop will continue until a valid entry is entered.
                    # This marks the end of this inside loop.
            do_again = False  # This will break the condition of the main while
            # loop, thus stopping and jumping to the end of the loop.
        elif answer1 == "3":
            answer_name = input(
                "Enter the name of the concert you would wish to find. ")
            results_name = db.search(
                Concert.name == answer_name)  # Performing a search within the
            # database using the input from the answer1 variable which in this
            # case is '3' being linked to the name category.
            print('\n')
            list_of_items(
                results_name)  # Recalling a function to list items found in
            # results_name.
            do_again = False  # This will break the condition of the main while
            # loop, thus stopping and jumping to the end of the loop.
        else:
            if answer1 != range(1,
                                4):  # If the user input does not equal the
                # range from 1 to 4 (1, 2, 3), the user will be prompted to
                # enter a valid entry.
                answer1 = input("Please enter a valid entry: ")
                do_again = True  # The loop condition is met, so the loop will
                # continue until a valid entry has been entered.
    print('\n')
    do_performer_again = True  # Setting up a condition to be met for the while
    # loop up ahead.
    answer2 = input(
        "Would you like to search a specific performer? y for yes, any other "
        "key for no: ")
    print('\n')
    while do_performer_again:  # Initiating a while loop with the condition
        # assigned a few lines earlier. This loop will continue as long as
        # this condition is met.# Initiating the loop
        if answer2 == "y":
            answer_performers = input(
                "Enter the last name of the performer you would like to look "
                "up. ")
            # Search for Kemmerer and you'll find the concert(s) she performed
            # in.
            print('\n')
            results_performers = db.search(Concert.performers.any(
                answer_performers))  # Performing a search within the database
            # using the input from the answer_performers variable. This is set
            # up so that if the input matches ANY indices within the
            # performers category over all items, those items will be sorted
            # out.
            list_of_items(
                results_performers)  # Recalling a function to list items found
            # in results_performers.
            do_performer_again = False  # This will break the condition of the
            # loop, thus stopping and jumping to the end of the loop.
        else:
            if not (answer2 == "y"):
                do_performer_again = False  # This still breaks the condition
                # of the loop, but the user is shown an additional message
                # instead of just the last one.
                print("I hope this program was helpful!")
    print('\n')
    print("Thank you for using this program!")


def crap_2():
    """
    An explanation of the various operators from Sprint 1
    :return:
    """
    # An explanation of the exponent operator **
    print('\n')
    print("Next, we'll look at some commonly used numeric operators.\n")
    print("First up is the exponent operator: ** .")
    print(
        "This operator will raise the first integer to the power of the "
        "second integer.")
    print("4 ** 2 =", 4 ** 2)
    print("Let's try some numbers of your own.")
    power_first_num = input("Enter your base number: ")
    power_sec_num = input(
        "Enter the exponent in which to raise the base number: ")
    print(power_first_num + " ** " + power_sec_num + " =",
          int(power_first_num) ** int(power_sec_num))
    print("\n")

    # An explanation of the multiplication operator *

    print("Next, we will take a look at the multiplication operator: * .")
    print("This operator will multiply two integers together.")
    print("4 * 2 =", 4 * 2)
    print("Let's try some numbers of your own again.")
    multi_first_num = input("Enter your first number: ")
    multi_sec_num = input("Enter your second number: ")
    print(multi_first_num + " * " + multi_sec_num + " =",
          int(multi_first_num) * int(multi_sec_num))
    print("\n")

    # An explanation how the multiplication operator works with strings

    print(
        "Interestingly, the multiplication operator can work with string "
        "types as well.")
    print(
        "For example, 'Hello World!' * 5 with print Hello World! 5 times, "
        "like so:")
    print("Hello World!" * 5)
    animal = input("What is your favorite animal? ")
    qty = input("How many times would you like it to repeat? ")
    print(animal * int(qty))
    print("\n")

    # An explanation of the division operator /

    print("Now, we will move on to the division operator: / .")
    print("This operator will divide one number by another number.")
    print("10 / 5 =", 10 / 5)
    print("Enter in some numbers of your own again.")
    div_first_num = input("Enter your first number: ")
    div_sec_num = input("Enter the number you'd like to divide by: ")
    print(div_first_num + " / " + div_sec_num + " =",
          int(div_first_num) / int(div_sec_num))
    print("\n")

    # An explanation of the addition (+) and subtraction (-) operators

    print("Up next, we'll use two operators: addition (+) and subtraction "
          "(-).")
    print(
        "Obviously, + will add two numbers and - will subtract one number "
        "from another.")
    print("3 + 4 =", 3 + 4)
    print("4 - 3 =", 4 - 3)
    print("Now, enter in a few numbers to add together.")
    add_first_num = input("Enter first number: ")
    add_sec_num = input("Enter second number: ")
    add_third_num = input("Enter third number: ")
    add_final_num = input("And one more: ")
    print(add_first_num + " + " + add_sec_num + " + " + add_third_num + " + " +
          add_final_num + " =", int(add_first_num) + int(add_sec_num) +
          int(add_third_num) + int(add_final_num))
    print("\n")

    # An explanation how the addition operator works with strings

    print(
        "Similar to the multiplication (*) operator, addition (+) can be used "
        "on string types as well.")
    print(
        "For example, look what happens when we add the two words camp and "
        "ground together by running the code 'camp' + 'ground'.")
    print("camp" + "ground", "\n")
    print("Next, enter two numbers you would like to subtract.")
    sub_first_num = input("Enter your first number: ")
    sub_sec_num = input(
        "Enter your second number for which you will subtract: ")
    print(sub_first_num + " - " + sub_sec_num + " =",
          int(sub_first_num) - int(sub_sec_num))
    print("\n")

    # An explanation on the modulus (%) and floor division (//) operators

    print(
        "Finally, we'll look at a couple of special operators that are quite "
        "useful in accounting and other financial situations.")
    print("Those are the modulus (%) and the floor division (//) operators.")
    print(
        "There are essentially three parts to a division problem: dividend, "
        "divisor, and quotient.")
    print(
        "The quotient is the solution to a division problem, but the dividend "
        "doesn't always get divided evenly by the divisor, so a remainder is "
        "left over.")
    print("That's where these operators come in handy.")
    print(
        "The modulus (%) operator will only give us the remainder portion of "
        "the quotient.")
    print("For example, try entering in two numbers that will not divide "
          "evenly.")
    mod_first_num = input("Enter your first number: ")
    mod_sec_num = input("Enter your second number: ")
    print(mod_first_num + " % " + mod_sec_num + " =",
          int(mod_first_num) % int(mod_sec_num))
    print("\n")
    print(
        "On the other hand, the floor division (//) operator will only give "
        "us the whole number portion of the quotient.")
    print(
        "Try two different numbers that do not divide evenly and try to "
        "guess what you think the answer will be.")
    floor_first_num = input("Enter your first number: ")
    floor_sec_num = input("Enter your second number: ")
    print(floor_first_num + " // " + floor_sec_num + " =",
          int(floor_first_num) // int(floor_sec_num))


def crap_3():
    """
    This section is adding the AND and OR to fulfill part of the requirements
    from Sprint 2.
    :return:
    """
    total_sales = int(
        input("Enter your total amount above sales goal below $25,000: "))
    do_again = True
    while do_again:
        if (total_sales > 15000) and (total_sales <= 25000):
            print("Excellent!")
            do_again = False
        elif (total_sales > 10000) and (total_sales <= 15000):
            print("Good! However, there's still room for improvement!")
            do_again = False
        elif (total_sales > 5000) and (total_sales <= 10000):
            print("Fair, but some improvements are expected to be made by "
                  "next evaluation.")
            do_again = False
        elif (total_sales > 1) and (total_sales <= 5000):
            print("Poor, if improvements aren't made by next evaluation, then "
                  "you will be placed on a probationary period.")
            do_again = False
        elif (total_sales < 1) or (total_sales > 25000):
            total_sales = int(input("Invalid entry: please try again: "))
            do_again = True


main()
crap_1()
crap_2()
crap_3()
