ar = [[0 for _ in range(4)] for _ in range(6)]
categories = ["Input", "File", "Query", "Interface", "Output"]

for i, category in enumerate(categories):
    ar[i][0] = int(input(f"Enter Initial Value of {category}: "))

w1 = float(input(f"Enter Weighing Factor of Simple (default 0.5): ") or 0.5)
w2 = float(input(f"Enter Weighing Factor of Average (default 1.0): ") or 1.0)
w3 = float(input(f"Enter Weighing Factor of Complex (default 1.5): ") or 1.5)

for i, category in enumerate(categories):
    inputt = input(f"Enter Input Ratio of '{category}': ")
    if ":" in inputt:
        temp = list(map(int, inputt.split(":")))
        total = sum(temp)
        for j in range(3):
            ar[i][j + 1] = temp[j] * ar[i][0] // total
    else:
        j = ["simple", "average", "complex"].index(inputt.lower())
        ar[i][j + 1] = ar[i][0]

ar[5][1:] = [sum(ar[i][j] for i in range(5)) for j in range(1, 4)]

print("Enter Features of the Product (Enter 00 to Stop): ")
arr = []
while (temp := input()) != "00":
    arr.append(temp)

ufp = sum(w * ar[5][i + 1] for i, w in enumerate([w1, w2, w3]))
print(f"Un-adjusted Function Point: {ufp}")

tdi = sum(float(i[:-1]) / 100 if "%" in i else float(i) for i in arr)
print(f"Total Degree of Influence: {tdi}")

vaf = 0.01 * tdi + 0.65
print(f"Value Added Factor: {vaf}")

afp = vaf * ufp
print(f"Adjusted Function Point: {afp}")
