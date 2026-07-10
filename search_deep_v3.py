import json
import os

# We will check the 34 projects found
file_path = r'C:\Users\diego\.gemini\antigravity\brain\9b1ecd5f-aa41-4e56-9897-ecbc52b726a0\.system_generated\steps\103\output.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

projects = data.get('projects', [])

print(f"Total projects to check: {len(projects)}")

# Keywords to search
keywords = ["COXION", "KANDELA", "COXION", "Kandela"]

for i, project in enumerate(projects):
    title = project.get('title', 'No Title')
    name = project.get('name')
    print(f"[{i+1}/{len(projects)}] Checking project: {title} ({name})")
    
    # Check designMd
    design_md = project.get('designTheme', {}).get('designMd', '')
    for fw in keywords:
        if fw.lower() in design_md.lower():
            print(f"  FOUND '{fw}' in designMd for {title}")
    
    # Check screen titles in the project object (already listed)
    screens = project.get('screenInstances', [])
    for screen in screens:
        # Note: screenInstances in the list_projects output might not have all the text content
        pass

print("Done checking project metadata.")
