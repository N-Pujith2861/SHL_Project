import psycopg2
import requests
from transformers import pipeline

# Connect to the PostgreSQL database
conn = psycopg2.connect(database="project_search", user="project_search")
cur = conn.cursor()

# Create a smart search pipeline
smart_search_pipeline = pipeline("text-to-sql", use_gpu=True, token="YOUR_GPT_3.5_4_API_TOKEN")

# Define a function to do smart search for projects in the database using GPT-3.5/4
def smart_search_projects(query):
    """Uses GPT-3.5/4 to do multi-attribute search for projects in the database."""

    query_with_availability = f"SELECT * FROM projects WHERE name ILIKE %s OR technologies ILIKE %s OR frontend_skills ILIKE %s OR backend_skills ILIKE %s OR databases_skills ILIKE %s OR infrastructure_skills ILIKE %s AND availability = '{query}';"

    # Search for projects using the modified query
    projects = cur.execute(query_with_availability, (f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%", f"%{query}%"))

    return projects

# Define a function to render the project gallery view
def render_project_gallery(projects):
    """Renders the project gallery view."""

    return (
        f"<div>"
        f"{projects.map((project) => (f"<div key={project.id}><h3>{project.name}</h3><p>{project.technologies}</p><p>{project.availability}</p></div>"))}"
        f"</div>"
    )

# Start the web server
if __name__ == "__main__":
    app.run(debug=True)
