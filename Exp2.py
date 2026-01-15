marklist=[20,20,27,94,None,20,57,None,10,57,20,None,91,94,56,None]
avg=0
absent=0
t=[]
total=0

#Absent
for i in marklist:
    if i==None:
        absent=absent+1
    else:
        t.append(i)

#Average
total=sum(t)
print("The average score of class:",total/len(marklist))
print("Highest score and lowest score of class:Max = ",max(t),"Min = ",min(t))
print("Count of student who were absent for the test: ",absent)

#Frequency
freq={}
for i in t:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
key=[]
value=[]
for i in freq:
    key.append(i)
    value.append(freq[i])

print("Marks with high frequency are:",key[value.index(max(value))],"with frequency of:",max(value))

