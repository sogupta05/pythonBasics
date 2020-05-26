#yield creates an iterator internally
#yield does not  terminate the function like Return so thats the difference between return and yield
# fetching 1000 records from the databases, all 1000 records will be loaded in the memory.  generator can
#be used to fetch values one by one instead of loading everything in the memory
def topten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n +=1



values = topten()

print(next(values))
for i in values:
    print(i)