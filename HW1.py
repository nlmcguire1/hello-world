a = input("Enter a string")
outFile = open("prog.bf","w")
i = 0
while i < len(a):
  hx = ord(a[i])
  j = 0;
  while j < hx:
    outFile.write('+')
    j += 1
  i += 1
