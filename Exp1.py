def intersection(l1,l2):
    res = []
    for student in l1:
        if student in l2:
            res.append(student)
    return res
     
a = [1,2,3,4,5,6,7]
b = [2,3,6,7,8]
c = [2,4,6,8,10,12]
print(f"A={a}|\nB={b}|\nC={c}\n")
print(f"a)List of students who play both cricket and badminton = ", end="")
print(intersection(a,b))
def union(l1,l2):
    res = l2.copy()
    for student in l1:
        if not student in l2:
            res.append(student)
    return res
def diff(l1,l2):
    res = []
    for student in l1:
        if not student in l2:
            res.append(student)
    return res
u = union(a,b)
i = intersection(a,b)
print(f"b)List of students who play either cricket or badminton but not both = ", end="")
print(diff(u,i))
diffcb = diff(c,b)
print(f"c)Number os students who play neither cricket nor badminton =", end="")
print(diff(diffcb,a))
unionac = union(a,c)
print(f"d)Number of students who play cricket and football but not badminton =", end="")
print(diff(unionac,b))