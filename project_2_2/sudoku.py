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

#first check if solution is a valid 9x9 grid

#check if each row has 1ea of 1 thru 9 values
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

#check if each column has 1ea of 1 thru 9 values
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

#check if each 3x3 square has 1ea of 1 thru 9 values
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


print(row_checker)
print(column_checker)
print(grid_checker)
