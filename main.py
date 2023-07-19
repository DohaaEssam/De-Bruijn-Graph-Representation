import re

def singleInput():
  list1=[]
  list2=[]

  single_read=open("test.txt", "r")
  kemer=single_read.readlines()
  kemer=15

  for line in single_read.readlines():
     list1.append(line[0:kemer-1])
     list2.append(line[1:kemer])
  startpoint = [x for x in list1 + list2 if x in list1 and x not in list2]
  endpoint = [x for x in list1 + list2 if x not in list1 and x in list2]
  Eulerian_path={}
  Eulerian_path = {list1[i]: list2[i] for i in range(len(list1))}
  for start_key, j in Eulerian_path.items():
    sp=''.join(map(str,startpoint))
    if sp == start_key:
      break
  for i, end_key in Eulerian_path.items():
    ep=''.join(map(str,endpoint))
    if ep == end_key:
      break

  path_list=[]
  path_list.append(sp)
  print(path_list)
  for index in range(len(Eulerian_path)):
    key = path_list[-1]
    print(path_list)
    print(key)
    value = Eulerian_path[key]
    path_list.append(value)
  genome=""
  for i in range(len(path_list)):
    if i == 0:
      genome+=path_list[i]
    else:
      seq=path_list[i]
      genome+=seq[len(seq)-1]

  print("Eulrian Path:",path_list)
  print("Genome:",genome)

#singleInput()



def Pair_input():
  pair_read = open("ReadPairsInput.txt", "r")
  first_line = pair_read.readline()
  first_line_splitted = re.split('\s+', first_line)
  kemer = first_line_splitted[0]
  kemer = int(kemer)
  gaps = first_line_splitted[1]
  gaps = int(gaps)
  print("Kemer =", kemer, "Gaps=", gaps)
  list1 = []
  list2 = []
  for line in pair_read.readlines():
    # GACGCG -> ACCCGC
    list1.append(line[0:kemer - 1] + line[kemer + 1:(kemer * 2)])
    list2.append(line[1:kemer] + line[kemer + 2:(kemer * 2) + 1])
  startpoint = [x for x in list1 + list2 if x in list1 and x not in list2]
  endpoint = [x for x in list1 + list2 if x not in list1 and x in list2]
  Eulerian_path = {}
  Eulerian_path = {list1[i]: list2[i] for i in range(len(list1))}
  for start_key, j in Eulerian_path.items():
    sp = ''.join(map(str, startpoint))
    if sp == start_key:
      break
  for i, end_key in Eulerian_path.items():
    ep = ''.join(map(str, endpoint))
    if ep == end_key:
      break
  path_list = []
  path_list.append(sp)
  for index in range(len(Eulerian_path)):
    key = path_list[-1]
    value = Eulerian_path[key]
    path_list.append(value)
  print(path_list)
  Top_list = []
  Terminal_list_suffix = []
  Prefix_seq = ""
  Suffix_seq = ""
  for i in range(len(path_list)):
    temp = path_list[i]
    Top_list.append(temp[0:kemer - 1])
    Terminal_list_suffix.append(temp[kemer - 1:len(temp)])
  for i in range(len(Top_list)):
    if i == len(Top_list) - 1:
      Prefix_seq += Top_list[i]
      Suffix_seq += Terminal_list_suffix[i]
    else:
      temp = Top_list[i]
      Prefix_seq += temp[0]
      temp2 = Terminal_list_suffix[i]
      Suffix_seq += temp2[0]

  print("Prefix", Prefix_seq)
  print("Suffix", Suffix_seq)
  kd = kemer + gaps
  new_suffix = Suffix_seq[(len(Suffix_seq) - kd):len(Suffix_seq)]
  genome = Prefix_seq + new_suffix
  print("Genome:", genome)

Pair_input()