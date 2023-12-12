import yaml


def load(my_file):
    with open(my_file, "r") as file:
        return yaml.safe_load(file)


def find_tasks(task_name, tasks_data, visited=None):
    if visited is None:
        visited = set()

    task_info = []
    for task in tasks_data:
        if task["name"] == task_name:
            task_info = task
            break

    dependencies = []
    if task_info:
        dependencies.extend(task_info.get("dependencies", []))
        for sub_task_name in dependencies:
            if sub_task_name not in visited:
                visited.add(sub_task_name)
                sub_task_dependencies = find_tasks(sub_task_name, tasks_data, visited)
                dependencies.extend(sub_task_dependencies)

    return dependencies


def find_build_tasks(build_name, builds_data, tasks_data):
    build_tasks = []
    result_tasks = []

    for build in builds_data:
        if build["name"] == build_name:
            build_tasks = build["tasks"]
            break

    for task_name in build_tasks:
        result_tasks.append(task_name)
        result_tasks.extend(find_tasks(task_name, tasks_data))

    return result_tasks


builds_data = load("builds.yaml")["builds"]
tasks_data = load("tasks.yaml")["tasks"]

build_name = "forward_interest"
build_tasks = find_build_tasks(build_name, builds_data, tasks_data)

print(f"Для {build_name} список задач:")
for task in build_tasks:
    print(task)
