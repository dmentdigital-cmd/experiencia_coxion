import json

path = r'C:\Users\diego\.gemini\antigravity\brain\9f294d07-a0bc-4758-bea3-eb4bf1817f60\.system_generated\steps\27\output.txt'
with open(path, 'r', encoding='utf-16le' if 'utf-16le' in str(path) else 'utf-8') as f:
    data = json.load(f)

for project in data['projects']:
    text = json.dumps(project).upper()
    if 'COXION' in text:
        print(f"Found COXION in project: {project.get('title')} ({project.get('name')})")
    if 'KANDELA' in text:
        print(f"Found KANDELA in project: {project.get('title')} ({project.get('name')})")
