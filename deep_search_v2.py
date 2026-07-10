import json
import os

file_path = r'C:\Users\diego\.gemini\antigravity\brain\9b1ecd5f-aa41-4e56-9897-ecbc52b726a0\.system_generated\steps\103\output.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = ["COXION", "KANDELA", "COXION", "Kandela"]

found = []
for project in data.get('projects', []):
    title = project.get('title', '')
    design_md = project.get('designTheme', {}).get('designMd', '')
    
    match_found = False
    for kw in keywords:
        if kw.lower() in title.lower() or kw.lower() in design_md.lower():
            match_found = True
            break
            
    if match_found:
        found.append({
            'title': title,
            'name': project.get('name')
        })

print(json.dumps(found, indent=2))
