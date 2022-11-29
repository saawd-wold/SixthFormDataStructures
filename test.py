import danielsdatastructures as dds

Q = dds.CircularQueue(5)
Q.enqueue(5)
print(Q.isEmpty())
print(Q.dequeue())
print(Q.isEmpty())