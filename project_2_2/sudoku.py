import threading

solution = [[6,2,4,5,3,9,1,8,7], 
            [5,1,9,7,2,8,6,3,4],
            [8,3,7,6,1,4,2,9,5], 
            [1,4,3,8,6,5,7,2,9],
            [9,5,8,2,4,7,3,6,1], 
            [7,6,2,3,9,1,4,5,8],
            [3,7,1,9,5,6,8,4,2],
            [4,9,6,1,8,2,5,7,3],
            [2,8,5,4,7,3,9,1,6]]

accurate = []

#first check if solution is a valid 9x9 grid

#check if each row has 1ea of 1 thru 9 values

def Row():
    row_checker = 1;
    for i in range(9):
        counter = 0
        for x in range(9):
            #verify numbers are 1 thru 9
            if solution[x][i] > 10 or solution[x][i] < 1:
                row_checker = 0
            counter = counter + solution[x][i]
        if counter != 45:
            row_checker = 0;
    accurate.append(row_checker)
    print(row_checker)

#check if each column has 1ea of 1 thru 9 values

def Column():
    column_checker = 1;
    for i in range(9):
        counter = 0
        for x in range(9):
            #verify numbers are 1 thru 9
            if solution[x][i] > 10 or solution[x][i] < 1:
                row_checker = 0
            counter = counter + solution[i][x]
        if counter != 45:
            column_checker = 0;
    accurate.append(column_checker)
    print(column_checker)

#check if each 3x3 square has 1ea of 1 thru 9 values

def Grid():
    grid_checker = 1;
    for n in range(0, 9, 3):
        counter = 0
        for i in range(n, n+3):
            for x in range (n, n+3):
                if solution[i][x] > 10 or solution[i][x] < 1:
                    grid_checker = 0
                counter = counter + solution[i][x]
        if counter != 45:
            grid_checker = 0;
    accurate.append(grid_checker)
    print(grid_checker)


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=Row)
    t2 = threading.Thread(target=Column)
    t3= threading.Thread(target=Grid)
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # starting thread 3
    t3.start()

    # wait until threads are completely executed
    t1.join()
    t2.join()
    t3.join()
  
    # both threads completely executed
    print("Done!")

    if 0 in accurate:
        print("This Sudoku is Incorrect")  
    else:
        print("This Sudoku is Correct!")
