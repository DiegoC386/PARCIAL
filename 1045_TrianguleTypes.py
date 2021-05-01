"""
Read 3 double numbers (A, B and C) representing the sides of a triangle and arrange them in decreasing order,
so that the side A is the biggest of the three sides. Next, determine the type of triangle that they can make,
based on the following cases always writing an appropriate message:
if A ≥ B + C, write the message: NAO FORMA TRIANGULO
if A2 = B2 + C2, write the message: TRIANGULO RETANGULO
if A2 > B2 + C2, write the message: TRIANGULO OBTUSANGULO
if A2 < B2 + C2, write the message: TRIANGULO ACUTANGULO
if the three sides are the same size, write the message: TRIANGULO EQUILATERO
if only two sides are the same and the third one is different, write the message: TRIANGULO ISOSCELES
"""
triangulo=input("")
(a,b,c)=triangulo.split(" ")
a=float(a)
b=float(b)
c=float(c)
if(a==b==c):
	A=a
	B=b
	C=c
elif(a>=b and a>=c and b>=c):
	A=a
	B=b
	C=c
elif(a>=b and a>=c and c>=b):
	A=a
	B=c
	C=b
elif(b>=a and b>=c and a>=c):
	A=b
	B=a
	C=c
elif(b>=a and b>=c and c>=a):
	A=b
	B=c
	C=a
elif(c>=a and c>=b and a>=b):
	A=c
	B=a
	C=b
elif(c>=a and c>=b and b>=a):
	A=c
	B=b
	C=a
if(A>=B+C):
	print("NAO FORMA TRIANGULO")
else:
	if(A**2==B**2+C**2):
		print("TRIANGULO RETANGULO")
	if(A**2>(B**2+C**2)):
		print("TRIANGULO OBTUSANGULO")
	if(A**2<B**2+C**2):
		print("TRIANGULO ACUTANGULO")
	if(A==B==C):
		print("TRIANGULO EQUILATERO")
	if(A==B and A!=C or B==C and B!=A or C==A and C!=B):
		print("TRIANGULO ISOSCELES")