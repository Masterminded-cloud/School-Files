import a8q2_functions as q2



isValidPhoneNumber_tests = [

               {'inputs'  : ["306-966-4886"],

                'outputs' : True,

                'reason'  : "valid phone number (typical case)"},

               {'inputs'  : ["123-456-7890"],

                'outputs' : True,

                'reason'  : "valid phone number (one of each valid digit)"},

               {'inputs'  : ["306.966-3059"],

                'outputs' : False,

                'reason'  : "invalid separator character used for first separator"},

               {'inputs'  : ["123-456.4305"],

                'outputs' : False,

                'reason'  : "invalid separator character used for second separator"},

               {'inputs'  : ["452.456.1233"],

                'outputs' : False,

                'reason'  : "invalid separator character used for both separators"},

               {'inputs'  : ["306-966-309"],

                'outputs' : False,

                'reason'  : "dashes in correct locations, but not enough numbers"},

               {'inputs'  : ["306-9641-3055"],

                'outputs' : False,

                'reason'  : "too many characters in the number"},

               {'inputs'  : ["abc-edf-ghji"],

                'outputs' : False,

                'reason'  : "correct length, dashes in correct locations, but non-numeric digits used"},

               {'inputs'  : ["306-496-496a"],

                'outputs' : False,

                'reason'  : "correct length, dashes in correct locations, non-numeric digit used at end"},

               {'inputs'  : ["306-496-496a"],

                'outputs' : False,

                'reason'  : "correct length, dashes in correct locations, non-numeric digit used at end"},

               {'inputs'  : ["a06-496-4964"],

                'outputs' : False,

                'reason'  : "correct length, dashes in correct locations, non-numeric digit used at beginning"},

               {'inputs'  : ["(306) 866-5821"],

                'outputs' : False,

                'reason'  : "correct number of digits, but incorrect format"
               }

               ]


# the output for this function is a return value

for test in isValidPhoneNumber_tests:

    inputs = test['inputs']

    result = q2.isValidPhoneNumber(inputs[0])

    if result != test['outputs']:

        print ('Error: isValidPhoneNumber returned', result, 'on inputs', inputs, '('+str(test['reason'])+')')


# we are assuming isValidPhoneNumber works at this point


validatePhoneBook_tests = []


test_book1 = [ { "name" : "Department of Computer Science",

                 "phone number" : "306-966-4886" },

               { "name" : "Department of History",

                 "phone number" : "306.966.8712" },

               { "name" : "Department of Psychology",

                 "phone number" : "(306) 966-6657"
               }

             ]

validatePhoneBook_tests.append({ 'inputs':test_book1,
                                 'outputs':[True, False, False],

                                 'reason' : "a typical case with a mixture of valid and invalid entries" 
                              })


test_book2 = []

validatePhoneBook_tests.append({ 'inputs':test_book2,  
                                 'outputs':[],

                                 'reason' : "an empty phone book should result in no change" 
                              })


test_book3 = [ { "name" : "Department of Computer Science",

                 "phone number" : "306-966-4886" },

               { "name" : "Department of History",

                 "phone number" : "306-966-8712" },

               { "name" : "Department of Psychology",

                 "phone number" : "306-966-6657" }

             ]

validatePhoneBook_tests.append({ 'inputs':test_book3,
                                 'outputs':[True,True,True],

                                 'reason' : "a case where all entries are valid"
                              })


test_book4 = [ { "name" : "Department of Computer Science",

                 "phone number" : "306 966 4886" },

               { "name" : "Department of History",

                 "phone number" : "306.966.8712" },

               { "name" : "Department of Psychology",

                 "phone number" : "(306) 966-6657" }

             ]

validatePhoneBook_tests.append({ 'inputs':test_book4,
                                 'outputs':[False,False,False],

                                 'reason' : "a case where all entries are invalid"  
                              })



test_book5 = [ { "name" : "Department of Computer Science",

                 "phone number" : "306-966-4886" }

             ]


validatePhoneBook_tests.append({ 'inputs':test_book5,
                                 'outputs':[True],

                                 'reason' : "a case with a single valid entry" 
                              })


test_book6 = [ { "name" : "Department of Computer Science",

                 "phone number" : "a306-966-4886" }

             ]

validatePhoneBook_tests.append({ 'inputs':test_book6,
                                 'outputs':[False],

                                 'reason' : "a case with a single invalid entry"
                              })


for test in validatePhoneBook_tests:

    arg = test['inputs']

    q2.validatePhoneBook(arg)

    result = [r['valid'] for r in arg]

    expected = test['outputs']

    
if result != expected:

        print('Error in validatePhoneBook: got',result,'expected', expected,'*** ' + test['reason'])
