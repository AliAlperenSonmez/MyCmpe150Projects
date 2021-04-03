
x = int(input())
y = int(input())
g = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
laststarindex = x-1
firststarindex = 0
counter = 0
score = 0
is_x_zero = False

table = []


# adjust the table
for i in range(x):
    table.append(list("*"*y))

for i in range(g):
    table.append(list(" "*y))
    
if y%2!=0:
    table.append(list(" "*int((y-1)/2)+"@"+" "*int((y-1)/2)))
else:
    table.append(list(" "*int((y/2)-1)+"@"+" "*int(y/2)))
    
    
# if x == 0 
if x == 0:
    print("YOU WON!")
    for i in table:
        for j in i:
            print(j,end = "")
        print()
    print("-"*72)
    print("YOUR SCORE: {}".format(score))
    is_x_zero = True

# print the initial table
if is_x_zero==False:
    for i in table:
        for j in i:
            print(j,end="")
        print()
    print("-"*72)


while True:
    if is_x_zero==True:
        break
    else:
        pass
    
    # Choose an action 
    action = input("Choose your action!\n")
    action = action.lower()
    counter+=1
    
    
    # Exit action:
    if action == "exit":
        for i in table:
            for j in i:
                print(j,end="")
            print()
        print("-"*72)
        print("YOUR SCORE: {}".format(score))
        break
    
    
    # Left action:
    if action == "left":
        indexAt = table[-1].index("@")
        if indexAt==0:
            pass
        
        else:
            table[-1][indexAt]= " "
            table[-1][indexAt-1]= "@"
    
    
    # Right action:
    if action == "right":
        indexAt = table[-1].index("@")
        if indexAt==y-1:
            pass
        
        else:
            table[-1][indexAt]= " "
            table[-1][indexAt+1]= "@"
    
    
    # Fire action:
    if action=="fire":
        indexAt = table[-1].index("@")
        for indexfire in range(1,x+g+1):
            if table[x+g-indexfire][indexAt]==" ":
                table[x+g-indexfire][indexAt]="|"
                for i in table:
                    for j in i:
                        print(j,end="")
                    print()
                print("-"*72)
                table[x+g-indexfire][indexAt]=" "
            
            elif table[x+g-indexfire][indexAt]=="*":
                table[x+g-indexfire][indexAt]=" "
                score+=1
                break    
    
    # Yıldızlar bitti
    wonmu=3
    for i in table:
        for j in i:
            if j=="*":
                wonmu=False
                break
            else:
                wonmu=True
        if wonmu==False:
            break
        
        
    if wonmu==True:
        print("YOU WON!")
        for i in table:
            for j in i:
                print(j, end="")
            print()
        print("-" * 72)
        print("YOUR SCORE: {}".format(score))
        break
        
    
    # Bir sıra bitti
    if not "*" in table[laststarindex]:
        laststarindex-=1
    
    # Sayaç beşin katı oldu
    if counter%5==0 and counter!=0:
        if laststarindex!=len(table)-2:
            table.insert(firststarindex,list(" "*y))
            table.pop(len(table)-2)
            laststarindex+=1
            firststarindex+=1

        else:
            print("GAME OVER")
            for i in table:
                for j in i:
                    print(j,end="")
                print()
            print("-"*72)
            print("YOUR SCORE: {}".format(score))
            break
    
    # Tabloyu yazdır
    for i in table:
        for j in i:
            print(j,end="")
        print()
    print("-"*72)
    
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
