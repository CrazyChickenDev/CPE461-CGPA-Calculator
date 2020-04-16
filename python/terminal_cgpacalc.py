#CGPA_Calculator
print('This program calculates the CGPA of 300 Level Computer Engineering Students')
print('Input your scores in the 1st Semester')
a = input('MTH 101= ')
a = float(a)
while a > 100 or a < 0:
    print('Please input a correct value')
    a = input('MTH 101= ')
    a = float(a)
b = input('CHM 101= ')
b = float(b)
while b >100 or b <0:
    print('Please input a correct value')
    b = input('CHM 101= ')
    b = float(b)
c = input('PHY 101= ')
c = float(c)
while c >100 or c <0:
    print('Please input a correct value')
    c = input('PHY 101= ')
    c = float(c)
d = input('PHY 107= ')
d = float(d)
while d >100 or d <0:
    print('Please input a correct value')
    d = input('PHY 107= ')
    d = float(d)
e = input('CHM 103= ')
e = float(e)
while e >100 or e <0:
    print('Please input a correct value')
    e = input('CHM 103= ')
    e = float(e)
f = input('TPD 101= ')
f = float(f)
while f >100 or f <0:
    print('Please input a correct value')
    f = input('TPD 101= ')
    f = float(f)
g = input('SER 001= ')
g = float(g)
while g >100 or g <0:
    print('Please input a correct value')
    g = input('SER 001= ')
    g = float(g)
scores = [a, b, c, d, e, f, g]
n = 0
points = [0, 0, 0, 0, 0, 0, 0]
while n <=6:
    if scores[n] >=70 and scores[n] <=100:
        points[n] = 5
    elif scores[n] >= 60 and scores[n] <=69:
        points[n] = 4
    elif scores[n] >= 50 and scores[n] <=59:
        points[n] = 3
    elif scores[n] >= 45 and scores[n] <=49:
        points[n] = 2
    elif scores[n] >= 40 and scores[n] <=44:
        points[n] = 1
    elif scores[n] >= 0 and scores[n] <=39:
        points[n] = 0
    n+=1
units = [5, 4, 4, 1, 1, 1, 0]
global totalpoints
totalpoints = [0, 0, 0, 0, 0, 0, 0]
c=0
while c<=6:
    totalpoints[c]=units[c]*points[c]
    c+=1
gpa=sum(totalpoints)/sum(units)
gpa=round(gpa, 2)
print('Your GPA for 1st Semester is ',gpa)

print('Input your scores in the 2nd Semester')
a1 = input('MTH 102= ')
a1 = float(a1)
while a1 > 100 or a1 < 0:
    print('Please input a correct value')
    a1 = input('MTH 102= ')
    a1 = float(a1)
b1 = input('CHM 102= ')
b1 = float(b1)
while b1 >100 or b1 <0:
    print('Please input a correct value')
    b1 = input('CHM 102= ')
    b1 = float(b1)
c1 = input('PHY 102= ')
c1 = float(c1)
while c1 >100 or c1 <0:
    print('Please input a correct value')
    c1 = input('PHY 102= ')
    c1 = float(c1)
d1 = input('PHY 108= ')
d1 = float(d1)
while d1 >100 or d1 <0:
    print('Please input a correct value')
    d1 = input('PHY 108= ')
    d1 = float(d1)
e1 = input('CHM 104= ')
e1 = float(e1)
while e1 >100 or e1 <0:
    print('Please input a correct value')
    e1 = input('CHM 104= ')
    e1 = float(e1)
f1 = input('MTH 104= ')
f1 = float(f1)
while f1 >100 or f1 <0:
    print('Please input a correct value')
    f1 = input('MTH 104= ')
    f1 = float(f1)
g1 = input('SER 001= ')
g1 = float(g1)
while g1 >100 or g1 <0:
    print('Please input a correct value')
    g1 = input('SER 001= ')
    g1 = float(g1)
scores1 = [a1, b1, c1, d1, e1, f1, g1]
n1 = 0
points1 = [0, 0, 0, 0, 0, 0, 0]
while n1 <=6:
    if scores1[n1] >=70 and scores1[n1] <=100:
        points1[n1] = 5
    elif scores1[n1] >= 60 and scores1[n1] <=69:
        points1[n1] = 4
    elif scores1[n1] >= 50 and scores1[n1] <=59:
        points1[n1] = 3
    elif scores1[n1] >= 45 and scores1[n1] <=49:
        points1[n1] = 2
    elif scores1[n1] >= 40 and scores1[n1] <=44:
        points1[n1] = 1
    elif scores1[n1] >= 0 and scores1[n1] <=39:
        points1[n1] = 0
    n1+=1
units1 = [5, 4, 4, 1, 1, 2, 0]
global totalpoints1
totalpoints1 = [0, 0, 0, 0, 0, 0, 0]
c1=0
while c1<=6:
    totalpoints1[c1]=units1[c1]*points1[c1]
    c1+=1
gpa1=sum(totalpoints1)/sum(units1)
gpa1= round(gpa1, 2)
print('Your GPA for 2nd Semester is ',gpa1)
cgpa=(sum(totalpoints)+sum(totalpoints1))/(sum(units)+sum(units1))
cgpa=round(cgpa, 2)
print('Your CGPA is ',cgpa)
if cgpa >=4.5 and cgpa <= 5.0:
    print('You are on First Class')
elif cgpa >=3.5 and cgpa <= 4.49:
    print('You are on Second Class Upper')
elif cgpa >=2.5 and cgpa <= 3.49:
    print('You are on Second Class Lower')
elif cgpa >=1.5 and cgpa <= 2.49:
    print('You are on Third Class')
