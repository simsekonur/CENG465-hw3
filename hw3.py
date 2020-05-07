#These two function will give you a list of items as list 
def giveMeFirstChain(nameOfTheFile):
    generalList = []
    for line in open(nameOfTheFile):
        lst = line.split()
        if (lst[0]=='ATOM' and lst[4]=='A'): # I'm talking about first chain
            lst[6] = float (lst[6])
            lst[7] = float (lst[7])
            lst[8] = float (lst[8])
            if(lst[2]=='CB' or (lst[2]=='CA' and lst[3]=='GLY')):
                generalList.append(lst)
    return generalList

def giveMeSecondChain(nameOfTheFile):
    generalList = []
    for line in open(nameOfTheFile):
        lst = line.split()
        if (lst[0]=='ATOM' and lst[4]=='B'): # I'm talking about second chain
            lst[6] = float (lst[6])
            lst[7] = float (lst[7])
            lst[8] = float (lst[8])
            if(lst[2]=='CB' or (lst[2]=='CA' and lst[3]=='GLY')):
                generalList.append(lst)
    return generalList

def eucDis(lst1,lst2):
    distance = 0
    distance = ((lst1[6] - lst2[6])**2 + (lst1[7] - lst2[7])**2 + (lst1[8] - lst2[8])**2) ** 0.5
    return distance 

def printGuys (lst1,lst2,groupNo):
    print "Group " +str (groupNo) + ": " + lst1[3]+"("+lst1[5]+")"+"-"+ lst2[3]+"("+lst2[5]+")"

firstFile = '4uap.pdb'
firstChain = giveMeFirstChain(firstFile)
secondChain = giveMeSecondChain(firstFile)
record = 0
groupNumbers=1

#recordu buldurmaca 
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            record+=1
#print ettirmece          
print("There are " +str(record)+" interacting pairs.")
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            printGuys(firstChain[i],secondChain[j],1)
print("Number of groups = " + str(groupNumbers))            

#########################################################

firstFile = '2bti.pdb'
firstChain = giveMeFirstChain(firstFile)
secondChain = giveMeSecondChain(firstFile)
record = 0
groupNumbers=1

#recordu buldurmaca 
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            record+=1
#print ettirmece          
print("There are " +str(record)+" interacting pairs.")
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            printGuys(firstChain[i],secondChain[j],1)
print("Number of groups = " + str(groupNumbers))  

#########################################################

firstFile = '3r0a.pdb'
firstChain = giveMeFirstChain(firstFile)
secondChain = giveMeSecondChain(firstFile)
record = 0
groupNumbers=1

#recordu buldurmaca 
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            record+=1
#print ettirmece          
print("There are " +str(record)+" interacting pairs.")
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            printGuys(firstChain[i],secondChain[j],1)
print("Number of groups = " + str(groupNumbers))  

############################################################

firstFile = '6k62.pdb'
firstChain = giveMeFirstChain(firstFile)
secondChain = giveMeSecondChain(firstFile)
record = 0
groupNumbers=1

#recordu buldurmaca 
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            record+=1
#print ettirmece          
print("There are " +str(record)+" interacting pairs.")
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            printGuys(firstChain[i],secondChain[j],1)
print("Number of groups = " + str(groupNumbers))  

##########################################################

firstFile = '6k97.pdb'
firstChain = giveMeFirstChain(firstFile)
secondChain = giveMeSecondChain(firstFile)
record = 0
groupNumbers=1

#recordu buldurmaca 
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            record+=1
#print ettirmece          
print("There are " +str(record)+" interacting pairs.")
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            printGuys(firstChain[i],secondChain[j],1)
print("Number of groups = " + str(groupNumbers))  

#######################################################

firstFile = '6lac.pdb'
firstChain = giveMeFirstChain(firstFile)
secondChain = giveMeSecondChain(firstFile)
record = 0
groupNumbers=1

#recordu buldurmaca 
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            record+=1
#print ettirmece          
print("There are " +str(record)+" interacting pairs.")
for i in range(0,len(firstChain)):
    for j in range(0,len(secondChain)):
        if(eucDis(firstChain[i],secondChain[j]) < 8.0 and firstChain[i][1] != secondChain[j][1]):
            printGuys(firstChain[i],secondChain[j],1)
print("Number of groups = " + str(groupNumbers))  

