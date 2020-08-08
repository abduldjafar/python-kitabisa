input1=input("input1:")
input2=input("input2:")

input1 = input1.split(",")
input2 = input2.split(",")

lenInput1 = len(input1)
lenInput2 = len(input2)

def samakan_list(input1,input2):
    temp_len = len(input1) - len(input2)
    for temp_data in range(0, temp_len):
        input2.append("NULL")

    return input2

if lenInput1> lenInput2:
    input2 = samakan_list(input1,input2)
if lenInput1 < lenInput2:
    input1 = samakan_list(input2,input1)

output = ",".join(["["+input1[x]+":"+input2[x]+"]" for x in range(0,len(input1))])

print("output: "+output)