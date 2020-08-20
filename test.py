Output=[]
li1=[10,20,30,60,40]
li2=[20,10,40,50,30]
for i in range(len(li1)):
   if li1[i]>li2[i]:
      Output.append(li1[i]-li2[i])
   else:
      Output.append(li1[i])

print('original list are:')
print(li1)
print(li2)

print("\noutput list are:")
print(Output)