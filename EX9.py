# range(數列首項,數列末項+1, 差值)
for i in range(200, 501, 1):
    # i可以被17與23整除
    if i%17 == 0 and i%23 == 0:
        print(i)
