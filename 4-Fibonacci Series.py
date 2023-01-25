n = int(input("For how many numbers your want the series to be printed? -> "))
first_num = 0
sec_num = 1
for i in range(n):
    print(first_num)
    temp = first_num
    first_num = sec_num
    sec_num = sec_num + temp
    