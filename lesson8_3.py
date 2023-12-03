import yaml


def load_yaml(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data


def subtasks(task_name, tasks_data):
    for task in tasks_data.get("tasks", []):
        if task["name"] == task_name:
            return task.get("subtasks", [])
    return []


def build_task_list(build_name, builds_data, tasks_data):
    build_tasks = []
    for build in builds_data.get("builds", []):
        if build["name"] == build_name:
            for task_name in build["tasks"]:
                build_tasks.append(
                    {
                        "name": task_name,
                        "subtasks": subtasks(task_name, tasks_data),
                    }
                )
    return build_tasks


builds_data = load_yaml("builds.yaml")
tasks_data = load_yaml("tasks.yaml")

target_build_name = "forward_interest"


build_tasks_list = build_task_list(target_build_name, builds_data, tasks_data)

for build_task in build_tasks_list:
    print(f"Задача: {build_task['name']}")
    print(f"Подзадачи: {', '.join(build_task['subtasks'])}")
