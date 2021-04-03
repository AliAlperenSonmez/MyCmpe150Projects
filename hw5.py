import re
import sys


# Check numbervariable ve dogru


# Read the input file
filer = open("calc.in")
lines = filer.readlines()
filer.close()



# Get rid of empty lines
while "\n" in lines:
    lines.remove("\n")





# Get rid of white spaces an new line characters
lines = [i.lstrip().rstrip().rstrip("\n") for i in lines]





# Check if necessary lines exist
# print("----------")
if lines[0]!="AnaDegiskenler" or not ("YeniDegiskenler" in lines) or not ("Sonuc" in lines):
    filew = open("calc.out","w")
    filew.write("Dont Let Me Down")
    filew.close()
    sys.exit()    






# Define indexes
indexYeni = lines.index("YeniDegiskenler")
indexSonuc = lines.index("Sonuc")






#  Check if indexes are in the correct order
# print("----------")
if indexSonuc<indexYeni:
    filew = open("calc.out","w")
    filew.write("Dont Let Me Down")
    filew.close()
    sys.exit()







# Check if there are invalid white spaces in anavalues
unvalidDigitPattern = "(\d \.\d)|(\d \. \d)|(\d\. \d)"
# print("----------")
for i in lines[1:indexYeni]:
    if re.findall(unvalidDigitPattern,i):
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()





# Preprocess anadegiskenler
AnaDegiskenler = [i.split() for i in lines[1:indexYeni]]

for i in AnaDegiskenler:
    if len(i)==6:
        indexi = AnaDegiskenler.index(i)
        i[2]=i[2]+i[3]+i[4]
        i.pop(3)
        i.pop(3)
        AnaDegiskenler[indexi]=i
# print(AnaDegiskenler)





#  Check if AnaDegiskenler have correct number of items
# print("----------")
for i in AnaDegiskenler:
    if len(i)<4 or len(i)>6 or len(i)==5:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()




# Define AnaVariables:
AnaVariables = [i[0] for i in AnaDegiskenler]
# print(AnaVariables)
# print("----------")
for i in AnaVariables:
    if AnaVariables.count(i)>1:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()



AnaVariablesRegex = ""
for i in AnaVariables:
    AnaVariablesRegex+="^"+i+"$|"
    
    
AnaVariablesRegex = AnaVariablesRegex.rstrip("|")
# print(AnaVariablesRegex,sep="\n\n")



# print(AnaVariables)

# Set patterns
variables = [i for i in AnaVariables]

numbers = "sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz"

keywords = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sifir', 'bir', 'iki', 'uc', 'dort', 'bes', 'alti', 'yedi', 'sekiz', 'dokuz', 'dogru', 'yanlis', '+', '-', '*', 'arti', 'eksi', 'carpi', 've', 'veya', '(', ')', 'ac-parantez', 'kapa-parantez', 'AnaDegiskenler', 'YeniDegiskenler', 'Sonuc', 'degeri', 'olsun', 'nokta']

PatternVariable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

anaPatternValue = "^\d$|^\d\.\d$|^sifir$|^bir$|^iki$|^dogru$|^yanlis$|^uc$|^dort$|^bes$|^alti$|^yedi$|^sekiz$|^dokuz$|^sifirnoktasifir$|^sifirnoktabir$|^sifirnoktaiki$|^sifirnoktauc$|^sifirnoktadort$|^sifirnoktabes$|^sifirnoktaalti$|^sifirnoktayedi$|^sifirnoktasekiz$|^sifirnoktadokuz$|^birnoktasifir$|^birnoktabir$|^birnoktaiki$|^birnoktauc$|^birnoktadort$|^birnoktabes$|^birnoktaalti$|^birnoktayedi$|^birnoktasekiz$|^birnoktadokuz$|^ikinoktasifir$|^ikinoktabir$|^ikinoktaiki$|^ikinoktauc$|^ikinoktadort$|^ikinoktabes$|^ikinoktaalti$|^ikinoktayedi$|^ikinoktasekiz$|^ikinoktadokuz$|^ucnoktasifir$|^ucnoktabir$|^ucnoktaiki$|^ucnoktauc$|^ucnoktadort$|^ucnoktabes$|^ucnoktaalti$|^ucnoktayedi$|^ucnoktasekiz$|^ucnoktadokuz$|^dortnoktasifir$|^dortnoktabir$|^dortnoktaiki$|^dortnoktauc$|^dortnoktadort$|^dortnoktabes$|^dortnoktaalti$|^dortnoktayedi$|^dortnoktasekiz$|^dortnoktadokuz$|^besnoktasifir$|^besnoktabir$|^besnoktaiki$|^besnoktauc$|^besnoktadort$|^besnoktabes$|^besnoktaalti$|^besnoktayedi$|^besnoktasekiz$|^besnoktadokuz$|^altinoktasifir$|^altinoktabir$|^altinoktaiki$|^altinoktauc$|^altinoktadort$|^altinoktabes$|^altinoktaalti$|^altinoktayedi$|^altinoktasekiz$|^altinoktadokuz$|^yedinoktasifir$|^yedinoktabir$|^yedinoktaiki$|^yedinoktauc$|^yedinoktadort$|^yedinoktabes$|^yedinoktaalti$|^yedinoktayedi$|^yedinoktasekiz$|^yedinoktadokuz$|^sekiznoktasifir$|^sekiznoktabir$|^sekiznoktaiki$|^sekiznoktauc$|^sekiznoktadort$|^sekiznoktabes$|^sekiznoktaalti$|^sekiznoktayedi$|^sekiznoktasekiz$|^sekiznoktadokuz$|^dokuznoktasifir$|^dokuznoktabir$|^dokuznoktaiki$|^dokuznoktauc$|^dokuznoktadort$|^dokuznoktabes$|^dokuznoktaalti$|^dokuznoktayedi$|^dokuznoktasekiz$|^dokuznoktadokuz$"

values = anaPatternValue

logexp = "^dogru$|^yanlis$"

# values = values.replace("$","")

binaop = "^\+$|^\-$|^\*$|^arti$|^eksi$|^carpi$"

logicop = "^ve$|^veya$"

values = values+"|"+AnaVariablesRegex+"|"+"^ac-parantez$"+"|"+"^kapa-parantez$"+"|"+"^\)$"+"|"+"^\($"+"|"+binaop+"|"+"^nokta$"+"|"+"^ve$"+"|"+"^veya$"

acparantezPattern = "^ac-parantez$|^\($"

kapaparantezPattern = "^kapa-parantez$|^\)$"

binexp = "^\d$|^\d\.\d$|^sifir$|^bir$|^iki$|^uc$|^dort$|^bes$|^alti$|^yedi$|^sekiz$|^dokuz$|^sifirnoktasifir$|^sifirnoktabir$|^sifirnoktaiki$|^sifirnoktauc$|^sifirnoktadort$|^sifirnoktabes$|^sifirnoktaalti$|^sifirnoktayedi$|^sifirnoktasekiz$|^sifirnoktadokuz$|^birnoktasifir$|^birnoktabir$|^birnoktaiki$|^birnoktauc$|^birnoktadort$|^birnoktabes$|^birnoktaalti$|^birnoktayedi$|^birnoktasekiz$|^birnoktadokuz$|^ikinoktasifir$|^ikinoktabir$|^ikinoktaiki$|^ikinoktauc$|^ikinoktadort$|^ikinoktabes$|^ikinoktaalti$|^ikinoktayedi$|^ikinoktasekiz$|^ikinoktadokuz$|^ucnoktasifir$|^ucnoktabir$|^ucnoktaiki$|^ucnoktauc$|^ucnoktadort$|^ucnoktabes$|^ucnoktaalti$|^ucnoktayedi$|^ucnoktasekiz$|^ucnoktadokuz$|^dortnoktasifir$|^dortnoktabir$|^dortnoktaiki$|^dortnoktauc$|^dortnoktadort$|^dortnoktabes$|^dortnoktaalti$|^dortnoktayedi$|^dortnoktasekiz$|^dortnoktadokuz$|^besnoktasifir$|^besnoktabir$|^besnoktaiki$|^besnoktauc$|^besnoktadort$|^besnoktabes$|^besnoktaalti$|^besnoktayedi$|^besnoktasekiz$|^besnoktadokuz$|^altinoktasifir$|^altinoktabir$|^altinoktaiki$|^altinoktauc$|^altinoktadort$|^altinoktabes$|^altinoktaalti$|^altinoktayedi$|^altinoktasekiz$|^altinoktadokuz$|^yedinoktasifir$|^yedinoktabir$|^yedinoktaiki$|^yedinoktauc$|^yedinoktadort$|^yedinoktabes$|^yedinoktaalti$|^yedinoktayedi$|^yedinoktasekiz$|^yedinoktadokuz$|^sekiznoktasifir$|^sekiznoktabir$|^sekiznoktaiki$|^sekiznoktauc$|^sekiznoktadort$|^sekiznoktabes$|^sekiznoktaalti$|^sekiznoktayedi$|^sekiznoktasekiz$|^sekiznoktadokuz$|^dokuznoktasifir$|^dokuznoktabir$|^dokuznoktaiki$|^dokuznoktauc$|^dokuznoktadort$|^dokuznoktabes$|^dokuznoktaalti$|^dokuznoktayedi$|^dokuznoktasekiz$|^dokuznoktadokuz$"



# Check Anadegiskenler
# print("----------")
for i in AnaDegiskenler:        
    # are "degeri" and "olsun" at the right place?
    if i[1]!="degeri" or i[-1]!="olsun":
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
    
    # are anavariable and anavalue valid?
    if len(i[0])>10 or not re.findall(anaPatternValue,i[2]) or i[0] in keywords:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()    
        
    for j in i[0]:
        if not j in PatternVariable:
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit() 

# print("----------")



# preprocess1
yeniLines = []
for i in lines[indexYeni+1:indexSonuc]:
    yeniLines += [i]



# Check if degeri and olsun in yenidegiskenler
# print("----------")
for i in yeniLines:
    if not "degeri" in i or not "olsun" in i:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()    




# Preprocess2
YeniDegiskenler = [i.split() for i in lines[indexYeni+1:indexSonuc]]
# print("----------")
# print(YeniDegiskenler)
for m in YeniDegiskenler:
    # print(m)
    if len(m)<4:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
    ctrl=""
    for j in m[2:-1]:
        ctrl+=j+" "
    ctrl = ctrl.rstrip()
    m[2]=ctrl
    for k in range(len(m)-4):
        m.pop(3)

# print(YeniDegiskenler)




# Check1
for i in YeniDegiskenler:
    
    # Does i have correct lenght?
    if len(i)!=4:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
        
    # are "degeri" and "olsun" at the right place?
    if i[1]!="degeri" or i[3]!="olsun":
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
        
    # is yenivariable valid?
    if len(i[0])>10 or i[0] in keywords or i[0] in variables:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
    
    for j in i[0]:
        if not j in PatternVariable:
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit() 

    variables.append(i[0])




# Check2

yenivalue=[]
for i in YeniDegiskenler:
    yenivalue+=[i[2].split()]
# print(yenivalue)






# Check if number of parantheses are equal
pcounter = 0
for i in yenivalue:

    if i.count("ac-parantez")+i.count("(")!=i.count("kapa-parantez")+i.count(")") or re.findall(kapaparantezPattern,i[0] or re.findall(acparantezPattern,i[-1])):
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
        
        

# define all values
tempstr=""
for i in variables:
    tempstr+="|"+i
    
realValues = anaPatternValue + tempstr

# print(realValues)       
        

counter = 0
for i in yenivalue:
    
    for j in range(len(i)):
        # print(i[j])
        # print(j in keywords)
        
        # Check if there are any unvalid characters
        if not re.findall(values,i[j]) and not i[j] in AnaVariables:
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
        
        
        # Close paranthes after ops => 2*)
        if j!=len(i)-1 and (re.findall(binaop,i[j]) or re.findall(logicop,i[j])) and re.findall(kapaparantezPattern, i[j+1]):
            # print("---------------------")
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
        
        # Ops after open paranthes => (*2
        if j!=len(i)-1 and (re.findall(acparantezPattern,i[j])) and (re.findall(logicop,i[j+1]) or re.findall(binaop,i[j+1])):
            # print("----------------------")
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
        # realValues after close parnthes => ) 2
        if j!=len(i)-1 and re.findall(kapaparantezPattern, i[j]) and (re.findall(realValues, i[j+1])):
            # print("-----------------")
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
        # open paranthes after real values => 2 (
        if j!=len(i)-1 and (re.findall(realValues, i[j])) and re.findall(acparantezPattern, i[j+1]):
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
        
        # Check => )( and ()
        if j!=len(i)-1 and ((re.findall(acparantezPattern, i[j]) and re.findall(kapaparantezPattern, i[j+1])) or (re.findall(kapaparantezPattern,i[j]) and re.findall(acparantezPattern, i[j+1]))):
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
        # Check - +, * *, + ve...
        if j!=len(i)-1 and (re.findall(binaop,i[j]) or re.findall(logicop,i[j])) and (re.findall(binaop,i[j+1]) or re.findall(logicop,i[j+1])):
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
        
        
        
        # Check if ops are at the beginning or end of the expression
        if (j == len(i)-1 or j == 0)  and (re.findall(binaop,i[j]) or re.findall(logicop,i[j])):       
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
        # check dogru + yanlis:
        if (j!=0 and re.findall(binaop,i[j]) and re.findall(logexp,i[j-1]) ) or (j!=len(i)-1 and re.findall(binaop,i[j]) and re.findall(logexp,i[j+1])):
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
        # check 4 ve 5:
        if (j!=0 and re.findall(logicop,i[j]) and re.findall(binexp,i[j-1]) ) or (j!=len(i)-1 and re.findall(logicop,i[j]) and re.findall(binexp,i[j+1])):
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
        # check dogru 4
        if j!=len(i)-1 and re.findall(realValues,i[j]) and re.findall(realValues,i[j+1]):
            # print(i[j],i[j+1])
            filew = open("calc.out","w")
            filew.write("Dont Let Me Down")
            filew.close()
            sys.exit()
            
            
    # Add the variable to values
    values = values + "|" + "^"+YeniDegiskenler[counter][0]+"$"
    counter+=1




#  Any sonuc statements?
if len(lines)-1==indexSonuc:
    filew = open("calc.out","w")
    filew.write("Here Comes The Sun")
    filew.close()
    sys.exit() 




# Check sonuc statement
if indexSonuc!=len(lines)-2 and indexSonuc!=len(lines)-1:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()




sonucList = []
for i in lines[indexSonuc+1:]:
    sonucList = i.rstrip().lstrip().split()
# print(sonucList)
if len(sonucList)==1:
    if not sonucList[0] in variables and not re.findall(anaPatternValue,sonucList[0]):
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()   
        
    else:
        filew = open("calc.out","w")
        filew.write("Here Comes The Sun")
        filew.close()
        sys.exit() 
    
      

for i in range(len(sonucList)):
 
        # Check if there are any unvalid characters
    if not re.findall(values,sonucList[i]) and not sonucList[i] in AnaVariables:
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
        

    
        # Close paranthes after ops => 2*)
    if i!=len(sonucList)-1 and (re.findall(binaop,sonucList[i]) or re.findall(logicop,sonucList[i])) and re.findall(kapaparantezPattern, sonucList[i+1]):
        # print("---------------------")
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
 
        # Ops after open paranthes => (*2
    if i!=len(sonucList)-1 and (re.findall(acparantezPattern,sonucList[i])) and (re.findall(logicop,sonucList[i+1]) or re.findall(binaop,sonucList[i+1])):
        # print("----------------------")
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
      
        # realValues after close parnthes => ) 2
    if i!=len(sonucList)-1 and re.findall(kapaparantezPattern, sonucList[i]) and (re.findall(realValues, sonucList[i+1])):
        # print("-----------------")
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
            
        # open paranthes after real values => 2 (
    if i!=len(sonucList)-1 and (re.findall(realValues, sonucList[i])) and re.findall(acparantezPattern, sonucList[i+1]):
        # print("-----------------")
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
        

        # Check => )( and ()
    if i!=len(sonucList)-1 and ((re.findall(acparantezPattern, sonucList[i]) and re.findall(kapaparantezPattern, sonucList[i+1])) or (re.findall(kapaparantezPattern,sonucList[i+1]) and re.findall(acparantezPattern, sonucList[i+1]))):
        # print("-----------------")
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
            
        # Check - +, * *, + ve...
    if i!=len(sonucList)-1 and (re.findall(binaop,sonucList[i]) or re.findall(logicop,sonucList[i])) and (re.findall(binaop,sonucList[i+1]) or re.findall(logicop,sonucList[i+1])):
        # print("-----------------")
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
        
        
        
    # Check if ops are at the beginning or end of the expression
    if (i==len(sonucList)-1 or i == 0)  and (re.findall(binaop,sonucList[i]) or re.findall(logicop,sonucList[i])):  
        # print(sonucList[i])
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
     
        # check dogru + yanlis:
    if (i!=0 and re.findall(binaop,sonucList[i]) and re.findall(logexp,sonucList[i-1]) ) or (i!=len(sonucList)-1 and re.findall(binaop,sonucList[i]) and re.findall(logexp,sonucList[i+1])):
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
       
        # check 4 ve 5:
    if (i!=0 and re.findall(logicop,sonucList[i]) and re.findall(binexp,sonucList[i-1]) ) or (i!=len(sonucList)-1 and re.findall(logicop,sonucList[i]) and re.findall(binexp,sonucList[i+1])):
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()
    
        # check dogru 4
    if i!=len(sonucList)-1 and re.findall(realValues,sonucList[i]) and re.findall(realValues,sonucList[i+1]):
        filew = open("calc.out","w")
        filew.write("Dont Let Me Down")
        filew.close()
        sys.exit()


   
filew = open("calc.out","w")
filew.write("Here Comes The Sun")
filew.close()
sys.exit()    








