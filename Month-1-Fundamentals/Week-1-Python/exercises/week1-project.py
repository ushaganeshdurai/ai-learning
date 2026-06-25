import json
todo_list=[]

def add_todo(todo):
    todo_list.append({"task":todo,"done":False})


def list_todos():
    return todo_list

def delete_todo(index):
    real_index = index - 1
    del todo_list[real_index]

def mark_complete(index):
    todo_list[index]["done"] = True

def save_file():
    with open("todos.json","w") as f:
        json.dump(todo_list,f)


while True:
    print("1. Add a task \n 2.List tasks \n3.Mark as complete\n 4.Delete a task\n5.Save tasks")
    choice=input("Enter a number from choice list")
    if choice == '1':
        todo = input("Enter a task to add:")
        add_todo(todo)
    elif choice == '2':
        print(list_todos())
    elif choice == '3':
        task_to_complete = int(input("Enter the index of the task to complete:"))
        mark_complete(task_to_complete)
    elif choice == '4':
        task_to_delete = int(input("Enter the index of the task to delete:"))
        delete_todo(task_to_delete)
    elif choice == '5':
        save_file()
    elif choice == 'q':
        exit()
    else:
        print("Invalid choice. Select again.")
