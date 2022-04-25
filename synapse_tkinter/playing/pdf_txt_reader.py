
import numpy as np

with open('test.txt','r') as infile:
    test = infile.read()

test2 = test.replace('\n','')
print(test2[:10000])

#counter = 0
#for t in test:
#    if counter < 100 : 
#        print(t)
#    else: break
#    counter += 1


#test3 = [t.strip().replace('-\n','').replace('\n',' ').replace('aldot','al.') for t in test.replace('al.','aldot').split('. ')]

#references = []
#intro = False
#for line in test3:

#    if 'INTRODUCTION' in line: intro=True
#    if 'ACKNOWLEDGMENTS' in line: into=False
#    if not intro: continue
#    div = line.split()
#    flag = np.array([True for item in div if item[:5].isdigit()])
#    if flag.any(): references += [line]

#for i in range(20):
#    print(i,')',references[i])


