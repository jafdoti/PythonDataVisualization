"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

# def read_csv_file(file_name, separator, quote):
#     """
#     Helper function to make life easier!
#     Not a graded function
#     """
#     with open(file_name, newline='') as csv_file:
#         csv_table = []
#         csv_reader = csv.reader(csv_file, delimiter=separator, quotechar=quote)
#         for row in csv_reader:
#             csv_table.append(row)
#     return csv_table


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
    csv_data = []
    
    # Build a list of row data from csv
    with open(codeinfo.get("codefile"), newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=codeinfo.get("separator"), 
                                quotechar=codeinfo.get("quote"))
        for row in csv_reader:
            csv_data.append(row)    

    
    # Get the plot and data column indexs to match up codes
    plot_ndx = csv_data[0].index(codeinfo.get("plot_codes"))
    data_ndx = csv_data[0].index(codeinfo.get("data_codes"))

    csv_data.pop(0)
   
    for row in csv_data:
        country_info[row[plot_ndx]] = row[data_ndx]
 
    return country_info

## TESTS
## PASSES BOTH OF THESE TESTS FROM
## https://www.coursera.org/learn/python-visualization/discussions/weeks/4/threads/wKv7Am_eEemrEArKyDxDRA?sort=createdAtAsc&page=1
# codeinfo  =  {'separator': ',', 'quote': "'", 'plot_codes': 'Cd2', 'data_codes': 'Cd3', 'codefile': 'code2.csv'}
# print(build_country_code_converter(codeinfo))
# # Expected:
# #{'c1': 'ABC', 'c2': 'DEF', 'c3': 'GHI', 'c4': 'JKL'}
# 
# 
# codeinfo = {'separator': ',', 'quote': '"', 'codefile': 'code4.csv', 'data_codes': 'ISO3166-1-Alpha-3',
#             'plot_codes': 'ISO3166-1-Alpha-2'}
# print(build_country_code_converter(codeinfo))
# # Expected:
# #{'PR': 'PRI', 'NO': 'NOR', 'US': 'USA', 'AR': 'ARG', 'CH': 'CHE', 'JP': 'JPN', 'CX': 'CXR', 'RU': 'RUS', 'CN': 'CHN'} 

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
    for country in plot_countries:
        for code in converter:
            if country == code.lower() and converter[code] in gdp_countries.keys():
                found_countries[country] = converter[code]

    for country in plot_countries:
        if country not in found_countries:
            not_found.add(country)

    return found_countries, not_found

## TESTS
## PASSES FROM
## https://www.coursera.org/learn/python-visualization/discussions/weeks/4/threads/w6HhDlUARVeh4Q5VADVXlQ?sort=createdAtAsc&page=1
# codeinfo = {'codefile': 'code4.csv', 'separator': ',', 'quote': '"', 'plot_codes': 'ISO3166-1-Alpha-2', 'data_codes': 'ISO3166-1-Alpha-3'}
# plot_countries = {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}
# gdp_countries =  {'USA': {'Country Name': 'United States', 'Country Code': 'USA'}, 'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}}
#    
# print("Expected:  ({'no': 'NOR', 'us': 'USA'}, {'pr'})  ")
# print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """

#     go through the countries in that returned dictionary
#         
#         for those having data for the year you need in the country:data dictionary
#                 add data to output dictionary
#         the others, add to second output set
#             
#     return output dictionary, output set1, outoutput set2
    
    #  read in appropriate gdp file as a nested dict of country:data
    gdp_info = dict()
     
    with open(gdpinfo['gdpfile'], "rt", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=gdpinfo['separator'], quotechar=gdpinfo['quote'])
        for row in csv_reader:
            gdp_info[row[year]] = row
               
    #print("gdp_info - ", gdp_info)
#     
#     #  let reconcile_by_code return a dictionary plot_countries:gdp country codes, and a set, out_set_1
#     country_codes, out_set_1 = reconcile_countries_by_code(codeinfo, plot_countries, gdp_info)
#     print(country_codes)
#     print(out_set_1)
#     
    return {}, set(), set()
    

# gdpinfo = {'country_code': 'CC', 'gdpfile': 'gdptable3.csv', 'quote': "'",
#            'separator': ';', 'country_name': 'ID', 'min_year': 20010, 'max_year': 20017}
# codeinfo = {'separator': ',', 'plot_codes': 'Code4', 'data_codes': 'Code3', 'quote': "'", 
#             'codefile': 'code1.csv'}
# plot_countries =  {'C3': 'c3', 'C2': 'c2', 'C1': 'c1'}
# build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, '20016') 
# if build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, '20016') == \
#       ({'C3': 10.780708577050003, 'C2': 9.301029995663981, 'C1': 9.301029995663981}, set(), set()):
#     print("True")
# else:
#     print("False")

def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    return


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()

"""
# Example 1 plot_countries lc:UC, code _converter UC:UC
print("Example 1 plot_countries lc:UC, code _converter UC:UC")
codeinfo = {'codefile': 'code4.csv', 'plot_codes': 'ISO3166-1-Alpha-2',
            'data_codes': 'ISO3166-1-Alpha-3', 'quote': '"', 'separator': ','}
plot_countries = {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}
gdp_countries =  {'USA': {'Country Name': 'United States', 'Country Code': 'USA'},
                  'PRI': {'Country Name': 'Puerto Rico', 'Country Code': 'PRI'},
                  'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}}
 
print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("Expected:   ({'pr': 'PRI', 'no': 'NOR', 'us': 'USA'}, set())\n")
 
# # Example 2 plot_countries UC:lc, code _converter lc:UC
print("Example 2 plot_countries UC:lc, code _converter lc:UC")
codeinfo  =  {'separator': ',', 'quote': "'", 'plot_codes': 'Cd2',
              'data_codes': 'Cd3', 'codefile': 'code2.csv'}
plot_countries = {'C2': 'c2', 'C5': 'c5', 'C4': 'c4', 'C3': 'c3', 'C1': 'c1'}
gdp_countries = {'ABC': {'Country Name': 'Country1', 'Code': 'ABC', '2000': '1', '2001': '2', '2002': '3', '2003': '4', '2004': '5', '2005': '6'},
                'GHI': {'Country Name': 'Country2', 'Code': 'GHI', '2000': '10', '2001': '11', '2002': '12', '2003': '13', '2004': '14', '2005': '15'}}
  
print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("Expected:  ({'C3': 'GHI', 'C1': 'ABC'}, {'C5', 'C2', 'C4'})\n")
#  
 
# Example 3 plot_countries lc:UC, code _converter UC:UC, no countries in gdp_countries
print("Example 3 plot_countries lc:UC, code _converter UC:UC, no countries in gdp_countries")
codeinfo = {'quote': '"', 'data_codes': 'ISO3166-1-Alpha-3', 
            'plot_codes': 'ISO3166-1-Alpha-2', 'separator': ',', 'codefile': 'code4.csv'}
plot_countries = {'jp': 'Japan', 'cn': 'China', 'ru': 'Russian Federation'}
gdp_countries = {}
 
print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))
print("Expected: ({}, {'jp', 'cn', 'ru'})\n")
 
# # Example 4 plot countries UC:lc, code_converter lc:MixED
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
print("Expected ({'C4': 'ef', 'C3': 'Kl', 'C2': 'qR', 'C1': 'WX'}, {'C5'})\n")



print("Example 5")
codeinfo = {'codefile': 'code4.csv', 'plot_codes': 'ISO3166-1-Alpha-2',
            'data_codes': 'ISO3166-1-Alpha-3', 'quote': '"', 'separator': ','}
plot_countries = {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}
gdp_countries =  {'USA': {'Country Name': 'United States', 'Country Code': 'USA'},
                  'PRI': {'Country Name': 'Puerto Rico', 'Country Code': 'PRI'},
                  'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}}

print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries), "\n")

# Expected:   ({'pr': 'PRI', 'no': 'NOR', 'us': 'USA'}, set())

print("Example 6")
codeinfo  =  {'separator': ',', 'quote': "'", 'plot_codes': 'Cd2',
              'data_codes': 'Cd3', 'codefile': 'code2.csv'}
plot_countries = {'C2': 'c2', 'C5': 'c5', 'C4': 'c4', 'C3': 'c3', 'C1': 'c1'}
gdp_countries = {'ABC': {'Country Name': 'Country1', 'Code': 'ABC', '2000': '1', '2001': '2', '2002': '3', '2003': '4', '2004': '5', '2005': '6'},
                'GHI': {'Country Name': 'Country2', 'Code': 'GHI', '2000': '10', '2001': '11', '2002': '12', '2003': '13', '2004': '14', '2005': '15'}}

print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries), "\n")

# Expected:  ({'C3': 'GHI', 'C1': 'ABC'}, {'C5', 'C2', 'C4'})

print("Example 7")
codeinfo = {'quote': '"', 'data_codes': 'ISO3166-1-Alpha-3', 
            'plot_codes': 'ISO3166-1-Alpha-2', 'separator': ',', 'codefile': 'code4.csv'}
plot_countries = {'jp': 'Japan', 'cn': 'China', 'ru': 'Russian Federation'}
gdp_countries = {}

print(reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries))

# Expected: ({}, {'jp', 'cn', 'ru'}) 
"""
