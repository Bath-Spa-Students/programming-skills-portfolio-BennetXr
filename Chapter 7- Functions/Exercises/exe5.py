#Describe a city
def describe_city(city, country='china'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('bejing')
describe_city('madrid', 'spain')
describe_city('kerala',"india")
