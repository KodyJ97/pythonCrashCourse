import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# pip3 install requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print("Status code: ", r.status_code)

# Store API response in a variable
response_dict = r.json()

# Process the results.
print("Total Repositories: ", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

# Retrieve name and plot_dicts
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Retrieve the project description, if one is available
    description = repo_dict['description']
    if not description:
        description = 'No description provided.'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

    """ -- Data --
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
    """

# Make a visualization.
my_style = LS('#336699', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
