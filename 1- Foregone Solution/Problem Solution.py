T = int(input(""))
N = [0 for i in range(T)]
A = []
B = []
a = ""
b = ""
e = 0
flag = 0

for i in range(0, T):
    N[i] = int(input(""))

for x in range(0, len(N)):
    e = e + 1
    l = list(str(N[x]))
    for y in l:
        if y == '4':
            flag = 1
            B.append('3')
            A.append('1')
        elif flag == 1:
            B.append(y)
            A.append('0')
        else:
            B.append(y)

    for v in range(0, len(A)):
        a = a + A[v]

    for m in range(0, len(B)):
        b = b + B[m]

    print("Case #{e}: {a} {b}".format(e=e, a=int(a), b=int(b)))
    a = ""
    b = ""
    A.clear()
    B.clear()
    flag = 0
e = 0
