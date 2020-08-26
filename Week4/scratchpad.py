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

#  let reconcile_by_code return a dictionary plot_countries:gdp country codes, and a set, out_set_1
#     go through the countries in that returned dictionary
#         
#         for those having data for the year you need in the country:data dictionary
#                 add data to output dictionary
#         the others, add to second output set
#             
#     return output dictionary, output set1, outoutput set2
    countries = {}
    not_found = set()
    missing = set()
    
#  read in appropriate gdp file as a nested dict of country:data    
    with open(gdpinfo.get("gdpfile"), 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=gdpinfo.get("separator"), 
                                quotechar=gdpinfo.get("quote"))
        for data in reader:
            for country in plot_countries:
                if plot_countries.get(country) in data.values():
                    try:
                        countries[country] = math.log10(float(data.get(year)))
                    except ValueError:
                        missing.add(country)
                        continue
                    
    # We found countries that have gdp data or missing data
    # Now build the set of missing/not found countries
    for country in plot_countries:
        if country not in countries and country not in missing:
            not_found.add(country)

    return {}, set(), set()


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
