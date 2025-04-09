# Media mobile

st = input("Enter a list of numbers separated by ',': ")
n = int(input("Enter n value: "))

l_int = []

for e in st.split(','):
    k = int(e)
    l_int.append(k)

results = []

def moving_average (l, n):
    for i in range(1, len(l)+1):
        if i <= n:
            window = l[0:i]
            aver = sum(window)/len(window)
            results.append(aver)
        else:
            window = l[i-n:i]
            aver = sum(window)/len(window)
            results.append(aver)



mov_ave = moving_average(l_int, n) 

print(results)