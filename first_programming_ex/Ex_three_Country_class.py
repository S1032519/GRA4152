"""
This class (Country) is used to find the largest populated country, largest country by area and the country with highes population density.

The methods are: 
    - def populationDensity(self): ## Method that returns the population density for a country
    - def list_country_w_largest_area(countrylist): ## Method that takes a list and returns the country with the largest area
    - def list_country_w_largest_pop(countrylist): ## Method that takes a list and returns the country with the largest population
    - def list_country_w_largest_popdensity(countrylist): ## Method that takes a list and returns the country with the largest population density
    - def dict_country_w_largest_area(countrydict): ## Method that takes a dictionary and returns the country with the largest area
    - def dict_country_w_largest_pop(countrydict): ## Method that takes a dictionary and returns the country with the largest population
    - def dict_country_w_largest_popdensity(countrydict): ## Method that takes a dictionary and returns the country with the largest population density

Argparse is used to handle the description of the program and also the parameters to input.
"""
import argparse

class Country: ## Defining the class
    def __init__(self, country_name, population, area): ## Defining the constructor
        self._country_name = str(country_name) ## Instance variable, should be a string
        self._population = int(population) ## Instance variable, should be integer
        self._area = float(area) ## Instance variable, should be float

    def populationDensity(self): ## Method that returns the population density for a country
        return self._population / self._area ## returns the population density

    ## Using lists as input
    def list_country_w_largest_area(countrylist): ## Method that takes a list and returns the country with the largest area
        largest = countrylist[0] ## Initalise the object with the first country in the list
        for i in countrylist: ## Loop trough each country in the list
            if i._area > largest._area: ## Check if current country in "largest" has a larger area than the ith country in the list
                largest = i ## If the above is true large is updated
        return largest._country_name ## returns the country name with the largest area
        
    def list_country_w_largest_pop(countrylist): ## Method that takes a list and returns the country with the largest population
        largest = countrylist[0]
        for i in countrylist:
            if i._population > largest._population:
                largest = i
        return largest._country_name
            
    def list_country_w_largest_popdensity(countrylist): ## Method that takes a list and returns the country with the largest population density
        largest = countrylist[0]
        for i in countrylist:
            if i.populationDensity() > largest.populationDensity(): ## Here we use the populationDensity method to compare densities
                largest = i
        return largest._country_name


    ## Using dictionaries as input
    def dict_country_w_largest_area(countrydict): ## Method that takes a dictionary and returns the country with the largest area
        largest1 = next(iter(countrydict.keys())) ## iterates over the keys in the dictionary and gets the first one 
        for name, country in countrydict.items(): ## Looping over each key and value pair in the dict
            if country._area > countrydict[largest1]._area: ## Check if current country in "largest1" has a larger area than the ith "largest1" key
                largest1 = name ## If the above is true largest1 is updated
        return largest1 ## returns the country name with the largest area
        
    def dict_country_w_largest_pop(countrydict): ## Method that takes a dictionary and returns the country with the largest population
        largest1 = next(iter(countrydict.keys())) 
        for name, country in countrydict.items(): 
            if country._population > countrydict[largest1]._population: 
                largest1 = name
        return largest1
        
    def dict_country_w_largest_popdensity(countrydict): ## Method that takes a dictionary and returns the country with the largest population density
        largest1 = next(iter(countrydict.keys()))
        for name, country in countrydict.items():
            if country.populationDensity() > countrydict[largest1].populationDensity():
                largest1 = name
        return largest1

## Using argparse to specify input for the program
parser = argparse.ArgumentParser(description="Find country with largest area, population, and density") ## Description
parser.add_argument("--country", type=str, nargs="+", help="A country in the format: Name,Population,Area") ## How to add the parameters ex --country "Country1, 2000, 3000" "Country2, 1500, 10000" "Country3, 100, 100"
arguments = parser.parse_args()

countries = [] ## List comperhension to split name, population size and area into list format
for country in arguments.country:
    name, population, area = country.split(",")
    countries.append(Country(name, population, area))

countries_dict = {} ## Convert input into dictionary with country name as key and the country objects of the class Country as values.
for country_str in arguments.country:
    name, population, area = country_str.split(",")
    country_dict_transform = Country(name, population, area)
    countries_dict[name] = country_dict_transform

print("Using Lists:")
print("Country with largest area:", Country.list_country_w_largest_area(countries))
print("Country with largest population:", Country.list_country_w_largest_pop(countries))
print("Country with largest population density:", Country.list_country_w_largest_popdensity(countries))

print("Using Dictionaries:")
print("Country with largest area:", Country.dict_country_w_largest_area(countries_dict))
print("Country with largest population:", Country.dict_country_w_largest_pop(countries_dict))
print("Country with largest population density:", Country.dict_country_w_largest_popdensity(countries_dict))