a = int(input("Saissisez une longueur a:"))
b = int(input("Saissisez une longueur b:"))
c = int(input("Saissisez une longueur c:"))

if a<b+c and b<c+a and c<b+a:
    print ("Le triangle est possible !")
elif a==b==c :
    print ("Le triangle est possible !")
    print ("Le triangle est équilatéral ")
elif (a**b) or (b**c) or (c**a):
    print ("Le triangle est possible !")
    print ("Le triangle est rectangle")
elif a!=b!=c :
    print ("Le triangle est possible !")
    print ("Le triangle est isocéle")
else:
    print ("Nope !")