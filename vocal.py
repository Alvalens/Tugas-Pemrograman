x = input()
y = 'a','i','u','e','o','A','I','U','E','O'

for i in x:
    if i in y:
        x = x.replace(i,'')
        
print(x)
