import re

fin = open("aoc7.in", "r")
fout = open("aoc7.txt", "w")

bag_idx = {"shiny gold": 1}
bag_count = 2

def get_idx(name):
  global bag_count, bag_idx
  if name in bag_idx: 
    return bag_idx[name]
  bag_idx[name] = bag_count
  bag_count = bag_count + 1
  return bag_count - 1

for line in fin.readlines():
  src_name = re.match(r"([a-z]+ [a-z]+) bags contain", line).group(1)
  src_idx = get_idx(src_name)
  
  dests = re.findall(r"(\d) ([a-z]+ [a-z]+)", line)
  
  for dest in dests:
    dest_idx = get_idx(dest[1])
    fout.write("{}\n{}\n{}\n".format(src_idx, dest_idx, dest[0]))
    
  if len(dests) == 0:
    fout.write("{}\n-1\n1\n".format(src_idx))
  
fout.write("0\n")
