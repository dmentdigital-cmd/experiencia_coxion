import json

path = r'C:\Users\diego\.gemini\antigravity\brain\9f294d07-a0bc-4758-bea3-eb4bf1817f60\.system_generated\steps\27\output.txt'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for project in data['projects']:
    title = project.get('title', '')
    if 'COXION' in title.upper() or 'KANDELA' in title.upper():
        print(f"Match: {title} - {project['name']}")
