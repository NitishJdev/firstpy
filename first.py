#ask user their choice of operation
"""print('select operation')
print('1.addition')
print('2.subtraction')
print('3.division')
print('4.multiplication')
choice=input('Enter your choice:  ')
#ask user to enter number to operation with that operation
num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
#conditional functioning
if choice == '1':
    print(num1,'+',num2,'=',num1+num2)
elif choice == '2':
        print(num1, '-', num2, '=', num1 - num2)
elif choice == '3':
        print(num1, '/', num2, '=', num1 / num2)
elif choice == '4':
        print(num1, 'x', num2, '=', num1 * num2)
else:
    print('Invalid Input')"""
#import csv

"""big=0
small=None
fork=0
some=0
count=0
print('before',big)
for thing in [-25,-99,0,9,12,13,54,6,78,98]:
    count=count+1
    some=some+thing
    print(count,some,thing)
    print('before')
    fork=fork+1
    print(fork,thing)
    fork=fork+thing
    print(fork,thing)
    fork=fork-thing
    print(fork,thing)
    if thing>big:
        big=thing
    print(big,thing)
    if small is None:
        small=thing
    elif thing < small:
        small=thing
    print(small,thing)
print('big',big)
print('small',small)
print('count',fork)
print('average', count,some,some/count)

max=int(input('enter max value: '))
for x in range(1,max+1):
    if (x%2==0):
     print('even number',x)
    elif (x%2!=0):
        print('odd number',x)
    else:
        print('operation failed')
i=1
num=int(input('Enter any number: '))
for i in range(1,11):
    print("%d x %d = %d"%(num,i,num*i))

n=int(input('Enter number of rows you want to print: '))
i,j=0,0
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print('*',end="")
i=1
num=int(input('Enter any number: '))
while 1:
    i=1
    while i<=10:
        print('%d x %d = %d'%(num,i,num*i))
        i=i+1
    choice=int(input('Do you want to continue for next table?, press 0 for no: '))
    if choice==0:
        break"""

    #num=num+1

"""def sum(a,b):
    return a+b


a=int(input('Enter a: '))
b=int(input('Enter b: '))
print(sum(a,b))"""

"""def si(p,t,r):
    return (p*t*r)/100
p=float(input('Enter the principal amount: '))
r=float(input('Enter the rate of interest: '))
t=float(input('Enter the time in years: '))
print('Simple Interest: ',si(p,r,t,))"""

'''class student:
    idee=0
    name=''

    def __init__(self,idee,name):
        self.idee=idee
        self.name=name

student=student(102,'soham')
print(student.idee)
print(student.name)
setattr(student,'email','soham@gmail.com')
print(student.email)'''

"""str='lovethewayyoulie'
abc=sorted(str)
print(abc)"""

"""file=open('/home/nitish/Desktop/py.txt','r')

print('the byte pointer is at: ',file.tell())
content=file.read()
print('after reading, file pointer at: ',file.tell())"""

"""import calc
a=int(input('enter the first value: '))
b=int(input('enter the second value: '))
print('sum: ',calc.summation(a,b))
print('multi: ',calc.multiplication(a,b))
print('division: ',calc.division(a,b))"""

"""try:
    a=int(input('Enter a: '))
    b=int(input('Enter b: '))
    c=a/b
    print('a/b= %d'%c)
except Exception:
    print("can't divide with by zero")
else:
    print('operaiton failed')"""

"""class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name

    def display(self):
        print('ID: %d \nName: %s'%(self.id,self.name))
emp1=Employee('John',112)
emp2=Employee('vicky',111)

emp1.display()
emp2.display()"""

"""class animal:
    def speak(self):
        print('animal speaking')
class dog(animal):
    def bark(self):
        print('bow wow')
d=dog()
d.bark()
d.speak()"""
"""import smtplib
smtpObj=smtplib.SMTP('gmail.com', 587)
smtpObj.sendmail()"""

"""sender_mail='nitish.joshi89@gmail.com'
receiver_mail='joshinitish@yahoo.com'
#message= 
From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message
%(sender_mail,receiver_mail
try:
    smtpObj=smtplib.SMTP('nitish')
    smtpObj.sendmail(sender_mail,receiver_mail,message)
    print('successfully sent')
except:
    print('error occured')"""
#from csv import reader

"""with open('/home/nitish/Desktop/pyt.txt') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count==0:
            print(f'Column names are {",".join(row)}')
            line_count+=1"""
"""import pandas
df=pandas.read_csv('/home/nitish/Desktop/pyt.csv')
print(df)"""

"""import csv

with open('/home/nitish/Desktop/pyt.csv') as csvfile:
    fieldnames=['first_name','last_name','Rank']
    writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})
    writer.writerow({'Rank': 'A', 'first_name': 'Smith', 'last_name': 'Rodriguez'})
    writer.writerow({'Rank': 'C', 'first_name': 'Tom', 'last_name': 'smith'})
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Rank': 'A', 'first_name': 'Alex', 'last_name': 'Tim'})

print('writing complete')"""


#import xlrd

"""loc=('/media/nitish/Nitish/D Drive/Hiral documents/Pagar Slip Annual 2018-19.xlsx')
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
sheet.cell_value(1,13)"""




