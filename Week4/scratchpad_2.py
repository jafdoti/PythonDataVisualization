import csv

plot_countries = {'pr': 'PuertoRico', 'no': 'Norway', 'fr': 'France'}
gdp_countries = { 'PRI': {'name': 'Puerto Rico', 'data': 'some_data'}, 'NOR': {'name': 'Norway', 'data': 'some_data'} }
converter = {'PR': 'PRI', 'NO': 'NOR', 'FR': 'FRA' }
#converter = {'pR': 'Pri', 'no': 'NOR', 'fr': 'fRa' }


def build_country_code_converter(codeinfo):

    country_info = {}
    
    with open(codeinfo.get("codefile"), newline='') as csv_file:
        csv_table = []
        csv_reader = csv.reader(csv_file, delimiter=codeinfo.get("separator"), 
                                quotechar=codeinfo.get("quote"))
        for row in csv_reader:
            csv_table.append(row)    

    # Get the plot and data column indexes to get codes to match up
    plot_codes = csv_table[0].index(codeinfo.get("plot_codes"))
    data_codes = csv_table[0].index(codeinfo.get("data_codes"))

    for data in csv_table[1:]:
        country_info[data[plot_codes]] = data[data_codes]

    return country_info

    
def simple_reconcile_countries_by_code(converter, plot_countries, gdp_countries):
    
    # Return values
    found_countries = {}
    not_found = set()
    
    lower_converter = {}
    
    print("Converter - ", converter)
    for code in converter:
        lower_converter[code.lower()] = converter[code]   
    
    
    for country in plot_countries:
        for code in converter:
            if country == code.lower() and converter[code] in gdp_countries.keys():
                found_countries[country] = converter[code]

    for country in plot_countries.keys():
        if country not in found_countries.keys():
            not_found.add(country)

    return found_countries, not_found       
    
print(simple_reconcile_countries_by_code(converter, plot_countries, gdp_countries))
# Expected: {'pr': 'PRI', 'no': 'NOR'}, {'fr'}

"""
2. Challenge 2:

... But there is one problem: the entries in 'converter' can be in any case: 
    {'Pr': 'prI', 'nO': 'NOr', 'Fr': 'FrA' }, or {'pR': 'Pri', 'no': 'NOR', 'fr': 'fRa' } , 
    or any other combination.

Modify your code from Challenge 1 so that it works with either of the two examples above, 
(or any other combinations of upper-and-lowercase keys and values)
assigned to the argument 'converter'.

"""