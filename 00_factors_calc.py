# Functions go here

# Puts sereis of symboles at start and end of text
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# display instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quite.")
    print()
    return ""





# checks input is anumber more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter an interger that is more than (or equal to) {}".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# Gets factors, returns a sorted list
def get_factors(to_factor):

    #List to hold factors
    factors_list = []

    #Square root to_factors to find 'half-way'
    limit = int(to_factor**0.5)


    #find factor pairs and to find 'half-way'
    for item in range(1, limit + 1):

        #Cheak factor is not 1 (unity)

        if to_factor == 1:
            break

    # Check if number is a factor
    result = to_factor % item
    factor_1 = int(to_factor // item)   

    # Add factor to a list if it is not already in there
    if result == 0:
        factors_list.append(item)

    if factor_1 != item and result == 0:
            factors_list.append(factor_1)

    # sort list...        
    factors.sort()

    return(factors_list)                      

        
    
# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Dispaly instructions if user has not used the program before
first_time = input("Press <enter> to use instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment= ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number? ") 
    
    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square.".format(var_to_factor)    

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)    

    #Output factors and comment
    statement_generator(heading, "*")   
    print()
    print(factor_list) 
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit")
    print()


print()
print("Than you for using factors calculator")