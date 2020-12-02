

fin = open("aoc2.in", "r")
fout = open("aoc2.txt", "w")

for line in fin.readlines():
  words = line.split()
  min, max = words[0].split("-")
  fout.write("{}\n{}\n".format(min, max))
  
  letter = words[1][0]
  lnum = ord(letter) - ord('a') + 1
  fout.write("{}\n".format(lnum))
  
  for l in words[2]:
    lnum = ord(l) - ord('a') + 1
    fout.write("{}\n".format(lnum))
  
  fout.write("0\n")
