# Nama : Alvalen Shafelbilyunazra
# NIM : 220535608548

#Var
# x = greeting
# z = money

x=input().replace(" ","").lower()
if(x[0:5]=='hello'):
    z=0
elif(x[0]=='h'):
    z=20
else:
    z=100

print ('$', z)
