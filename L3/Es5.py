# Calcolo media

l_nums = map(int, list(input("Enter a list of numbers: ").split(',')))

l = list(l_nums)

print(f"Average: {sum(l)/len(l):.2f}")