#!/usr/bin/python3.10

names = ["Jimy","John","Jamesan"]
print(names)

names[0]="Dimi"
print()
print(names[0])
print(names[1])
print(names[2])

print()
print(names[0:2])

#empty row
print()
name=[1,2,3,4,5,6,7]
name.append(8)
#name.insert(2,33333)
#name.insert(5,55555)
print(name)
print(len(name))

#empty row
print()
name.remove(2)
name.remove(5)
print(name)
print(len(name))
