import re

fin = open("aoc5.in", "r")
fout = open("aoc5.txt", "w")

for line in fin.readlines():
  i = 512
  n = 0

  for c in line:
    if c == 'B' or c == 'R':
      n += i
    i = i >> 1
    
  fout.write(f"{n}\n")
  
fout.write("0\n")

