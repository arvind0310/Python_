s=input()
if 'EF' in s:
    s1=s.replace("EF","")
    if 'G' in s1:
        print(s1.replace('G',""))
    else:
        print(s1)
else:
    if 'G' in s:
        print(s.replace('G',""))
