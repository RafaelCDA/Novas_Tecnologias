v = int(input())

if v <  0 or v > 1000000:
 raise Exception("Presentation Error")

ced = [100,50,20,10,5,2,1]
print(v)
for cedula in ced:
 qtd = v//cedula
 v = v%cedula
 print("{} nota(s) de R$ {},00".format(qtd,cedula))
 