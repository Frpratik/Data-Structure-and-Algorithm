l = [1,2,3,5,6,7,9]

start = 0
op = []
for i in range(1,len(l)):
    print("start--->",start)
    if l[i] != l[i-1]+1:
        op.append(f"{l[start]}->{l[i-1]}")
        start = i
op.append(f"{l[start]}->{l[-1]}" if start != len(l)-1 else f"{l[start]}")
print(op)