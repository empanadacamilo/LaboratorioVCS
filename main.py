a=float(input("ingrese el primer numero", ))
b=float(input("ingrese el segundo numero", ))
c=float(input("ingrese el tercer numero ", ))
d=(((b**2)-(4*a*c))**(1/2))
x1=(((-1*b)+(d**(1/2))))/2*a
x2=(((-1*b)-(d**(1/2))))/2*a
x3=(-1*b)/2*a
if d>0:
  print("los resultados ",x1 , x2, )
else:
  if d==0:
    print("el resultado es",x3)
  else:
   print("el resutado no existe")
