import sys
import configparser
import pandas as pd
from jira import JIRA
from jira.exceptions import JIRAError

# Read Jira credentials from the INI file
print("Reading Jira credentials from the INI file")
config = configparser.ConfigParser()
config.read('/secrets/jira_credentials.ini')

jira_url = config.get('jira', 'url')
jira_username = config.get('jira', 'username')
jira_api_token = config.get('jira', 'api_token')

# Establish a connection to Jira
print("Establishing a connection to Jira")
print("Jira URL:", jira_url)
# Try to establish a connection to Jira and handle exceptions
try:
    jira = JIRA(server=jira_url, basic_auth=(jira_username, jira_api_token))
except JIRAError as e:
    print(f"Failed to connect to Jira: {e}")
    sys.exit(1)

# Get a list of all projects
print("Getting a list of all projects")
projects = jira.projects()
print(f"Found {len(projects)} projects")
print("Projects:", projects)
# Initialize an empty list to store data from all projects
all_data = []

# Iterate through the projects and fetch data for each project
print("Fetching data for each project")
for project in projects:
    project_key = project.key

    # Search for issues using JQL query
    jql = f"project={project_key}"
    print(f"Searching for issues in project {project_key}")
    issues = jira.search_issues(jql)

    # Extract required information from the issues
    for issue in issues:
        title = issue.fields.summary
        description = issue.fields.description
        created_date = issue.fields.created
        current_status = issue.fields.status.name
        project_name = project.name

        all_data.append([project_name, project_key, title, description, created_date, current_status])

# Create a pandas DataFrame
columns = ["Project Name", "Project Key", "Title", "Description", "Created Date", "Current Status"]
df = pd.DataFrame(all_data, columns=columns)

# Display the DataFrame
print(df)
