import csv
import math


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    country_info = {}
    
    with open(codeinfo.get("codefile"), newline='') as csv_file:
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=codeinfo.get("separator"), 
                                quotechar=codeinfo.get("quote"))
        for row in csv_reader:
            csv_table.append(row)    

    # Get the plot and data column codes to match up
    plot_codes = csv_table[0].index(codeinfo.get("plot_codes"))
    data_codes = csv_table[0].index(codeinfo.get("data_codes"))

    for data in csv_table[1:]:
        country_info[data[plot_codes]] = data[data_codes]

    return country_info

def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    found_countries = {}
    not_found = set()
    
    converter = build_country_code_converter(codeinfo)
    
#     print("plot_countries - ", plot_countries)
#     print("converter - ", converter)
#     print("gdp_countries - ", gdp_countries,"\n")
    

    # Do all key conversions to lower case   
#     plot_countries_lower = dict((key1.lower(), val1) for key1, val1 in plot_countries.items())  
#     converter_lower = dict((key2.lower(), val2) for key2, val2 in converter.items())
#     gdp_countries_lower = dict((key3.lower(), val3) for key3, val3 in gdp_countries.items()) 
#       
#     print("plot_countries keys - ", plot_countries)
#     print("plot_keys_lower - ", plot_countries_lower, "\n")
#     print("converter keys - ", converter)
#     print("converter_lower - ", converter_lower, "\n")
#     print("gdp_countries keys - ", gdp_countries)
#     print("gdp_countries_lower - ", gdp_countries_lower, "\n")

#     # THIS CODE BLOCK WORKS, PASSES OWLTEST, DO NOT ALTER!!!
#     for country in plot_countries:
#         for code in converter:
#             if country == code.lower() and converter[code] in gdp_countries:
#                 found_countries[country] = converter[code]
#  
#     for country in plot_countries:
#         if country not in found_countries:
#             not_found.add(country)

    for country in plot_countries:
        for code in converter:
            if country.lower() == code.lower():       
                for gdp in gdp_countries:
                    if gdp.lower() == converter[code].lower():
                        found_countries[country] = gdp

    for country in plot_countries:
        if country not in found_countries:
            not_found.add(country)

    return found_countries, not_found


## TESTS
## PASSES FROM
## https://www.coursera.org/learn/python-visualization/discussions/weeks/4/threads/w6HhDlUARVeh4Q5VADVXlQ?sort=createdAtAsc&page=1
codeinfo = {'codefile': 'code4.csv', 'separator': ',', 'quote': '"', 'plot_codes': 'ISO3166-1-Alpha-2', 'data_codes': 'ISO3166-1-Alpha-3'}
plot_countries = {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}
gdp_countries =  {'USA': {'Country Name': 'United States', 'Country Code': 'USA'}, 'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}}
     

print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("({'no': 'NOR', 'us': 'USA'}, {'pr'}) - Expected\n")

# print(reconcile_countries_by_code({'quote': '"', 'codefile': 'code4.csv', 'plot_codes': 'ISO3166-1-Alpha-2', 'separator': ',', 'data_codes': 'ISO3166-1-Alpha-3'}, {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}, {'NOR': {'Country Code': 'NOR', 'Country Name': 'Norway'}, 'PRI': {'Country Code': 'PRI', 'Country Name': 'Puerto Rico'}, 'USA': {'Country Code': 'USA', 'Country Name': 'United States'}}) ) 

"""
For an overview of the function, see here:
http://py3.codeskulptor.org/#user301_eEwf449Gi1_0.py

Below are four examples for reconcile_countries_by_code()
      lc = lowercase, UC = uppercase
One at a time, copy and paste each example block, 
including the two associated print() expressions,
somewhere below your reconcile_countries_by_code() function, then run your module.
If all four produce "Expected" output, you should be ready for OwlTest 
... and for Problem 3.

Please Note: When developing this function, you will find it helpful to 
print out every dictionary, including 
(1) those you are given by OwlTest, 
(2) the 'converter' dictionary that you get from build_country_code_converter(), and 
(3) the various 'lower' converter dictionaries that you make.
Having these at hand will make debugging much easier.
"""

## Example 1 plot_countries lc:UC, code _converter UC:UC
## PASS
print("Example 1 plot_countries lc:UC, code _converter UC:UC")
codeinfo = {'codefile': 'code4.csv', 'plot_codes': 'ISO3166-1-Alpha-2',
            'data_codes': 'ISO3166-1-Alpha-3', 'quote': '"', 'separator': ','}
plot_countries = {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}
gdp_countries =  {'USA': {'Country Name': 'United States', 'Country Code': 'USA'},
                  'PRI': {'Country Name': 'Puerto Rico', 'Country Code': 'PRI'},
                  'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}}
  
print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("({'pr': 'PRI', 'no': 'NOR', 'us': 'USA'}, set()) - Expected\n")

# Example 2 plot_countries UC:lc, code _converter lc:UC
print("Example 2 plot_countries UC:lc, code _converter lc:UC")
codeinfo  =  {'separator': ',', 'quote': "'", 'plot_codes': 'Cd2',
              'data_codes': 'Cd3', 'codefile': 'code2.csv'}
plot_countries = {'C2': 'c2', 'C5': 'c5', 'C4': 'c4', 'C3': 'c3', 'C1': 'c1'}
gdp_countries = {'ABC': {'Country Name': 'Country1', 'Code': 'ABC', '2000': '1', '2001': '2', '2002': '3', '2003': '4', '2004': '5', '2005': '6'},
                'GHI': {'Country Name': 'Country2', 'Code': 'GHI', '2000': '10', '2001': '11', '2002': '12', '2003': '13', '2004': '14', '2005': '15'}}
 
print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("({'C3': 'GHI', 'C1': 'ABC'}, {'C5', 'C2', 'C4'}) - Expected\n")


# Example 3 plot_countries lc:UC, code _converter UC:UC, no countries in gdp_countries
## PASS...?
print("Example 3 plot_countries lc:UC, code _converter UC:UC, no countries in gdp_countries")
codeinfo = {'quote': '"', 'data_codes': 'ISO3166-1-Alpha-3', 
            'plot_codes': 'ISO3166-1-Alpha-2', 'separator': ',', 'codefile': 'code4.csv'}
plot_countries = {'jp': 'Japan', 'cn': 'China', 'ru': 'Russian Federation'}
gdp_countries = {}
 
print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("({}, {'jp', 'cn', 'ru'}) - Expected\n")

# Example 4 plot countries UC:lc, code_converter lc:MixED
print("Example 4 plot countries UC:lc, code_converter lc:MixED")
codeinfo =  {'quote': "'", 'separator': ',', 'plot_codes': 'Code4', 'codefile': 'code1.csv', 'data_codes': 'Code3'}
plot_countries =  {'C4': 'c4', 'C3': 'c3', 'C2': 'c2', 'C1': 'c1', 'C5': 'c5'}
gdp_countries =  {
'qR': {'ID': 'A 5 ', 'CC': 'qR'},
'Kl': {'ID': 'B 6', 'CC': 'Kl'},
'WX': {'ID': 'C 7 ', 'CC': 'WX'},
'ef': {'ID': 'D 8', 'CC': 'ef'}
}

print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("({'C4': 'ef', 'C3': 'Kl', 'C2': 'qR', 'C1': 'WX'}, {'C5'}) - Expected ")
"""
"""

