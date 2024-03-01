import sqlite3

# Make a database
con = sqlite3.connect("taskmanager.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS tasks(taskname, task, deadline)")

while True:
    print("+.Create a new task")
    print("-.Delete a task")
    print("1.See a task")
    print("0.Quit")

    question = input("Enter your choice: ")

    if question == "+":
        def create():
            task_name = input("Enter the title of the task: ")
            task_desc = input("Enter a task description: ")
            deadline = input("Enter the deadline: ")

            # Use placeholders in the SQL query to avoid SQL injection
            cur.execute("INSERT INTO tasks VALUES (?, ?, ?)", (task_name, task_desc, deadline))
            con.commit()  # Commit the changes to the database

        create()

    elif question == "-":
        delete = input("The title of the task you want to delete: ")
        cur.execute("DELETE FROM tasks WHERE taskname=?", (delete,))
        con.commit()

    elif question == "1":
        find = input("What task do you want to see? Enter the title: ")
        cur.execute("SELECT task FROM tasks WHERE taskname=?", (find,))
        result = cur.fetchone()
        if result:
            print(f"Task: {result[0]}")
        else:
            print(f"No task found with the title '{find}'")

    elif question == "0":
        break  # Exit the loop if the user enters 0

    else:
        print("Invalid choice. Please enter a valid option.")

# Close the database connection after completing the operation
con.close()
