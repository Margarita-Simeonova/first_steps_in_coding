ONE_PROJECT_TIME = 3


def project_creation(name: str, projects_count: int):

    total_time = projects_count * ONE_PROJECT_TIME
    result = (f"The architect {name} will need "
              f"{total_time} hours to complete {projects_count}"
              f" project/s.")
    return result


name_arg = input()
projects_count_arg = int(input())
result = project_creation(name_arg, projects_count_arg)

print(result)
