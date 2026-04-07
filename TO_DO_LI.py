tasks = []

while True:
    print("\n1.Add Task  2.View Tasks  3.Remove Task  4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == 2:
        print("Your Tasks:")
        for i, t in enumerate(tasks):
            print(i+1, ".", t)
    elif choice == 3:
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            tasks.pop(num-1)
        else:
            print("Invalid number")
    elif choice == 4:
        break
    else:
        print("Invalid choice")