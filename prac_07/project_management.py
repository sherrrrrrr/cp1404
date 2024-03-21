import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%"

    def update(self, percent_complete='', priority=''):
        if percent_complete:
            self.percent_complete = int(percent_complete)
        if priority:
            self.priority = int(priority)

    def is_after_date(self, date):
        project_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        filter_date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        return project_date > filter_date

# Define utility functions for loading, saving and displaying projects
def load_projects(file_name):
    projects = []
    try:
        with open(file_name, 'r') as file:
            file.readline()  # Skip header line
            for line in file:
                name, start_date, priority, cost_estimate, percent_complete = line.strip().split('\t')
                project = Project(name, start_date, int(priority), float(cost_estimate), int(percent_complete))
                projects.append(project)
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with an empty project list.")
    return projects
def save_projects(file_name, projects):
    with open(file_name, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.percent_complete}\n")

def display_projects(projects):
    incomplete_projects = [project for project in projects if project.percent_complete < 100]
    completed_projects = [project for project in projects if project.percent_complete == 100]

    if incomplete_projects:
        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")
    if completed_projects:
        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")

def add_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    percent_complete = input("Percent complete: ")
    project = Project(name, start_date, int(priority), float(cost_estimate), int(percent_complete))
    projects.append(project)

def update_project(projects):
    # Display all projects with indexes for user selection
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]
    print(selected_project)

    # Ask for new values, update only if input is provided
    new_percent_complete = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()

    # Update project if new values are provided
    selected_project.update(percent_complete=new_percent_complete if new_percent_complete else '',
                            priority=new_priority if new_priority else '')

    print("Project updated successfully.")
    # Optionally, print the updated project details
    print(selected_project)

def filter_projects_by_date(projects):
    date = input("Show projects that start after date (dd/mm/yyyy): ")
    filtered_projects = [project for project in projects if project.is_after_date(date)]
    for project in filtered_projects:
        print(f"  {project}")

def main():
    file_name = 'projects.txt'
    projects = load_projects(file_name)

    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {file_name}")

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'q':
            if input("Would you like to save to projects.txt? ").lower() in ['yes', 'y']:
                save_projects(file_name, projects)
            print("Thank you for using custom-built project management software.")
            break
        elif choice == 'l':
            projects = load_projects(file_name)  # Corrected
        elif choice == 's':
            save_projects(file_name, projects)  # Corrected
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid option, please try again.")



if __name__ == "__main__":
    main()