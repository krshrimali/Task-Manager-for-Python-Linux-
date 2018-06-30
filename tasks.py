import datetime
import os
import subprocess as s

os.system("reset")
# os.system("python3 tasks.py")
# global
today = datetime.date.today()
day = datetime.datetime.today().weekday() # Monday is 0, Sunday is 6

# removes new line character from a list having strips
# for file reading
def remove_newline(content):
    revised_content = []
    for line in content:
        line = line.strip('\n')
        revised_content.append(line)
    return revised_content

# check date of the file with current date
def check_if_same_date(content):
    # date mentioned in the task file
    print(content[0].split(': '))
    file_date = content[0].split(': ')[1]
    # cross check date with today
    if(file_date == str(today)):
        return 1
    else:
        return 0

# count number of tasks
def get_count_tasks(content):
    n_task = content[len(content) - 1].split(': ')[1]
    return n_task

# find tasks before
def get_all_tasks(content):
    # tasks are from line number 4 to len(content) - 2
    tasks = []
    for i in range(3, len(content) - 2):
        tasks.append(content[i])
    return tasks

# check mode
mode = input("Writing or Reading? (W/R)")

# check mode - if write, then create another file
if(mode == "W"):
    filename = str(today) + ".txt"
    if(os.path.exists(filename)):
        existing_file = open(filename, 'r+')
        content_new = existing_file.readlines()
        existing_file.close()

        existing_file = open(filename, "w+")
        content = remove_newline(content_new)
        # existing_file.close()

        if(check_if_same_date(content)):
            toAdd = input("Do you want to add any tasks? (Y/N)")
            
            n_tasks = int(get_count_tasks(content))

            if(n_tasks != 0):
                tasks_before = get_all_tasks(content)
                print(tasks_before)

            while(toAdd == "Y"):
                task = str(input("Task: \n"))
                deadline = str(input("Deadline: [Format: DD.MM/5:30:PM\n"))
                
                print("Setting reminder before 1 hour of the deadline.\nSnoozing after every 5 minutes of the alarm.")

                last_index = len(content) - 1


                content[last_index - 1] = str(n_tasks + 1) + ": " + task + "\t\t" + deadline + "\n"
                content[last_index] = str("\n")
                

                n_tasks += 1


                content.append("Total: " + str(n_tasks))
                toAdd = input("Do you want to add any tasks? (Y/N)")
                
                if(toAdd == 'N'):
                    for i in range(0, 3):
                        content[i] = content_new[i]
                    
                    existing_file.writelines(content)
                    existing_file.close()
                    break
                last_index += 1
        print(content)
    else:
        file = open(str(today) + ".txt", 'w')
        file.write("Date: " + str(today) + "\n")
        file.write("Day:  " + str(day) + "\n\n\n")
        file.write("Total: " + str(0) + "\n") # line number 5
        file.close()
print("Tasks: ")