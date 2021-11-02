

import testingECPM as a8


ecpm_test_suite = [
    
# ad_spend is 0, which should cause 0.0 return

    {
     "inputs": [0,100],

     "outputs": 0.0,

     "reason": "ad_spend of 0, based on first conditional, should return 0.0"
    },


    # ad_impressions is 0, which should cause 0.0 return (avoiding divide by 0)

    {
     "inputs": [100,0],

     "outputs": 0.0,

     "reason": "ad_spend of 0, based on first conditional, should return 0.0"
    },


    # answer is rounded properly

    {
     "inputs": [100,6],

     "outputs": 16666.67,

     "reason": "return value from round() should be 2 digits"
    },


    # both ad_spend and ad_impressions at 0

    {
     "inputs": [0,0],

     "outputs": 0.0,

     "reason": "ad_spend and ad_impressions should not be 0, or return 0.0"
    },


    # caculation is correct for basic input

    {
     "inputs": [123, 123],

     "outputs": 1000.0,

     "reason": "correct value calculated for basic positive inputs"
    },


    # negative values result in 0.0

    {
     "inputs": [-100, -100],

     "outputs": 0.0,

     "reason": "negative value of ad_spend & ad_impressions result in 0.0"
    }

]


for test in ecpm_test_suite:

    inputs = test["inputs"]

    result = a8.calculate_ecpm(inputs[0],inputs[1])

    if result != test["outputs"]:

        print("Testing fault: calculate_ecpm() returned",result,"on inputs",inputs,"(",test["reason"],")")



arpdau_test_suite = [

    # correct calculation is performed

    {
     "inputs": [[1,2,3,4],[112,216,333,442]],

     "outputs": 27.575,

     "reason": "correct value returned with 2 lists of 4 numbers"
    },


    # user_list has no values

    {
     "inputs": [[],[1,2,3,4,5]],

     "outputs": 0.0,

     "reason": "no items in user_list fails conditional and results in 0.0"
    },


    # revenue_list has no values

    {
     "inputs": [[100,200,300,500],[]],

     "outputs": 0.0,

     "reason": "no items in revenue_list fails conditional and results in 0.0"
    },


    # user_list & revenue_list don't have same number of items
    
    {
     "inputs": [[100],[1,2]],

     "outputs": 0.0,

     "reason": "different number of items in user_list & revenue_list fails conditional and results in 0.0"
    },


    # user_list sums up to 0

    {
     "inputs": [[0,0], [1, 2]],

     "outputs": 0.0,

     "reason": "user_list sum is 0 failing conditional and returning 0.0"
    },


    # rounding is done correctly

    {
     "inputs": [[115,200], [10, 20]],

     "outputs": 0.0476,

     "reason": "return value is rounded to 4 or less decimal places properly"
    }

]


for test in arpdau_test_suite:

    inputs = test["inputs"]

    result = a8.calculate_arpdau(inputs[0],inputs[1])

    if result != test["outputs"]:

        print("Testing fault: calculate_arpdau() returned",result,"on inputs",inputs,"(",test["reason"],")")
