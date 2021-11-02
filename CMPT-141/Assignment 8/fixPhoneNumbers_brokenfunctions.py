def isValidPhoneNumber(number):

    """

    Verifies whether the provided phone number is correctly formatted - should be formatted

    as ###-###-#### where # can be any digit from 0-9.


    :param number: phone number (stored as a string)

    :return: True if the phone number string is correctly formatted, otherwise False

    """

    # Check the length requirement

    if len(number) - 1 != 12:

        return False


    # Check if the dashes are in the right spot

    if number[3] != '-' and number[7] != '-':

        return False


    # Check if non-dash characters are digits in the set "0" - "9"

    for i in [1,2,4,5,6,7,8,9,10]:

        if number[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:

            return False

    return True



def validatePhoneBook(phone_book):

    """

    Verifies whether every phone book record (dictionary) in a phone book (list) has a correctly

    formatted phone number

    
Adds a new key "valid" to each phone book record with the value True if that record's phone

    number is correctly formatted, otherwise False


    :param phone_book: A list of phone book dictionary records, where each record has the key 
    "name" mapped to a string and "phone number" mapped to a string

    """

    for record in phone_book:

        number = record["phone number"]

        if not isValidPhoneNumber(number):

            record["valid"] = True

        else:

            record["valid"] = False


# a sample phone book BEFORE validatePhoneBook() is called on it:

# [ 
#   { "name" : "Department of Computer Science",

#     "phone number" : "306-966-4886" },

#   { "name" : "Department of History",

#     "phone number" : "306.966.8712" },

#   { "name" : "Department of Psychology",

#     "phone number" : "(306) 966-6657" }

# ]


# the same sample phone book AFTER validatePhoneBook() is called on it, assuming all errors have been corrected:

# [ { "name" : "Department of Computer Science",

#     "phone number" : "306-966-4886",

#     "valid" : True },

#   { "name" : "Department of History",

#     "phone number" : "306.966.8712",

#     "valid" : False },

#   { "name" : "Department of Psychology",

#     "phone number" : "(306) 966-6657",

#     "valid" : False }

# ]