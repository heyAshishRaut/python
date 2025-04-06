"""
Todo Application
"""

tasks = []

def addTask(task, desc, priority):
    entry = {
        "task" : task,
        "desc" : desc,
        "priority" : priority
    }

    tasks.append(entry)

def getTasks():
    for val in tasks:
        print("---------------------------------------")
        print("Task - ", val["task"])
        print("Priority - ", val["priority"])
        print(f"{val["desc"]}")
        print("---------------------------------------")

def updateTask(oldTaskName, newTaskName, newDescription, newPriority):
    for val in tasks:
        if val["task"] == oldTaskName:
            val["task"] = newTaskName,
            val["desc"] = newDescription
            val["priority"] = newPriority

            print("Updated successfully")
            break
        else:
            print("Task not found")

def deleteTask(task):
    for i, val in enumerate(tasks):
        if val["task"] == task:
            del tasks[i]  
            print(f"Deleted task: {task}")
        else:
            print("Invalid task")

def main():
    while True:
        print("Todo Application")

        print("""
            1. Add Task
            2. Get Tasks
            3. Update Task
            4. Delete Task  
            5. Exit    
        """)
    
        choice = input("Enter choice - ")
    
        match choice:
            case "1":
                task = input("Enter task - ")
                desc = input("Enter description - ")
                priority = input("Enter priority - ")

                addTask(task, desc, priority)
            
            case "2":
                getTasks()

            case "3":
                oldTaskName = input("Enter old task - ")
                newTaskName = input("Enter new task - ")
                newDescription = input("Enter description - ")
                newPriority = input("Enter priority - ")

                updateTask(oldTaskName, newTaskName, newDescription, newPriority)

            case "4":
                task = input("Enter task - ")
                deleteTask(task)
            
            case "5":
                break


if __name__ == "__main__":
    main()