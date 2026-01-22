import math
print('                                ','WELCONE TO MY PROJECT')
print("=================================🤖SCIENTIFIC CALCULATOR🤖====================================")
while True:
 print('What you wants to check \n1.simple calculation[+,-,*,/]\n2.advance logic[sqrt,cube,fact,floor]\n3.trigometric[sin,cos,tan,cot,sec,cosec]\n4.log[logx,log10x,exponitial,antilog,logbase]')
 op=int(input('Enter choice='))
 if op == 1:
    print('IN THIS U CAN DO ADDICTION,SUBTRACTION,DIVID,MULTIPILE')
    var1=int(input('enter a='))
    var2=int(input('enter b='))
    print('select \n1.add\n2.sub\n3.divi\n4.mul')
    p=int(input('Enter choice'))
    if p==1:
        print('solution=',var1 + var2)
    elif p==2:
        print('solution=',var1 -var2)
    elif p==3:
        print('solution=',var1/var2)
    elif p==4:
        print('solution=',var1 * var2)
 elif op ==2:
    a=float(input('enter num='))
    print('select 1.square,2.factorial,3.cube,4.floor')
    op=int(input('enter choice='))
    if op == 1:
        print(math.sqrt(a),'=',a)
    elif op == 2:
        o=int(a)
        print(math.factorial(o),'=',a)
    elif op == 3:
        print(a ** 3,'=',a)
    elif op == 4:
        print(math.floor(a),'=',a)
 elif op ==3:
    print('TRIGNOMETRIC SECTION U CAN FIND THE RADIAN')
    a=int(input('enter degree='))
    b=math.radians(a)
    print('choose which find like sin ,cos,tan,sec,cosec,cot')
    op=input('enter trigo =')
    if op =='sin':
        print(math.sin(b))
    elif op =='cos':
        print(math.cos(b))
    elif op =="tan":
        print(math.tan(b))
    elif op == "sec":
        c=1/math.cos(b)
        print(c)
    elif op == "cosec":
        print(1/math.sin(b))
    elif op == "cot":
        print(1/math.tan(b))
    else:
        print('Yet not available features')
  
 elif op == 4:
     print('select log10,log,log_base,antilog,exp ')
     o=input('enter selection=')
     if o == 'log10':
         x=float(input('enter x='))
         print(math.log10(x),'=',x)
     elif o =='log':
         x=float(input('enter x='))
         print(math.log(x),'=',x)
     elif o == " log_base":
         x=float(input('enter x='))
         b=float(input('enter base='))
         print(math.log(x)/math.log(b))
     elif o == 'antilog':
         x=float(input('enter x='))
         print(10 ** x)
     elif o == "exp":
         x=float(input('enter x='))
         print(math.exp(x),'=',x)
     else:
         print('Yet features not available')
 else:
     print('invalid choice!!,try again')