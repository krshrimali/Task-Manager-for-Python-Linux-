from threading import Timer
import os
import datetime
import time
import subprocess as s

def get_all_tasks(content):
    # tasks are from line number 4 to len(content) - 2
    tasks = []
    for i in range(3, len(content) - 2):
        tasks.append(content[i])
    return tasks

def callbackfunc(task, filename):
    s.call(['notify-send', 'ALERT', task])
    print('task called was: ', task[0])
    deleteTask(task[0], filename)

def deleteTask(task_number, filename):
    task_number = int(task_number)
    # for 1st task - line number 3
    # for 2nd task - "     "     4
    # and so on . . . 
    file_ = open(filename, 'r+')
    content = file_.readlines()
    content_new = remove_newline(content)

    print("Deleting..., ", content[3 + int(task_number) - 1])
    
    content[3 + task_number - 1] = "1. Done!"
    file_.writelines(content)
    file_.close()

def startTimer(interval_, task, files):
    print('timer is: ', interval_)
    print('timer started for: ', task)
    t = Timer(interval_, callbackfunc, args=[task, files])
    t.start()
    # t.join()

def remove_newline(content):
    revised_content = []
    for line in content:
        line = line.strip('\n')
        revised_content.append(line)
    return revised_content


text_files = [x for x in os.listdir() if '.txt' in x]

while True:
    for files in text_files:
        file = open(files, 'r')
        content  = file.readlines()
    
        # date_ = remove_newline(content)[len(content)-3].split('\t')[2].split('/')[0].split('.')
        # time_ = remove_newline(content)[len(content)-3].split('\t')[2].split('/')[1].split(':')
    
    
        revised_content = remove_newline(content)
        tasks = get_all_tasks(revised_content)
    
        for task in tasks:
            print(task)
            date_ = task.split('\t')[2].split('/')[0].split('.')
            time_ = task.split('\t')[2].split('/')[1].split(':')
    
            print(date_, time_)
    
            current_time = datetime.datetime.now().time()
            
            # update this
            current_hour, current_minute = current_time.hour, current_time.minute
    
            deadline_hour, deadline_minute = int(time_[0]), int(time_[1])
    
            # keep on updating this
            timer_time = 60 * (deadline_hour - current_hour) + deadline_minute - current_minute
            
            startTimer(timer_time * 60, task, files)
            # print(datetime.datetime.now().date())
            
            task_added = input("Task added? (Y/N)")
            if(task_added == "Y"):
                print("exiting, and resetting the timer for you")
                os.system("exit_and_call_again.sh")
            
