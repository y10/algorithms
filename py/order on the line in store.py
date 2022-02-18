# store
# k = people
#     baskets (time to process)
# n cahiers

# the order of people 

from queue import PriorityQueue

cashiers = 2
line = [1,10,5,3]
q = PriorityQueue(cashiers)
s = 0
for i in range(len(line)):
    t = line[i]
    if q.qsize() < cashiers:
        q.put((t, i))
    else:
        (tt, ii) = q.get()
        if tt <= (t + s):
            s += tt
        q.put((t, i))
        print(f"{ii}  {line[ii]} ms")

while not q.empty():
    (t, i) = q.get()
    print(f"{i}  {line[i]} ms")


