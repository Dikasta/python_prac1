#perform read paragraph from d1 txt  write paragraph d2 txt only one time
import  os
inp_file= 'd1'
op_file ='d2'
with open(inp_file,'r') as inp_fi:
    os.path.exists(op_file)
    os.remove(op_file)  # remove d2 txt file
    for line in inp_fi.readlines():
        with open(op_file,'a') as op_fi:  # create or open d2 txt file
            op_fi.write(line)


# print count of specific string from file d2
with open(op_file,'r') as in_fil:
    count = 0
    for line in in_fil.readlines():
        for itr in list(line.split(' ')):
            # paragraph convert in list using  'list(line.split(' '))' ['One', 'of', 'the', 'most', 'popular', 'ways', 'to', 'build', 'APIs', 'is', 'the', 'REST', 'build', 'architecture', 'style.\n']
            if 'build'== itr:
                count=count+1
    print(count)


#fsn