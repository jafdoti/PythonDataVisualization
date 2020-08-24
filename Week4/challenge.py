""" Here is a stepwise approach to reconcile_countries_by_code():
1.  Background and general idea:
You are given two dictionaries:

plot_countries ---> {'pr': "PuertoRico", 'no': 'Norway', 'fr': 'France'}
gdp_countries ---> { 'PRI': {dict containing country data for Puerto Rico}, 'NOR': {'dict containing country data for Norway } }

... and you also have a dictionary which you have created
using the function, country_code_converter():  converter ---> {'PR': 'PRI', 'NO': 'NOR' }

You must use these three to make a new dict consisting of 
the following items from the dictionaries above: 
{key: value}, where key = plot_countries key, and value = gdp_countries key

You will use the general flow: 
plot_countries_key => converter_key ==> converter_value ==> gdp_countries_key

It should output:  {'pr': 'PRI', 'no': 'NOR'}

If there are codes in plot_countries for countries not found in plot_countries, 
they should be included in a set, in this case, {'fr')

Stepwise introduction to reconcile_countries_by_code(), part 2

1.  Challenge 1  So, first, copy everything between the ###, paste it into your IDE, 
and add code where you see # code here to give the expected output.
    ###############
"""
from astropy.wcs.docstrings import convert
plot_countries = {'pr': 'PuertoRico', 'no': 'Norway', 'fr': 'France'}
gdp_countries = { 'PRI': {'name': 'Puerto Rico', 'data': 'some_data'}, 'NOR': {'name': 'Norway', 'data': 'some_data'} }
converter = {'PR': 'PRI', 'NO': 'NOR', 'FR': 'FRA' }

def simple_reconcile_countries_by_code(converter, plot_countries, gdp_countries):
    out_dict = {}
    out_set = set()
    converter = build_country_code_converter(codeinfo)
    # code here  (6 - 10 lines)
    for country in plot_countries.keys():
        for code in converter.keys():
            if country == code.lower() and converter[code] in gdp_countries.keys():
                print(country, converter[code])
                out_dict[country] = converter[code]

    for country in plot_countries.keys():
        if country not in out_dict.keys():
            out_set.add(country)
    
    print(out_dict, out_set)
    return out_dict, out_set    
    
simple_reconcile_countries_by_code(converter, plot_countries, gdp_countries)

#print(simple_reconcile_countries_by_code(converter, plot_countries, gdp_countries))
# Expected: {'pr': 'PRI', 'no': 'NOR'}, {'fr'}
    ##############

#    *********************************
#    
# 2. Challenge 2:
# 
# ... But there is one problem: the entries in 'converter' can be in any case: 
#     {'Pr': 'prI', 'nO': 'NOr', 'Fr': 'FrA' }, or {'pR': 'Pri', 'no': 'NOR', 'fr': 'fRa' } , 
#     or any other combination.
# 
# Modify your code from Challenge 1 so that it works with either of the two examples above, 
# (or any other combinations of upper-and-lowercase keys and values)
# assigned to the argument 'converter'.
# 
#    *********************************
# 
# 3. Next steps
# 
# Note that the actual parameters for this function in the assignment are not 
# (converter, plot_countries, gdp_countries), 
# but rather (codeinfo, plot_countries, gdp_countries).  
# The only place where codeinfo is used is to obtain 
# the converter dictionary from build_country_code_converter(),
# which you have presumably already coded successfully.
# So, to your code above just add the line, 
# 
# converter = build_country_code_converter(codeinfo)
# 
# 
# Then, go here:
# https://py3.codeskulptor.org/#user305_PfNa7iJ0fNCXtzH_1.py
#     
# ... and work out the four "real world" challenges there. If you 
# receive "Expected" for all four, your function will pass OwlTest.
# """
