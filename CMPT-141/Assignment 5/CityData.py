def read_citydata(filename):

    """

    reads city data from a comma-separated text file

    On each line are: neighbourhood, ward, language1, language2, language3, etc...

    :param filename: string  name of input file

    :return: dictionary of city data as database. keys are neighbourhoods

    """

    file = open(filename, "r")

    citydata = {}


    for line in file:

        line = line.strip().split(",")

        neighbourhood = line[0]

        ward = line[1]

        languages = line[2:]

        # create the record

        record = {}

        record["Neighbourhood"] = neighbourhood

        record["Ward"] = ward

        record["Languages"] = languages

        # add record to database

        citydata[neighbourhood] = record


    return citydata



def find_wards(citydata):

    """

    makes a list of all the unique wards

    :param citydata: database of cities, keyed by neighbourhood. 
     Each record has a "Ward" field.

    :return: a list of all the unique wards
 
    """

    wards = []

    for record in citydata.values():

        if record["Ward"] not in wards:

            wards.append(record["Ward"])


    return wards




def ward_neighbourhoods(citydata, ward):

    """

    makes a list of all neighbourhoods that are in a specific ward

    :param citydata: database of cities, keyed by neighbourhood.  Each record has a "Ward" field.

    :param ward: string.  Name of the ward for which to build a list

    :return: a list of neighbourhoods

    """

    neighbourhoods = []

    for neighbourhood in citydata:

        if ward == citydata[neighbourhood]["Ward"]:

            neighbourhoods.append(neighbourhood)


    return neighbourhoods




def count_languages(citydata, neighbourhood_list):

    """

    creates summary counts for each neighbourhood in a list

    :param citydata: database of cities, keyed by neighbourhood.  Each record has a "Languages" field

        containing a list of languages spoken in that neighbourhood

    :param neighbourhood_list: list of neighbourhoods

    :return: dictionary mapping languages to counts of neighbourhoods that speak it

    """

    languages = {}

    for neighbourhood in neighbourhood_list:

        n_languages = citydata[neighbourhood]["Languages"]

        for lang in n_languages:

            if lang not in languages:

                languages[lang] = 1

            else:

                languages[lang] += 1


    return languages


input_file = "CityData.txt"

citydata = read_citydata(input_file)

wards = find_wards(citydata)


print()

print("Welcome to Saskatoon, a diverse city made up of",len(wards),"Wards.")

print()


for ward in wards:

    neighbourhoods = ward_neighbourhoods(citydata, ward)

    print(ward,"contains",len(neighbourhoods),"neighbourhoods.")

    print("Below are the languages spoken in the Ward\nand the number of neighbourhoods where that language is spoken.")

    languages = count_languages(citydata,neighbourhoods)

    print(languages)

    print()