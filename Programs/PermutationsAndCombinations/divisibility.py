
# inclusive range
start = 1
stop = 1000
step = 1

# change stop
stop += step
counter = []

for i in range(start, stop, step):
        if (i % 2 != 0 and i % 3 != 0)  :
            counter.append(i)
            print(i, end=' ')


print(" --- Total count %s "  %len(counter))