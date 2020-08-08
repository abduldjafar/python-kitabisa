data = input("input:")
x = 0
num = 0
output = []
while True:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            output.append(str(num))
            x = x +1
            if x == int(data):
                break
    num = num + 1
print("ouput: "+",".join(output))