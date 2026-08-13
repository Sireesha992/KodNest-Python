def add_task(task, tasks=None):
    if tasks is None:
        tasks=[]
    tasks.append(task)
    print(tasks)
print(add_task("Learn Python"))
print(add_task("Practice Functions"))