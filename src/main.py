import tkinter
import time
import random

window = tkinter.Tk()
window.title("Sorting Algorithm Visualizer")
canvas = tkinter.Canvas(window, bg="white", height=650, width=1200)

LIGHT_GRAY = "#a9a9a9"
DARKER_GRAY = "#878787"
DARK_GRAY = "#555555"

unsorted_list = []
color_count = 1
lines = []
colors = []

def generate_list():
    global color_count
    global unsorted_list
    global lines
    global colors

    unsorted_list = []

    if lines != []:
        for line in lines:
            canvas.delete(line)

    lines = []

    for i in range(0, 99):
        unsorted_list.append(random.randint(1, 50))

    for i in range(0, len(unsorted_list)):
        color_count += 1
        if color_count > 3:
            color_count = 1
        if color_count == 1:
            color = LIGHT_GRAY
        elif color_count == 2:
            color = DARKER_GRAY
        elif color_count == 3:
            color = DARK_GRAY
        line = canvas.create_rectangle(i * 10, 5, (i * 10) + 10, unsorted_list[i] * 10, outline=color, fill=color)
        lines.append(line)
        colors.append(color)

        canvas.update()

generate_list()

def bubble_sort(myList):
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            canvas.itemconfig(lines[j], outline="green")
            canvas.itemconfig(lines[j], fill="green")
            canvas.update()
            time.sleep(0.05)
            canvas.itemconfig(lines[j], outline=colors[j])
            canvas.itemconfig(lines[j], fill=colors[j])
            canvas.update()
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
                loc1 = canvas.coords(lines[j])
                loc2 = canvas.coords(lines[j + 1])
                diff = loc1[0] - loc2[0]
                canvas.move(lines[j], -diff, 0)
                canvas.move(lines[j + 1], diff, 0)
                templine = lines[j]
                lines[j] = lines[j + 1]
                lines[j + 1] = templine

    for line in lines:
        canvas.itemconfig(line, outline="black")
        canvas.itemconfig(line, fill="green")
    print(f"Sorted list: {myList}")
    return myList

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        canvas.itemconfig(lines[i], outline="green")
        canvas.itemconfig(lines[i], fill="green")
        canvas.update()
        time.sleep(0.05)
        canvas.itemconfig(lines[i], outline=colors[i])
        canvas.itemconfig(lines[i], fill=colors[i])
        canvas.update()
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
            loc1 = canvas.coords(lines[i])
            loc2 = canvas.coords(lines[min_index])
            diff = loc1[0] - loc2[0]
            canvas.move(lines[i], -diff, 0)
            canvas.move(lines[min_index], diff, 0)
            templine = lines[i]
            lines[i] = lines[min_index]
            lines[min_index] = templine

    for line in lines:
        canvas.itemconfig(line, outline="black")
        canvas.itemconfig(line, fill="green")
    print(f"Sorted list: {my_list}")
    return my_list

def insertion_sort(aList):
    for i in range(1, len(aList)):
        temp = aList[i]
        j = i - 1
        canvas.itemconfig(lines[i], outline="green")
        canvas.itemconfig(lines[i], fill="green")
        canvas.update()
        time.sleep(0.05)
        canvas.itemconfig(lines[i], outline=colors[i])
        canvas.itemconfig(lines[i], fill=colors[i])
        canvas.update()
        while temp < aList[j] and j > -1:
            aList[j + 1] = aList[j]
            aList[j] = temp
            loc1 = canvas.coords(lines[j])
            loc2 = canvas.coords(lines[j + 1])
            diff = loc1[0] - loc2[0]
            canvas.move(lines[j], -diff, 0)
            canvas.move(lines[j + 1], diff, 0)
            templine = lines[j]
            lines[j] = lines[j + 1]
            lines[j + 1] = templine
            j -= 1

    for line in lines:
        canvas.itemconfig(line, outline="black")
        canvas.itemconfig(line, fill="green")
    print(f"Sorted list: {aList}")
    return aList

def run(sort):
    if sort == "Bubble Sort":
        bubble_sort(unsorted_list)
    elif sort == "Selection Sort":
        selection_sort(unsorted_list)
    elif sort == "Insertion Sort":
        insertion_sort(unsorted_list)


options = ["Bubble Sort", "Selection Sort", "Insertion Sort"]
chosen = tkinter.StringVar()
chosen.set("Bubble Sort")
sort_type = tkinter.OptionMenu(window, chosen, *options)
sort_type.pack(padx=5, side=tkinter.TOP)

run_button = tkinter.Button(text="Run", command=lambda:run(chosen.get()))
run_button.pack(padx=5, side=tkinter.TOP)

genlist_button = tkinter.Button(text="New List", command=lambda:generate_list())
genlist_button.pack(padx=5, side=tkinter.TOP)

canvas.pack()
window.mainloop()
