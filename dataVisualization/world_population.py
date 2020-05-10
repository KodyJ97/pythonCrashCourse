import json

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
# Print the 2010 population for each country
for pop_dict in pop_data:
    if str(pop_dict['Year']) == '1970':
        country_name = pop_dict['Country Name']
        population = int(pop_dict['Value'])
        print(country_name + ": " + str(population))
