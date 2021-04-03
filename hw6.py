# Take inputs from input file:
    
input_file = open("crime_scene.txt")
lines = input_file.readlines()
input_file.close()


# Preprocess input lines

def getRidOffNewLineChars(listLines, index):
    if index==len(listLines):
        return
    listLines[index] = listLines[index].rstrip("\n")
    getRidOffNewLineChars(listLines,index+1)

getRidOffNewLineChars(lines,0)
# print(lines)



# Determine W,T and N

weight_limit = int(lines[0].split()[0])
time_limit = int(lines[0].split()[1])
numberOfEvidences = int(lines[1])
# print("weight limit: {}".format(weight_limit),"time limit: {}".format(time_limit),"numberOfEvidences: {}".format(numberOfEvidences),sep="\n")


# Sorting Function:
def my_bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if (lst[j]>lst[j+1]):
                #swap lst[j] with lst[j+1]
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst






#  Preprocess listOfEvidences

listOfEvidences = lines[2:]

def preProcessEvidences(listOfEvidences,index):  
    if index == len(listOfEvidences):
        return
    listOfEvidences[index] = listOfEvidences[index].split()
    preProcessEvidences(listOfEvidences,index+1)
preProcessEvidences(listOfEvidences,0)


def preProcessEvidences2(listOfEvidences,index):
    if index==len(listOfEvidences):
        return
    listOfEvidences[index][0] = int(listOfEvidences[index][0])
    listOfEvidences[index][1] = int(listOfEvidences[index][1])
    listOfEvidences[index][2] = int(listOfEvidences[index][2])
    listOfEvidences[index][3] = int(listOfEvidences[index][3])
    preProcessEvidences2(listOfEvidences,index+1)
preProcessEvidences2(listOfEvidences,0)
# print(listOfEvidences)





# Solution Part 1 (Weight only):
    
def solution_part1(weight_limit, i):
    if i == numberOfEvidences:
        return 0 , []
    
    if weight_limit - listOfEvidences[i][1] >= 0:
        collected_value , collected_list = solution_part1(weight_limit-listOfEvidences[i][1], i+1)
        collected_value += listOfEvidences[i][3]
        collected_list.append(listOfEvidences[i])
        
    else:
        collected_value = 0
        collected_list = []
        
    collected_value_dont_take , collected_list_dont_take = solution_part1(weight_limit, i+1)
        

    if collected_value>collected_value_dont_take:
        return collected_value, collected_list
    
    else:
        return collected_value_dont_take, collected_list_dont_take

# print(solution_part1(weight_limit, 0))
solution_part1_tuple = solution_part1(weight_limit, 0)

solution_part1_ids = []
def f1(lista,index):
    global solution_part1_ids
    if index==len(lista):
        return
    solution_part1_ids.append(lista[index][0])
    f1(lista,index+1)

f1(solution_part1_tuple[1],0)
solution_part1_ids = my_bubble_sort(solution_part1_ids)
# print(solution_part1_ids)

file1 = open("solution_part1.txt","w")
file1.write(str(solution_part1_tuple[0])+"\n")
for i in solution_part1_ids:
    if solution_part1_ids.index(i)!=len(solution_part1_ids)-1:
        file1.write(str(i)+" ")
    else:
        file1.write(str(i))
file1.close()






# Solution Part 2 (Time only):
    
def solution_part2(time_limit, i):
    if i == numberOfEvidences:
        return 0 , []
    
    if time_limit - listOfEvidences[i][2] >= 0:
        collected_value , collected_list = solution_part2(time_limit-listOfEvidences[i][2], i+1)
        collected_value += listOfEvidences[i][3]
        collected_list.append(listOfEvidences[i])
        
    else:
        collected_value = 0
        collected_list = []
        
    collected_value_dont_take , collected_list_dont_take = solution_part2(time_limit, i+1)
        

    if collected_value>collected_value_dont_take:
        return collected_value, collected_list
    
    else:
        return collected_value_dont_take, collected_list_dont_take

# print(solution_part2(time_limit, 0))
solution_part2_tuple = solution_part2(time_limit, 0)

solution_part2_ids = []
def f2(lista,index):
    global solution_part2_ids
    if index==len(lista):
        return
    solution_part2_ids.append(lista[index][0])
    f2(lista,index+1)

f2(solution_part2_tuple[1],0)
solution_part2_ids = my_bubble_sort(solution_part2_ids)
# print(solution_part2_ids)

file2 = open("solution_part2.txt","w")
file2.write(str(solution_part2_tuple[0])+"\n")
for i in solution_part2_ids:
    if solution_part2_ids.index(i)!=len(solution_part2_ids)-1:
        file2.write(str(i)+" ")
    else:
        file2.write(str(i))
file2.close()






# Solution Part 3 (Final Solution):

def solution_part3(weight_limit, time_limit, i):
    if i == numberOfEvidences:
        return 0, []
    
    if weight_limit-listOfEvidences[i][1] >= 0 and time_limit-listOfEvidences[i][2] >= 0:
        collected_value , collected_list = solution_part3(weight_limit-listOfEvidences[i][1], time_limit-listOfEvidences[i][2], i+1)
        collected_value += listOfEvidences[i][3]
        collected_list.append(listOfEvidences[i])
        
    else:
        collected_value = 0
        collected_list = []


    collected_value_dont_take , collected_list_dont_take = solution_part3(weight_limit, time_limit, i+1)
    
    if collected_value>collected_value_dont_take:
        return collected_value, collected_list
    
    else:
        return collected_value_dont_take, collected_list_dont_take



# print(solution_part3(weight_limit, time_limit, 0))
solution_part3_tuple = solution_part3(weight_limit, time_limit, 0)


solution_part3_ids = []
def f3(lista,index):
    global solution_part3_ids
    if index==len(lista):
        return
    solution_part3_ids.append(lista[index][0])
    f3(lista,index+1)




f3(solution_part3_tuple[1],0)
solution_part3_ids = my_bubble_sort(solution_part3_ids)
# print(solution_part3_ids)

file3 = open("solution_part3.txt","w")
file3.write(str(solution_part3_tuple[0])+"\n")
for i in solution_part3_ids:
    if solution_part3_ids.index(i)!=len(solution_part3_ids)-1:
        file3.write(str(i)+" ")
    else:
        file3.write(str(i))
file3.close()
