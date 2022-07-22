#l1=['m','n']
#n=3
#for i in range(1,n+1):
 #   print('m',i)
num=int(input("enter the number to check"))
if 1200<num<3000 and num%8==0 and num%6==0:
      print("number is divisible by 8 and 6")
elif 1200<num<3000 and num%4==0:
      print("number is divisible by4")
elif 1200<num<3000 and num%8!=0 and num%6!=0 and num%4!=0:
    print("number is not divisible by 4,6 and 8")
else:
    print("enter a valid number")