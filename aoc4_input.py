import re

fin = open("aoc4.in", "r")
fout = open("aoc4.txt", "w")

key_idx = {'ecl':1, 'pid':2, 'eyr':3, 'hcl':4, 'byr':5, 'iyr':6, 'cid':7, 'hgt':8}

for line in fin.readlines():
  kvs = line.split()
  
  if len(kvs) == 0:
    fout.write("0\n")
    continue
    
  for kv in kvs:
    key, value = kv.split(':')
    fout.write("{}\n".format(key_idx[key]))
    try:
      intval = int(value)
      if intval < 1 or intval > 2047: raise ValueError()
      fout.write("{}\n".format(intval))
    except ValueError:
      for c in value:
        fout.write("{}\n".format(ord(c)))
    
    fout.write("0\n")
  
fout.write("0\n")

