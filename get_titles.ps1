$json = Get-Content 'C:/Users/diego/.gemini/antigravity/brain/9f294d07-a0bc-4758-bea3-eb4bf1817f60/.system_generated/steps/27/output.txt' -Raw | ConvertFrom-Json
$json.projects.title | Out-File -FilePath 'C:/Users/diego/Documents/DIEGOSAN/PROYECTO COXION/LANDING HECHA EN ANTIGRAVITY/project_titles.txt'
