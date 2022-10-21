s = str(input())

a = s.count('{') - s.count('}')
b = s.count('[') - s.count(']')
c = s.count('(') - s.count(')')

if a == 0 and b == 0 and c == 0:
    print("True")
else:
    print("False")

