"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data
    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    
    countries = set()
    country_info = {}
    
    for code in plot_countries:
        if plot_countries.get(code) not in gdp_countries:
            countries.add(code)
        else:
            country_info[code] = plot_countries.get(code)

    # A tuple containing a dictionary and a set
    return (country_info, countries)


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    countries = {}
    not_found = set()
    missing = set()
    
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

    # A tuple containing a dictionary and two sets
    return (countries, not_found, missing)


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    # Eh, it works
    world_map = pygal.maps.world.World()
    world_map.title = 'GDP by Country for ' + year 
    gdp_data = build_map_dict_by_name(gdpinfo, plot_countries, year)
    
    world_map.add('GDP - ' + year, gdp_data[0])
    world_map.add('Missing/Unavailable GDP Data', gdp_data[1])
    world_map.add('No GDP Data', gdp_data[2])
    world_map.render_to_file(map_file)


def test_render_world_map():
    """
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

#test_render_world_map()
