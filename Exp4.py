#FDS EXP:4

print ("\n1.Linear search\n2.Binary search\n3.Sentinal search\n4.Fibonacci search\n5.Exit")

#Linear
def linear():
    n=int(input("Enter the Student count: "))
    print("Enter the %i stuent roll no's"%(n))
    fds=list(map(int,input().split()))
    print("Student roll no's are",fds)
    x=int(input("Enter the roll no to be sreach: "))
    flag=0
    for i in range(n):
        if(x==fds[i]):
            flag=1
            print("Roll no",x,"attend tranining program")
            break;
    if(flag==0):
        print("Roll no",x,"not attend tranining program")

#Sentinal
def sentinal():
    n=int(input("Enter the Student count: "))
    print("Enter the %i stuent roll no's"%(n))
    fds=list(map(int,input().split()))
    print("Student roll no's are:",fds)
    x=int(input("Enter the roll no to be sreach: "))
    last= fds[n-1]
    fds[n-1]=x
    i=0
    while(fds[i]!=x):
        i=i+1
        fds[n-1]=last
        if((i<n-1)or(fds[n-1]==x)):
           print("Roll no",x,"attend tranining program")
        else:
            print("Roll no",x,"not attend tranining program")

#Binary
def binary():
    n=int(input("Enter the Student count: "))
    print("Enter the %i stuent roll no's"%(n))
    fds=list(map(int,input().split()))
    print("Student roll no's are",fds)
    x=int(input("Enter the roll no to be sreach: "))
    flag=0
    l=0
    h=n-1
    while(l<=h):
        m=(l+h)
        if(x==fds[m]):
            flag=1
            print("Roll no",x,"attend tranining program")
            break;
        elif(x<fds[m]):
            h=m-1
        else:
            l=m+1
            if(flag==0):
                print("Roll no",x,"not attend tranining program")

#Fibonacci
def fibonacci():
    n=int(input("Enter the Student count: "))
    print("Enter the %i stuent roll no's"%(n))
    fds=list(map(int,input().split()))
    print("Student roll no's are",fds)
    x=int(input("Enter the roll no to be sreach: "))
    m1=1
    m2=0
    m=m1+m2
    while(m<n):
        m2=m1
        m1=m
        m=m1+m2
        flag=0
        offset = -1
    while(m>1):
        i=offset+m2
        if(fds[i]<x):
            m=m1
            m1=m2
            m2=m-m1
            offset=i
        elif(fds[i]>x):
            m=m2
            m1=m1-m
            m2=m-m1
        else:
            flag=1
            print("Roll no",x,"attend tranining program")
            break;
    if(flag==0):
        print("Roll no",x,"not attend tranining program")
        
while True:
    ch=int(input("Enter your choice: "))
    if(ch==1):
        linear()
    elif(ch==2):
        binary()
    elif(ch==3):
        sentinal()
    elif(ch==4):
        fibonacci()
    elif(ch==5):
        break