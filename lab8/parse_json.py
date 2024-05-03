import json

with open('data/schacon.repos.json', 'r') as file:
    data = json.load(file)

with open('chacon.csv', 'w') as csv_file:
    for repo in data[:5]:
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']
       
        csv_file.write(f"{name},{html_url},{updated_at},{visibility}\n")
