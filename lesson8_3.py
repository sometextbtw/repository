import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def find_task_dependencies(task_name, tasks_data):
    task_info = next((task for task in tasks_data if task['name'] == task_name), None)
    dependencies = []
    if task_info:
        dependencies.extend(task_info.get('dependencies', []))
        for subtask_name in task_info.get('subtasks', []):
            dependencies.extend(find_task_dependencies(subtask_name, tasks_data))
    return dependencies

def find_build_tasks(build_name, builds_data, tasks_data):
    build_tasks = next((build['tasks'] for build in builds_data if build['name'] == build_name), [])
    result_tasks = []

    for task_name in build_tasks:
        result_tasks.append(task_name)
        result_tasks.extend(find_task_dependencies(task_name, tasks_data))

    return result_tasks

builds_data = load_yaml('builds.yaml')['builds']
tasks_data = load_yaml('tasks.yaml')['tasks']

build_name = 'forward_interest'
build_tasks = find_build_tasks(build_name, builds_data, tasks_data)

print(f"Билд - {build_name}")
print("Список задач:")
for task in build_tasks:
    print(task)