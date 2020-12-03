

fin = open("aoc3.in", "r")
fout = open("aoc3.txt", "w")

for line in fin.readlines():
  i = 0
  n = 0
  for c in line:
    if c == '#':
      n += 1 << i
    i = i + 1
  
  fout.write("{}\n{}\n{}\n".format(n & 0x3ff, (n >> 10) & 0x3ff, n >> 20))
  
fout.write("-1\n")

