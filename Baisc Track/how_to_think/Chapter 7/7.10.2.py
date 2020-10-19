#2. Write a program that reads a file and prints only those lines that contain the substring snake.


def find_snake(file):
    with open(file, "r") as infile:
        for line in infile:
            if "snake"in line:
                print(line)

find_snake("C:\\Users\\Anna\\Desktop\\Learning Community\\snake.txt")