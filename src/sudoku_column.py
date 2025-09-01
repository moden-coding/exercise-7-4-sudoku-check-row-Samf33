# Write your solution here
def column_correct(list : list, column_num : int):
    column = []
    count1 = 0
    for row in list:
        count1 = 0
        for value in row:
            if count1 == column_num:
                column.append(value)
            count1 +=1
    count1 = 0
    count2 = 0
    for num in column:
        count1 += 1
        for nom in column:
            count2+=1
            if nom == num and nom != 0 and num != 0 and count1 != count2:
                return False
        count2 = 0
    return True

    

if __name__ == "__main__":

    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
        ]
    print(column_correct(sudoku, 0))
    print(column_correct(sudoku, 1))    