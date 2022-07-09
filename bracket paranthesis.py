# check for bracket paranthesis in python
# print balanced or not
string=input()
open=["(","{","["]
close=[")","}","]"]
stack=[]
for i in range(len(string)):
    if string[i] in open:
        stack.append(string[i])
    if string[i] in close:
        m=close.index(string[i])
        n=open.index(stack[-1])
        if m==n:
            stack.pop()
if len(stack)==0:
    print("Balanced")
else:
    print("Unbalanced")