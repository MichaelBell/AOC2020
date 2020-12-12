import re

fin = open("aoc8.in", "r")
fout = open("aoc8.txt", "w")

instr_map = { 'acc':1, 'jmp':2, 'nop':3 }

for line in fin.readlines():
  instr, num = line.split()
  
  fout.write("{}\n{}\n".format(instr_map[instr], num))
  
fout.write("0\n")
